---
title: Glossary of Unmanned Vehicle Systems Terms
description: Comprehensive glossary of terminology for unmanned aerial, ground, and marine vehicle systems
---

# Glossary

This glossary provides definitions for common terms used in unmanned vehicle systems. Terms are organized alphabetically with category tags for easy navigation.

## How to Use This Glossary

- **Alphabetical listing** below provides all terms
- **Category filters** help find related terms
- **Cross-references** link related concepts
- Click category tags to see similar terms

### Categories

- 🚁 **Aerial** - Specific to UAVs/drones
- 🚗 **Ground** - Specific to UGVs/rovers
- 🚤 **Marine** - Specific to USVs/boats
- 🔧 **Hardware** - Physical components
- 💻 **Software** - Programming and control
- ⚡ **Power** - Batteries and power systems
- 📡 **Communication** - Radio and telemetry
- 🛡️ **Safety** - Safety-related terms
- ⚖️ **Regulatory** - Legal and compliance

---

## A

### Accelerometer
**Categories:** 🔧 Hardware | 💻 Software

A sensor that measures acceleration forces. Part of the IMU, it detects changes in velocity and orientation. Essential for stabilization and navigation.

**See also:** IMU, Gyroscope

---

### AGL (Above Ground Level)
**Categories:** 🚁 Aerial | ⚖️ Regulatory

Altitude measured from the ground directly below the aircraft, rather than sea level. FAA regulations specify 400 feet AGL maximum for most recreational/Part 107 operations.

**See also:** MSL, Altitude

---

### Altitude
**Categories:** 🚁 Aerial | 💻 Software

Vertical distance above a reference point (usually ground or sea level). Can be measured by barometer, GPS, or ultrasonic sensors.

**See also:** AGL, MSL

---

### ARF (Almost-Ready-to-Fly)
**Categories:** 🔧 Hardware

A platform that requires significant assembly including soldering, component installation, and configuration. Usually includes frame, motors, ESCs, and flight controller but needs integration.

**See also:** RTF, BNF, Build Levels

---

### Arming
**Categories:** 💻 Software | 🛡️ Safety

The process of enabling motors to spin. Safety feature that prevents accidental motor activation. Usually requires specific stick combination or switch on transmitter.

**See also:** Disarming, Failsafe

---

### Autopilot
**Categories:** 💻 Software

Software system that controls vehicle automatically, executing missions without direct pilot input. Examples: ArduPilot, PX4, DJI flight systems.

**See also:** Flight Controller, Waypoint, Autonomous

---

### Autonomous
**Categories:** 💻 Software

Operating independently without human control. Levels range from simple altitude hold to complex AI-driven decision making.

**See also:** Autopilot, Semi-Autonomous, Manual Control

---

### AUV (Autonomous Underwater Vehicle)
**Categories:** 🚤 Marine

Unmanned vehicle that operates underwater without tether, carrying its own power and navigation. Used for ocean research, inspection, etc.

**See also:** USV, ROV

---

## B

### Barometer
**Categories:** 🔧 Hardware | 💻 Software

Atmospheric pressure sensor used to measure altitude. More accurate than GPS for altitude, but drifts with weather changes.

**See also:** GPS, Altitude

---

### Battery Monitor/Alarm
**Categories:** ⚡ Power | 🛡️ Safety

Device that monitors LiPo battery voltage and alerts when cells drop below safe level (typically 3.5V). Critical safety equipment.

**See also:** LiPo, Voltage, C-Rating

---

### BEC (Battery Eliminator Circuit)
**Categories:** ⚡ Power | 🔧 Hardware

Voltage regulator that provides stable power to electronics (receiver, servos) from main battery. Eliminates need for separate receiver battery.

**See also:** ESC, Voltage Regulator

---

### Betaflight
**Categories:** 💻 Software | 🚁 Aerial

Popular open-source flight controller firmware for multirotors, especially racing and freestyle drones. Known for excellent tuning and performance.

**See also:** Cleanflight, Flight Controller, ArduPilot

---

### BNF (Bind-and-Fly)
**Categories:** 🔧 Hardware

Platform that comes fully assembled but without transmitter/receiver. User must "bind" their own compatible radio system.

