#!/usr/bin/env python3
"""
Simple Takeoff and Land Script using DroneKit

Connects to ArduPilot vehicle, arms, takes off to specified altitude,
hovers briefly, and lands.

Requirements:
 - ArduPilot flight controller (Pixhawk, Cube, etc.)
 - DroneKit library: pip install dronekit
 - MAVProxy or direct serial/UDP connection

Usage:
 python3 simple_takeoff.py --connect /dev/ttyUSB0  # Serial
 python3 simple_takeoff.py --connect udp:127.0.0.1:14550  # SITL simulator

Safety:
 - Test in simulator (SITL) first
 - Remove propellers for initial tests
 - Always have manual override ready
 - Fly in open area, no obstacles

Author: Unmanned Vehicle Edu Hub
License: MIT
"""

from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import argparse

def arm_and_takeoff(vehicle, target_altitude):
    """
    Arms vehicle and flies to target_altitude.

    Args:
        vehicle: Connected Vehicle object
        target_altitude: Target altitude in meters
    """

    print("Basic pre-arm checks")
    # Don't let the user try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialize...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Armed!")

    print(f"Taking off to {target_altitude}m")
    vehicle.simple_takeoff(target_altitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height
    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print(f" Altitude: {altitude:.1f}m")

        # Break and return from function when reach target altitude
        if altitude >= target_altitude * 0.95:  # Trigger at 95% of target alt
            print("Reached target altitude")
            break

        time.sleep(1)

def land_vehicle(vehicle):
    """
    Commands vehicle to land.

    Args:
        vehicle: Connected Vehicle object
    """
    print("Landing...")
    vehicle.mode = VehicleMode("LAND")

    # Wait until disarmed (landed)
    while vehicle.armed:
        altitude = vehicle.location.global_relative_frame.alt
        print(f" Altitude: {altitude:.1f}m")
        time.sleep(1)

    print("Landed and disarmed")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Simple DroneKit Takeoff Example')
    parser.add_argument('--connect', default='/dev/ttyUSB0',
                        help="Vehicle connection target (default: /dev/ttyUSB0)")
    parser.add_argument('--altitude', type=float, default=10.0,
                        help="Target altitude in meters (default: 10)")
    parser.add_argument('--hover-time', type=float, default=10.0,
                        help="Hover time in seconds (default: 10)")
    args = parser.parse_args()

    print("=" * 50)
    print("Simple Takeoff Script")
    print("=" * 50)
    print(f"Connecting to vehicle on: {args.connect}")

    # Connect to the Vehicle
    try:
        vehicle = connect(args.connect, wait_ready=True, baud=57600, timeout=60)
    except Exception as e:
        print(f"Error connecting to vehicle: {e}")
        return

    try:
        # Display basic vehicle state
        print("\nVehicle Information:")
        print(f" Autopilot Firmware version: {vehicle.version}")
        print(f" Mode: {vehicle.mode.name}")
        print(f" Armed: {vehicle.armed}")
        print(f" GPS: {vehicle.gps_0}")
        print(f" Battery: {vehicle.battery}")
        print(f" Location: {vehicle.location.global_relative_frame}")

        # Arm and takeoff
        arm_and_takeoff(vehicle, args.altitude)

        # Hover for specified time
        print(f"\nHovering for {args.hover_time} seconds...")
        for i in range(int(args.hover_time)):
            altitude = vehicle.location.global_relative_frame.alt
            battery = vehicle.battery.voltage
            print(f" Time: {i+1}s | Altitude: {altitude:.1f}m | Battery: {battery:.1f}V")
            time.sleep(1)

        # Land
        land_vehicle(vehicle)

        print("\nMission complete!")

    except KeyboardInterrupt:
        print("\nScript interrupted by user")
        print("Attempting emergency landing...")
        vehicle.mode = VehicleMode("LAND")

    except Exception as e:
        print(f"\nError during flight: {e}")
        print("Attempting emergency landing...")
        vehicle.mode = VehicleMode("LAND")

    finally:
        print("\nClosing vehicle connection...")
        vehicle.close()
        print("Done.")

if __name__ == "__main__":
    main()
