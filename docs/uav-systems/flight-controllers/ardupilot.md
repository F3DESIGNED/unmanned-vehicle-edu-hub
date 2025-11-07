# ArduPilot Flight Controller System

ArduPilot is an advanced, open-source autopilot system perfect for educational environments focused on autonomous operations, mission planning, and research applications.

## Overview

**ArduPilot** is a full-featured autopilot platform supporting multirotors, fixed-wing, rovers, boats, and more. It excels in autonomous missions, sensor integration, and advanced programming.

### Key Features
- **Multi-Platform**: Copter, Plane, Rover, Sub, Antenna Tracker
- **Mission Planning**: Complex waypoint missions with conditions
- **Extensive Sensor Support**: GPS, optical flow, rangefinders, cameras
- **Programming Interface**: DroneKit (Python), MAVLink, ROS integration
- **Mature Ecosystem**: 15+ years of development, large community
- **Advanced Features**: Precision landing, object avoidance, follow-me

### Educational Strengths
- Professional-grade autonomous capabilities
- Excellent for STEM/robotics competitions (AUVSI SUAS, others)
- Python programming with DroneKit
- Comprehensive logging for analysis
- Research-appropriate platform

### Challenges
- Steeper learning curve than racing firmware
- More complex configuration
- Requires understanding of multiple ground station software
- May be overkill for simple FPV/manual flight

## Supported Hardware

### Flight Controller Boards

#### Pixhawk Family (Recommended for Education)

**Pixhawk 4 / Pixhawk 6C**
- Modern standard, excellent sensors
- Multiple redundant IMUs and power inputs
- CAN bus support for peripherals
- Cost: $150-250
- **Best For**: High school, post-secondary, research

**Pixhawk 2.4.8 (Original Pixhawk Clone)**
- Widely available, well-supported
- Good sensor suite
- Cost: $60-100
- **Best For**: Budget educational builds, introductory courses

**Holybro Kakute H7 / Matek H743**
- Smaller form factor for racing frames
- ArduPilot compatible
- Cost: $80-120
- **Best For**: Hybrid autonomous racing projects

#### The Cube Series
- **Cube Orange**, **Cube Purple**: High-end professional
- Excellent vibration isolation
- Redundant systems
- Cost: $250-400
- **Best For**: Research, professional education programs

#### Raspberry Pi + Navio2/Navio2+
- Complete ArduPilot system on Raspberry Pi platform
- Onboard Linux computer for companion capabilities
- Cost: $180-220 (with Pi)
- **Best For**: Advanced programming, computer vision integration

### Companion Computers
Run alongside flight controller for advanced processing:

- **Raspberry Pi 4 (4GB)**: Most common, excellent support
- **NVIDIA Jetson Nano**: Computer vision, AI applications
- **Orange Pi**, **Odroid**: Budget alternatives

## Installation & Setup

### Firmware Installation