**See also:** RTF, ARF, Binding

---

### Binding
**Categories:** 📡 Communication

Process of pairing a transmitter with a receiver so they communicate exclusively. Prevents interference from other radios.

**See also:** BNF, Transmitter, Receiver

---

### Brushless Motor
**Categories:** 🔧 Hardware | ⚡ Power

Electric motor type using electronic commutation instead of physical brushes. More efficient, powerful, and durable than brushed motors. Standard for drones.

**See also:** ESC, KV, Motor

---

## C

### C-Rating
**Categories:** ⚡ Power

Battery specification indicating maximum safe discharge rate. Formula: Max Amps = Capacity (Ah) × C-Rating. Example: 1500mAh (1.5Ah) × 50C = 75A max.

**See also:** LiPo, Capacity, Discharge Rate

---

### CAN Bus
**Categories:** 💻 Software | 📡 Communication

Controller Area Network - robust serial bus standard for connecting sensors, ESCs, and other components. Used in advanced systems.

**See also:** Communication Protocol, ESC

---

### Capacity (Battery)
**Categories:** ⚡ Power

Amount of energy a battery stores, measured in milliamp-hours (mAh) or amp-hours (Ah). Higher capacity = longer runtime but heavier battery.

**See also:** LiPo, C-Rating, Runtime

---

### Center of Gravity (CG)
**Categories:** 🔧 Hardware | 🚁 Aerial

Balance point of vehicle. Critical for aerial platforms - improper CG causes instability. Should be near geometric center for multirotors.

**See also:** Trim, Balance

---

### Cleanflight
**Categories:** 💻 Software | 🚁 Aerial

Open-source flight controller firmware, predecessor to Betaflight. Still used on some platforms.

**See also:** Betaflight, Flight Controller

---

### Compass/Magnetometer
**Categories:** 🔧 Hardware | 💻 Software

Sensor that measures magnetic field direction to determine heading. Critical for GPS navigation and return-to-home. Requires calibration and should be mounted away from magnetic interference.

**See also:** GPS, IMU, Calibration

---

### Crash
**Categories:** 🛡️ Safety

Uncontrolled impact with ground or obstacle. Ranges from minor tip-over to complete destruction. Always inspect before flying again.

**See also:** Hard Landing, Failsafe

---

## D

### Differential Drive
**Categories:** 🚗 Ground

Steering method using different wheel speeds on left vs. right sides. Common in rovers and tanks. Simple but effective.

**See also:** UGV, Rover, Skid Steering

---

### Disarming
**Categories:** 💻 Software | 🛡️ Safety

Disabling motors so they cannot spin. Critical safety procedure after every landing.

**See also:** Arming, Emergency Stop

---

### Drone
**Categories:** 🚁 Aerial

Common term for UAV (Unmanned Aerial Vehicle). Originally referred to autonomous aircraft; now used broadly for all remote/autonomous flying vehicles.

**See also:** UAV, UAS, Multirotor

---

## E

### ESC (Electronic Speed Controller)
**Categories:** 🔧 Hardware | ⚡ Power

Electronic device that controls motor speed based on flight controller commands. Converts battery DC power to three-phase AC for brushless motors.

**See also:** Motor, Flight Controller, BEC

---

## F

### Failsafe
**Categories:** 🛡️ Safety | 💻 Software

Automated safety action when signal is lost. Common failsafes: return-to-home, hover, land, or cut motors. Must be configured and tested.

**See also:** RTH, Signal Loss, Safety

---

### Fixed-Wing
**Categories:** 🚁 Aerial

Aircraft with rigid wings that generate lift through forward motion. More efficient than multirotor for long distance/endurance but requires runway or catapult.

**See also:** Multirotor, VTOL, UAV

---

### Flight Controller (FC)
**Categories:** 🔧 Hardware | 💻 Software

Central computer that stabilizes vehicle and executes flight commands. Contains sensors (IMU) and runs firmware (Betaflight, ArduPilot, etc.).

**See also:** Autopilot, IMU, Firmware

---

### Flight Mode
**Categories:** 💻 Software

Different control behaviors: Manual (pilot does everything), Stabilize (self-levels), Altitude Hold, GPS Hold, Autonomous, etc.

**See also:** Stabilization, GPS, Autonomous

---

### FPV (First-Person View)
**Categories:** 🚁 Aerial | 📡 Communication

Operating vehicle by watching real-time video from onboard camera, typically through goggles or monitor. Popular for racing and immersive flight.

**See also:** LOS, Video Transmitter, Goggles

---

### Frame
**Categories:** 🔧 Hardware

Structural body of vehicle. For multirotors, usually carbon fiber or plastic. Size measured by motor-to-motor diagonal (e.g., "5-inch quad").

**See also:** Airframe, Chassis

---

## G

### Geofence
**Categories:** 💻 Software | 🛡️ Safety

Virtual boundary programmed into vehicle. Prevents flight/movement outside defined area. Important safety feature for autonomous operations.

**See also:** GPS, Autonomous, Safety

---

### Gimbal
**Categories:** 🔧 Hardware | 🚁 Aerial

Stabilized camera mount that keeps camera level regardless of vehicle movement. Uses motors and IMU to counteract vibrations.

**See also:** Camera, Stabilization

---

### GPS (Global Positioning System)
**Categories:** 🔧 Hardware | 💻 Software

Satellite navigation system providing position, altitude, and velocity. Required for waypoint navigation, return-to-home, and position hold. Needs clear sky view.

**See also:** GNSS, Waypoint, RTH

---

### Ground Control Station (GCS)
**Categories:** 💻 Software | 📡 Communication

Computer/tablet application for planning missions, monitoring telemetry, and configuring vehicle. Examples: Mission Planner, QGroundControl.

**See also:** Telemetry, MAVLink

---

### Gyroscope
**Categories:** 🔧 Hardware | 💻 Software

Sensor measuring rotational velocity. Part of IMU, essential for stabilization. Detects pitch, roll, and yaw rates.

**See also:** IMU, Accelerometer, Stabilization

---

## H

### Hard Landing
**Categories:** 🛡️ Safety | 🚁 Aerial

Landing with high descent rate or impact force. Can damage components. Always inspect after hard landing.

**See also:** Crash, Landing

---

### Hexacopter
**Categories:** 🚁 Aerial

Multirotor with six rotors. More lift and redundancy than quadcopter, but heavier and more complex.

**See also:** Quadcopter, Multirotor, Octocopter

---

### Hover
**Categories:** 🚁 Aerial

Maintaining stationary position in air. Multirotors can hover in place; fixed-wing cannot.

**See also:** Loiter, Position Hold

---

## I

### IMU (Inertial Measurement Unit)
**Categories:** 🔧 Hardware | 💻 Software

Sensor package containing accelerometer and gyroscope (sometimes magnetometer). Provides orientation and motion data for stabilization.

**See also:** Accelerometer, Gyroscope, Flight Controller

---

## K

### Kalman Filter
**Categories:** 💻 Software

Advanced sensor fusion algorithm combining multiple sensors (GPS, barometer, accelerometer) for accurate position/velocity estimates.

**See also:** Sensor Fusion, GPS

---

### KV (Motor Constant)
**Categories:** 🔧 Hardware | ⚡ Power

Motor specification: RPM per volt applied. Higher KV = faster spin, lower torque. Low KV (1000-1500) for large props, high KV (2300-2700) for small racing props.

**See also:** Motor, Brushless Motor, Propeller

---

## L

### LAANC (Low Altitude Authorization and Notification Capability)
**Categories:** ⚖️ Regulatory | 🚁 Aerial

FAA system providing near-instant airspace authorization for controlled airspace. Available through apps like Aloft, AirMap.

**See also:** Airspace, FAA, Part 107

---

### LiPo (Lithium Polymer Battery)
**Categories:** ⚡ Power | 🛡️ Safety

Rechargeable battery type standard in unmanned vehicles. High power density but requires careful handling. Cell voltage: 3.7V nominal, 4.2V charged, 3.0V minimum.

**See also:** Battery Safety, C-Rating, Capacity

---

### LOS (Line of Sight)
**Categories:** ⚖️ Regulatory | 🚁 Aerial