#### Method 1: Mission Planner (Windows)
1. Download [Mission Planner](https://ardupilot.org/planner/)
2. Connect flight controller via USB
3. Navigate to **Initial Setup** → **Install Firmware**
4. Select vehicle type (Copter most common for quads)
5. Click appropriate firmware (Quad, Hexa, etc.)
6. Wait for flash completion

#### Method 2: QGroundControl (Cross-Platform)
1. Download [QGroundControl](http://qgroundcontrol.com/)
2. Connect flight controller via USB
3. **Vehicle Setup** → **Firmware**
4. Select "ArduPilot" and vehicle type
5. Follow prompts to flash

#### Method 3: Command Line (Advanced)
```bash
# Install pymavlink tools
pip install pymavlink

# Download firmware for your board
wget https://firmware.ardupilot.org/Copter/latest/[board-name]/

# Flash firmware
python -m pymavlink.mavflash --board [board-name] ardupilot.bin
```

### Ground Station Software

#### Mission Planner (Windows)
**Best For**: Complete configuration, advanced features
- Full parameter access
- Mission planning with terrain awareness
- Log analysis tools
- Simulators (SITL)

#### QGroundControl (Windows, Mac, Linux, Mobile)
**Best For**: Cross-platform, clean interface
- Simplified interface vs Mission Planner
- Excellent mobile support
- Good for field operations
- Basic mission planning

#### MAVProxy (Command Line)
**Best For**: Scripting, advanced users, Linux
- Python-based, extensible
- Powerful for automation
- Lightweight, runs on companion computers

## Initial Configuration

### Mandatory Hardware Setup

#### 1. Frame Type Selection
**Mission Planner**: Setup → Mandatory Hardware → Frame Type
- **Quad X**: Most common educational platform
- **Quad H**: H-frame configuration
- **Hexa X**, **Octo X**: Six/eight motor configurations

#### 2. Accelerometer Calibration
**Critical for stable flight**

1. **Setup** → **Mandatory Hardware** → **Accel Calibration**
2. Place vehicle level, press button
3. Follow prompts: level, left, right, nose down, nose up, back
4. Keep vehicle still during each position
5. Complete all six orientations

**Tips**:
- Use stable surface (not hand-held)
- Ensure battery connected (loaded weight)
- Repeat if initial flight shows drift

#### 3. Compass Calibration
**Essential for GPS navigation**

1. **Setup** → **Mandatory Hardware** → **Compass**
2. Enable compass(es), set orientation
3. Click "Start" for calibration dance
4. Rotate vehicle slowly in all orientations
5. Progress bars show coverage, aim for green
6. Complete when prompted

**Common Issues**:
- Magnetic interference: Move away from metal, wires
- Motor magnets: Calibrate with battery connected, props OFF
- Multiple compasses: External GPS compass usually more accurate

#### 4. Radio Calibration
**Map transmitter to flight controller**

1. **Setup** → **Mandatory Hardware** → **Radio Calibration**
2. Turn on transmitter, receiver bound
3. Click "Calibrate Radio"
4. Move all sticks and switches to extremes
5. Click "Done" when ranges shown

**Verify**:
- All channels respond correctly
- Minimum/maximum values are ~1000/2000 μs
- Center values near 1500 μs

#### 5. Flight Modes Setup
**Configure switch positions**

1. **Setup** → **Mandatory Hardware** → **Flight Modes**
2. Select mode for each switch position (6 positions typical)

**Recommended Educational Configuration**:
- **Position 1**: Stabilize (manual, self-leveling)
- **Position 2**: Alt Hold (holds altitude, manual horizontal)
- **Position 3**: Loiter (holds position with GPS)
- **Position 4**: RTL (Return to Launch - emergency)
- **Position 5**: Auto (autonomous mission)
- **Position 6**: Guided (for DroneKit/MAVLink control)

#### 6. ESC Calibration
**Set throttle range for ESCs**

**Method 1: Automatic (Preferred)**
1. **Setup** → **Optional Hardware** → **ESC Calibration**
2. Follow prompts carefully
3. Props OFF, safety critical

**Method 2: Manual**
1. Disconnect battery
2. Transmitter throttle to maximum
3. Connect battery (ESCs beep)
4. Lower throttle to minimum (ESCs beep confirmation)
5. Complete

### Optional Hardware

#### GPS/Compass Module
1. **Setup** → **Optional Hardware** → **GPS**
2. Set GPS type (Auto-detect or specific model)
3. Set compass orientation if not auto
4. Verify GPS lock (usually requires outdoors)

#### Battery Monitor
1. **Setup** → **Optional Hardware** → **Battery Monitor**
2. Enter battery capacity (mAh)
3. Calibrate voltage sensor (multimeter recommended)
4. Set failsafe voltage (3.3V per cell)

#### Telemetry Radio
1. Connect to "TELEM1" or "TELEM2" port
2. Set appropriate baudrate (usually 57600)
3. Ground station automatically connects

## Flight Modes Explained

### Manual Modes (No GPS Required)

**Stabilize**
- Manual stick control, FC provides self-leveling
- Release sticks → level flight
- **Best For**: First flights, learning, line-of-sight

**AltHold (Altitude Hold)**
- Stabilize + automatic altitude hold with barometer
- Throttle controls climb/descent rate
- **Best For**: Easier flight training, photo/video

**Acro**
- Manual stick controls rotation rates, no self-leveling
- For advanced pilots and acrobatics
- **Best For**: Advanced manual control training

### GPS-Assisted Modes

**Loiter**
- Holds position and altitude with GPS
- Very stable, easy to fly
- **Best For**: Testing, beginners with GPS

**PosHold**
- Like loiter but uses accelerometers + GPS for tighter hold
- More responsive to stick input
- **Best For**: Precise positioning

### Autonomous Modes

**Auto**
- Follows pre-programmed waypoint mission
- Full autonomous operation
- **Best For**: Survey missions, competitions, demonstrations

**RTL (Return to Launch)**
- Flies back to takeoff point automatically
- Climbs to RTL_ALT, flies home, lands
- **Best For**: Failsafe, low battery return

**Guided**
- Accepts navigation commands from GCS or companion computer
- Used by DroneKit and MAVLink scripts
- **Best For**: Programming, dynamic missions

**Follow Me**
- Follows GPS signal from ground station or mobile device
- Maintains altitude and distance
- **Best For**: Action sports, demonstrations

### Failsafe Mode
Automatically triggered by:
- Low battery voltage
- Radio signal loss
- GPS loss (if in GPS mode)
- GCS heartbeat loss

**Default Action**: Switch to RTL, land if RTL fails

## Mission Planning

### Creating a Mission (Mission Planner)

1. **Flight Plan Tab** → Click on map to add waypoints
2. Right-click waypoint for options:
   - Set altitude (relative or absolute)
   - Add commands (loiter, takeoff, land, camera trigger)
   - Adjust speed
   - Set acceptance radius

3. Common Commands:
   - **Waypoint**: Navigate to position
   - **Loiter_Time**: Circle for specified seconds
   - **Loiter_Turns**: Circle for specified rotations
   - **Do_Set_CAM_Trigg_Dist**: Trigger camera every X meters
   - **Do_Change_Speed**: Adjust flight speed mid-mission
   - **Return_To_Launch**: End mission, fly home

4. **Write Mission** to flight controller
5. Execute by switching to AUTO mode

### Mission Verification
- Use "Preflight Calibration" to verify GPS quality
- Check "Write WPs" succeeded
- Verify home position is correct
- Test RTL before AUTO mode

### Example Educational Missions

**Mission 1: Square Pattern**
```
Waypoint 1: Takeoff to 10m
Waypoint 2: Fly 20m North, 10m altitude
Waypoint 3: Fly 20m East, 10m altitude
Waypoint 4: Fly 20m South, 10m altitude
Waypoint 5: Fly 20m West, 10m altitude
Waypoint 6: Return to Launch
```

**Mission 2: Survey Pattern with Camera**
- Set up parallel flight lines
- Add Do_Set_CAM_Trigg_Dist for camera intervals
- Set appropriate altitude for GSD (ground sample distance)
- Include loiter at start for GPS lock

## Programming with DroneKit (Python)

### Installation
```bash
pip install dronekit
pip install dronekit-sitl  # For simulation
```

### Basic Connection Script
```python
from dronekit import connect, VehicleMode
import time

# Connect to vehicle
connection_string = '/dev/ttyUSB0'  # or 'COM3' on Windows, 'udp:127.0.0.1:14550' for SITL
vehicle = connect(connection_string, wait_ready=True, baud=57600)

# Get vehicle state
print(f"Mode: {vehicle.mode.name}")
print(f"Armed: {vehicle.armed}")
print(f"GPS: {vehicle.gps_0}")
print(f"Battery: {vehicle.battery}")
print(f"Location: {vehicle.location.global_frame}")

# Close connection
vehicle.close()
```

### Arming and Takeoff
```python
def arm_and_takeoff(vehicle, target_altitude):
    """
    Arms vehicle and flies to target_altitude (meters)
    """
    print("Pre-arm checks...")
    while not vehicle.is_armable:
        print("Waiting for vehicle to initialize...")
        time.sleep(1)

    print("Arming motors...")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print("Armed!")

    print(f"Taking off to {target_altitude}m")
    vehicle.simple_takeoff(target_altitude)

    # Wait until target altitude reached
    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print(f"Altitude: {altitude:.1f}m")
        if altitude >= target_altitude * 0.95:
            print("Target altitude reached")
            break
        time.sleep(1)

# Usage
arm_and_takeoff(vehicle, 10)
```

### Navigate to Location
```python
from dronekit import LocationGlobalRelative

def goto_position(vehicle, lat, lon, alt):
    """
    Navigate to GPS position (lat, lon, alt in meters)
    """
    target = LocationGlobalRelative(lat, lon, alt)
    vehicle.simple_goto(target)

# Usage: Fly 20 meters North, 10m altitude
# (Latitude increases northward, ~0.0001 degrees ≈ 11 meters)
current_lat = vehicle.location.global_frame.lat
current_lon = vehicle.location.global_frame.lon

goto_position(vehicle, current_lat + 0.00018, current_lon, 10)
```

### Complete Mission Example
```python
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Connect
vehicle = connect('COM3', wait_ready=True, baud=57600)

# Arm and takeoff
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
while not vehicle.armed:
    time.sleep(1)

vehicle.simple_takeoff(10)
time.sleep(15)  # Wait for takeoff

# Fly square pattern (20m sides)
points = [
    (vehicle.location.global_frame.lat + 0.00018, vehicle.location.global_frame.lon, 10),
    (vehicle.location.global_frame.lat + 0.00018, vehicle.location.global_frame.lon + 0.00018, 10),
    (vehicle.location.global_frame.lat, vehicle.location.global_frame.lon + 0.00018, 10),
    (vehicle.location.global_frame.lat, vehicle.location.global_frame.lon, 10)
]

for lat, lon, alt in points:
    vehicle.simple_goto(LocationGlobalRelative(lat, lon, alt))
    time.sleep(20)  # Allow time to reach each point

# Return to launch
vehicle.mode = VehicleMode("RTL")
time.sleep(30)

vehicle.close()
```

**Full Examples**: See [code/flight-controllers/ardupilot-missions/](../../../code/flight-controllers/ardupilot-missions/)

## Parameter Tuning

### Key Parameters for Educational Use

#### Safety Parameters
- **BATT_CAPACITY**: Battery mAh (for accurate remaining estimates)
- **BATT_LOW_VOLT**: Failsafe trigger voltage (11.1V for 3S, 14.8V for 4S)
- **FS_BATT_ENABLE**: Enable battery failsafe (set to 2 for RTL)
- **FS_THR_ENABLE**: Enable radio failsafe (set to 1 for RTL)
- **FENCE_ENABLE**: Enable geofence (highly recommended for education)

#### Flight Performance
- **MOT_THST_HOVER**: Throttle % for hover (auto-learned, typically 0.3-0.5)
- **PSC_VELXY_P**: Horizontal velocity control (increase for more aggressive)
- **PSC_ACCZ_P/I**: Altitude hold tuning

#### GPS/Navigation
- **WPNAV_SPEED**: Autonomous waypoint speed (cm/s, default 1000 = 10m/s)
- **WPNAV_RADIUS**: Waypoint acceptance radius (cm, default 200 = 2m)
- **RTL_ALT**: Return-to-launch altitude (cm, default 1500 = 15m)

### Autotune
ArduPilot can automatically tune PID values:

1. Ensure vehicle flies well in AltHold
2. Switch to **Autotune** mode (set up in flight modes)
3. Vehicle will perform automated maneuvers
4. Takes 15-20 minutes for full tune
5. Land to save, or disarm to discard

**Best For**: Advanced builds, after manual tune is close

## Logging & Analysis

### Enabling Logs
Logs are automatically recorded to SD card on Pixhawk.

**Parameter**: Set LOG_BACKEND_TYPE for storage location

### Downloading Logs
**Mission Planner**: Setup → Optional Hardware → Dataflash Logs → Download

### Analyzing Logs
**Mission Planner Log Viewer**:
1. Load .bin or .log file
2. Graph any parameter vs time
3. Look for errors/warnings in message log

**Common Analysis**:
- **Vibration levels**: Graph IMU accelerometers, should be <30 m/s²
- **GPS performance**: Graph GPS satellites, HDOP
- **Battery voltage**: Check for voltage sag during high throttle
- **Desired vs actual**: Compare desired altitude/position to actual

## Troubleshooting

### Pre-Arm Checks Failed

**"Pre-Arm: Check FS_THR_VALUE"**
- Throttle not at minimum during arm attempt
- Solution: Lower throttle stick fully

**"Pre-Arm: RC not calibrated"**
- Radio calibration incomplete
- Solution: Re-run radio calibration

**"Pre-Arm: Compass not calibrated"**
- Compass needs calibration
- Solution: Run compass calibration outdoors, away from metal

**"Pre-Arm: High GPS HDOP"**
- Poor GPS accuracy
- Solution: Wait for better GPS lock, move to open area

### Flight Issues

**Vehicle drifts in Loiter**
- Compass calibration off or magnetic interference
- Solution: Re-calibrate compass, check for interference sources

**Oscillations/Wobbles**
- PID tuning needed
- Solution: Reduce PSC values incrementally, or run Autotune

**Poor altitude hold**
- Barometer drift or vibrations
- Solution: Check vibration levels, ensure barometer is not in prop wash

## Educational Activities

### Lab Projects

1. **Mission Comparison**: Fly same mission with different WPNAV_SPEED, compare times and battery use
2. **Failsafe Testing**: Test battery and radio failsafes in controlled environment
3. **Log Analysis**: Analyze logs to determine actual hover throttle, vibration levels
4. **DroneKit Programming**: Write Python scripts for custom missions
5. **Sensor Integration**: Add additional I2C/UART sensors, log data

### Competitions
- **AUVSI SUAS**: College-level autonomous competition
- **DroneBlocks**: Visual programming challenges
- **Custom School Challenges**: Autonomous pickup/delivery, search patterns

## Safety & Best Practices

### Pre-Flight Checklist
- [ ] Compass calibrated in flying area (different locations have different magnetic fields)
- [ ] GPS lock with 10+ satellites
- [ ] Pre-arm checks all passed
- [ ] Failsafes configured and tested
- [ ] Mission verified in QGroundControl or Mission Planner
- [ ] Backup pilot ready with transmitter
- [ ] Geofence enabled for area

### During Flight
- Always have manual override ready (switch to Stabilize mode)
- Monitor battery voltage
- Be prepared for GPS loss (mode will switch automatically)

### After Flight
- Download and review logs
- Note any issues for next flight
- Check battery for damage/puffing

## Resources

### Official Documentation
- [ArduPilot.org](https://ardupilot.org/) - Official docs
- [ArduPilot Discourse](https://discuss.ardupilot.org/) - Community forum
- [ArduPilot Discord](https://ardupilot.org/discord) - Real-time chat

### Ground Station Software Downloads
- [Mission Planner](https://ardupilot.org/planner/docs/mission-planner-installation.html)
- [QGroundControl](http://qgroundcontrol.com/)
- [MAVProxy](https://ardupilot.org/mavproxy/)

### Learning Resources
- [ArduPilot YouTube Channel](https://www.youtube.com/c/ardupilot)
- [Painless360 YouTube](https://www.youtube.com/c/Painless360) - Excellent setup tutorials
- [DroneKit Documentation](https://dronekit-python.readthedocs.io/)

### Code Examples
- [ArduPilot MAVLink Scripts](../../../code/flight-controllers/ardupilot-missions/)
- [DroneKit Example Missions](../../../code/flight-controllers/dronekit-examples/)

---

**Next**: [Betaflight →](betaflight.md) | [Back to Flight Controllers →](../index.md)