Operating vehicle while maintaining direct visual contact (not through camera/screen). Required by FAA regulations.

**See also:** VLOS, FPV, Regulations

---

## M

### mAh (Milliamp-Hour)
**Categories:** ⚡ Power

Battery capacity measurement. 1000mAh = 1Ah. Indicates how long battery can supply current.

**See also:** Capacity, Battery, Amp-Hour

---

### Manual Control
**Categories:** 💻 Software

Flight mode where pilot directly controls all vehicle movements. No stabilization or assistance (except basic rate stabilization).

**See also:** Flight Mode, Stabilization, Autonomous

---

### MAVLink
**Categories:** 💻 Software | 📡 Communication

Lightweight messaging protocol for communication between ground station and vehicle. Standard for ArduPilot and PX4.

**See also:** Telemetry, Ground Control Station

---

### Mission
**Categories:** 💻 Software

Pre-programmed series of waypoints and actions for autonomous flight/drive.

**See also:** Waypoint, Autonomous, GCS

---

### Motor
**Categories:** 🔧 Hardware | ⚡ Power

Propulsion device. Brushless motors standard for drones. Measured by size (2207 = 22mm diameter, 7mm height) and KV rating.

**See also:** Brushless Motor, ESC, KV, Propeller

---

### MSL (Mean Sea Level)
**Categories:** 🚁 Aerial | 💻 Software

Altitude measured from average sea level. Used in aviation charts. GPS reports MSL altitude.

**See also:** AGL, Altitude

---

### Multirotor
**Categories:** 🚁 Aerial

Rotary-wing aircraft with multiple motors/propellers. Includes tricopters, quadcopters, hexacopters, and octocopters.

**See also:** Quadcopter, Drone, UAV

---

## O

### Octocopter
**Categories:** 🚁 Aerial

Multirotor with eight motors. Maximum lift and redundancy, but heavy and complex. Used for heavy lift applications.

**See also:** Multirotor, Hexacopter, Quadcopter

---

### OSD (On-Screen Display)
**Categories:** 💻 Software | 📡 Communication

Overlay of telemetry data (battery voltage, altitude, etc.) on FPV video feed. Critical for FPV flying.

**See also:** FPV, Telemetry

---

## P

### Part 107
**Categories:** ⚖️ Regulatory | 🚁 Aerial

FAA regulation governing commercial drone operations in USA. Requires Remote Pilot Certificate (test), registration, and operational compliance.

**See also:** TRUST, FAA, Commercial Operation

---

### PID (Proportional-Integral-Derivative)
**Categories:** 💻 Software

Control algorithm that stabilizes vehicle by adjusting motor outputs based on sensor feedback. Tuning PID values critical for stable flight.

**See also:** Tuning, Flight Controller, Stabilization

---

### Pitch
**Categories:** 💻 Software | 🚁 Aerial

Rotation around lateral axis (nose up/down). Forward/backward tilt in multirotors.

**See also:** Roll, Yaw, Attitude

---

### Pixhawk
**Categories:** 🔧 Hardware | 💻 Software

Popular open-source autopilot hardware platform. Runs ArduPilot or PX4 firmware. Industry standard for research and DIY.

**See also:** Flight Controller, ArduPilot, PX4

---

### Propeller (Prop)
**Categories:** 🔧 Hardware | 🚁 Aerial

Rotating blade that generates thrust. Measured by diameter × pitch (e.g., 5×4.3 = 5" diameter, 4.3" pitch). Matched to motor KV and voltage.

**See also:** Motor, Thrust, KV

---

### PWM (Pulse Width Modulation)
**Categories:** 💻 Software | 📡 Communication

Signal type used to control motor speed and servo position. Vary pulse width (typically 1000-2000 microseconds) to set output.

**See also:** ESC, Servo, Signal

---

### PX4
**Categories:** 💻 Software

Open-source autopilot firmware for Pixhawk and compatible hardware. Alternative to ArduPilot, focuses on research/commercial use.

**See also:** ArduPilot, Pixhawk, Flight Controller

---

## Q

### Quadcopter
**Categories:** 🚁 Aerial

Multirotor with four motors arranged in X or + configuration. Most common drone type due to simplicity and efficiency.

**See also:** Multirotor, Hexacopter, Drone

---

## R

### Receiver (RX)
**Categories:** 📡 Communication | 🔧 Hardware

Radio receiver that picks up signals from transmitter. Outputs control signals to flight controller.

**See also:** Transmitter, Binding, Radio

---

### Roll
**Categories:** 💻 Software | 🚁 Aerial

Rotation around longitudinal axis (tilt left/right). Side-to-side tilt in multirotors.

**See also:** Pitch, Yaw, Attitude

---

### ROS (Robot Operating System)
**Categories:** 💻 Software | 🚗 Ground

Open-source robotics middleware providing tools, libraries, and conventions. Standard in research robotics.

**See also:** Software, UGV, Autonomous

---

### Rover
**Categories:** 🚗 Ground

Ground-based unmanned vehicle. Ranges from simple wheeled platforms to complex autonomous robots.

**See also:** UGV, Differential Drive

---

### ROV (Remotely Operated Vehicle)
**Categories:** 🚤 Marine

Underwater vehicle controlled via tether. Power and control through cable. Differs from AUV (autonomous, no tether).

**See also:** AUV, USV, Underwater

---

### RTF (Ready-to-Fly)
**Categories:** 🔧 Hardware

Platform requiring minimal assembly - typically just battery charging. Includes everything needed to operate.

**See also:** BNF, ARF, Build Levels

---

### RTH (Return-to-Home)
**Categories:** 💻 Software | 🛡️ Safety

Autonomous function that navigates vehicle back to takeoff point or pre-set home location. Common failsafe action.

**See also:** GPS, Failsafe, Autonomous

---

## S

### SLAM (Simultaneous Localization and Mapping)
**Categories:** 💻 Software | 🚗 Ground

Advanced algorithm for autonomous navigation in unknown environments. Robot builds map while determining its position.

**See also:** Autonomous, Sensor Fusion, UGV

---

### Stabilization
**Categories:** 💻 Software | 🚁 Aerial

Automatic leveling and smoothing of vehicle movements. Flight controller uses IMU sensors to counteract disturbances.

**See also:** PID, IMU, Flight Mode

---

## T

### Telemetry
**Categories:** 📡 Communication | 💻 Software

Real-time transmission of vehicle data (battery, GPS, altitude, etc.) to ground station or controller. Essential for monitoring.

**See also:** MAVLink, OSD, Radio

---

### Throttle
**Categories:** 💻 Software | ⚡ Power

Control of motor power/speed. Vertical control for multirotors, forward speed for fixed-wing and ground vehicles.

**See also:** Motor, Control

---

### Thrust
**Categories:** 🔧 Hardware | 🚁 Aerial

Force generated by propellers. Thrust-to-weight ratio determines climb rate and agility. Ratio >2:1 needed for acrobatics.

**See also:** Motor, Propeller, Weight

---

### Transmitter (TX)
**Categories:** 📡 Communication | 🔧 Hardware

Handheld radio controller sending pilot commands to vehicle. Features sticks, switches, and knobs for control.

**See also:** Receiver, Radio, Binding

---

### TRUST Test
**Categories:** ⚖️ Regulatory | 🚁 Aerial

FAA-required recreational UAS Safety Test. Free online test covering basic aeronautical knowledge and safety. Required for all recreational drone operators.

**See also:** Part 107, FAA, Recreational

---

### Tuning
**Categories:** 💻 Software

Process of adjusting PID values and other parameters for optimal performance and stability.

**See also:** PID, Flight Controller, Betaflight

---

## U

### UAV (Unmanned Aerial Vehicle)
**Categories:** 🚁 Aerial

Aircraft operated without pilot on board. Synonymous with "drone."

**See also:** UAS, Drone, Multirotor

---

### UAS (Unmanned Aircraft System)
**Categories:** 🚁 Aerial | ⚖️ Regulatory

Complete system including UAV, ground control station, communication links, and personnel. Preferred FAA terminology.

**See also:** UAV, Drone

---

### UGV (Unmanned Ground Vehicle)
**Categories:** 🚗 Ground

Vehicle operating on land without human driver. Ranges from simple RC cars to complex autonomous robots.

**See also:** Rover, Autonomous

---

### USV (Unmanned Surface Vehicle)
**Categories:** 🚤 Marine

Watercraft operating on water surface without crew. Differs from AUV (underwater).

**See also:** AUV, ROV, Marine

---

## V

### VLOS (Visual Line of Sight)
**Categories:** ⚖️ Regulatory | 🚁 Aerial

FAA requirement that operator maintain direct visual contact with aircraft at all times (not through FPV camera).

**See also:** LOS, FPV, Regulations

---

### Voltage
**Categories:** ⚡ Power

Electrical potential difference. Battery voltage indicates charge state. LiPo cells: 4.2V full, 3.7V nominal, 3.0V minimum.

**See also:** LiPo, Battery, Current

---

### VTOL (Vertical Takeoff and Landing)
**Categories:** 🚁 Aerial

Aircraft capable of hovering and vertical flight (like helicopter) plus forward flight (like airplane). Combines multirotor and fixed-wing advantages.

**See also:** Fixed-Wing, Multirotor, Hybrid

---

## W

### Waypoint
**Categories:** 💻 Software

GPS coordinate in autonomous mission. Vehicle navigates from waypoint to waypoint.

**See also:** GPS, Mission, Autonomous

---

### Weight
**Categories:** 🔧 Hardware

Total mass of vehicle. Critical specification - affects flight time, regulations (250g threshold), and performance.

**See also:** Thrust, Payload, Regulations

---

## Y

### Yaw
**Categories:** 💻 Software | 🚁 Aerial

Rotation around vertical axis (heading change). Spinning left/right for multirotors.

**See also:** Pitch, Roll, Heading

---

## Acronym Quick Reference

| Acronym | Full Term | Category |
|---------|-----------|----------|
| **AGL** | Above Ground Level | Aerial |
| **ARF** | Almost-Ready-to-Fly | Hardware |
| **AUV** | Autonomous Underwater Vehicle | Marine |
| **BEC** | Battery Eliminator Circuit | Power |
| **BNF** | Bind-and-Fly | Hardware |
| **CAN** | Controller Area Network | Communication |
| **CG** | Center of Gravity | Hardware |
| **ESC** | Electronic Speed Controller | Hardware |
| **FC** | Flight Controller | Hardware/Software |
| **FPV** | First-Person View | Aerial |
| **GCS** | Ground Control Station | Software |
| **GNSS** | Global Navigation Satellite System | Hardware |
| **GPS** | Global Positioning System | Hardware |
| **IMU** | Inertial Measurement Unit | Hardware |
| **KV** | Motor Constant (RPM/Volt) | Hardware |
| **LAANC** | Low Altitude Authorization | Regulatory |
| **LiPo** | Lithium Polymer | Power |
| **LOS** | Line of Sight | Regulatory |
| **mAh** | Milliamp-Hour | Power |
| **MSL** | Mean Sea Level | Aerial |
| **OSD** | On-Screen Display | Software |
| **PID** | Proportional-Integral-Derivative | Software |
| **PPE** | Personal Protective Equipment | Safety |
| **PWM** | Pulse Width Modulation | Communication |
| **ROV** | Remotely Operated Vehicle | Marine |
| **RTF** | Ready-to-Fly | Hardware |
| **RTH** | Return-to-Home | Software/Safety |
| **RX** | Receiver | Communication |
| **SLAM** | Simultaneous Localization And Mapping | Software |
| **TX** | Transmitter | Communication |
| **UAV** | Unmanned Aerial Vehicle | Aerial |
| **UAS** | Unmanned Aircraft System | Aerial |
| **UGV** | Unmanned Ground Vehicle | Ground |
| **USV** | Unmanned Surface Vehicle | Marine |
| **VLOS** | Visual Line of Sight | Regulatory |
| **VTOL** | Vertical Takeoff and Landing | Aerial |

---

## Contributing to Glossary

Found a term missing or definition unclear?

[Suggest an improvement →](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub/issues)

---

**Last Updated:** November 2025
**Terms:** 75+ definitions covering aerial, ground, marine, and general unmanned systems terminology
