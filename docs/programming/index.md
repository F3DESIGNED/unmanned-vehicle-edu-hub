# Programming Guide

Comprehensive programming resources for unmanned vehicle systems, from Arduino basics to advanced ROS development.

## Quick Navigation

### By Platform
- **[Arduino Programming →](arduino-programming/)**: C/C++ for microcontrollers
- **[Raspberry Pi Programming →](raspberry-pi-programming/)**: Python for Linux-based systems
- **[Flight Controller Programming →](flight-controller-programming/)**: MAVLink, DroneKit, Betaflight

### By Skill Level
- **Beginners**: Start with [Arduino Basics](arduino-programming/motor-control.md)
- **Intermediate**: Progress to [Raspberry Pi Python](raspberry-pi-programming/python-robotics.md)
- **Advanced**: Explore [ROS2](raspberry-pi-programming/ros2-integration.md) and [DroneKit](flight-controller-programming/ardupilot-mavlink.md)

## Programming Pathways

### Path 1: Ground Vehicles (Arduino)
1. [Motor Control](arduino-programming/motor-control.md) - Drive motors, H-bridges
2. [Sensor Integration](arduino-programming/sensor-integration.md) - Ultrasonic, IR, GPS
3. [Communication](arduino-programming/communication-protocols.md) - Serial, I2C, SPI
4. **Projects**: Obstacle avoidance rover, line follower

### Path 2: Aerial Vehicles (Flight Controllers)
1. [ArduPilot Configuration](flight-controller-programming/ardupilot-mavlink.md) - Parameter setup
2. [DroneKit Python](flight-controller-programming/ardupilot-mavlink.md#dronekit) - Autonomous missions
3. [MAVLink Protocol](flight-controller-programming/ardupilot-mavlink.md#mavlink) - Custom commands
4. **Projects**: GPS waypoint missions, precision landing

### Path 3: Computer Vision & AI (Raspberry Pi)
1. [Python Robotics Basics](raspberry-pi-programming/python-robotics.md) - GPIO, motors, sensors
2. [OpenCV Integration](raspberry-pi-programming/python-robotics.md#opencv) - Object detection
3. [ROS2 Fundamentals](raspberry-pi-programming/ros2-integration.md) - Nodes, topics, services
4. **Projects**: Object tracking, SLAM mapping, autonomous navigation

## Core Concepts

### Control Theory

**PID Control**: Fundamental algorithm for maintaining desired state
- **P (Proportional)**: Immediate correction based on error
- **I (Integral)**: Corrects persistent errors over time
- **D (Derivative)**: Dampens oscillations, predicts future error

**Applications**: Altitude hold, position control, line following, motor speed regulation

**Learn More**: [Control Fundamentals](fundamentals.md#pid-control)

### State Machines

**Purpose**: Organize complex behaviors into discrete states

**Example States** (Autonomous Rover):
- IDLE → NAVIGATE → AVOID_OBSTACLE → NAVIGATE → ARRIVED

**Benefits**: Predictable behavior, easier debugging, modular code

**Learn More**: [State Machines Guide](fundamentals.md#state-machines)

### Communication Protocols

| Protocol | Speed | Distance | Wiring | Best For |
|----------|-------|----------|--------|----------|
| **I2C** | Moderate | Short (< 1m) | 2 wires | Sensors (GPS, IMU, displays) |
| **SPI** | Fast | Short (< 1m) | 4+ wires | High-speed sensors, SD cards |
| **UART/Serial** | Moderate | Medium (~10m) | 2 wires | GPS, telemetry, ESCs |
| **PWM** | Slow | Short | 1 wire/signal | Servos, ESCs (legacy) |
| **CAN** | Fast | Long (~40m) | 2 wires | Vehicle networks, redundancy |
| **MAVLink** | N/A | Varies | Over Serial/UDP | Drone telemetry, commands |

**Learn More**: [Communication Protocols](arduino-programming/communication-protocols.md)

## Code Repository Structure

```
code/
├── arduino/
│   ├── basic-rover/           # Complete obstacle avoidance project
│   ├── line-follower/          # PID line following
│   └── sensor-examples/        # Individual sensor demos
├── raspberry-pi/
│   ├── python-examples/
│   │   ├── gpio-motor-control/
│   │   ├── opencv-object-detection/
│   │   └── autonomous-navigation/
│   └── ros2-examples/
├── flight-controllers/
│   ├── ardupilot-missions/    # Example waypoint missions
│   ├── dronekit-scripts/      # Python DroneKit examples
│   └── betaflight-configs/    # Config dumps for reference
└── utilities/
    ├── parameter-converter.py
    └── log-analyzer.py
```

## Getting Started

### Arduino Development
1. Install [Arduino IDE](https://www.arduino.cc/en/software) or [PlatformIO](https://platformio.org/)
2. Connect Arduino via USB
3. Select board and port
4. Upload example sketch: [Basic Motor Control](arduino-programming/motor-control.md)

### Raspberry Pi Development
1. Install [Raspberry Pi OS](https://www.raspberrypi.org/software/)
2. SSH or VNC into Pi
3. Install Python libraries: `pip install RPi.GPIO opencv-python`
4. Run example: [GPIO Motor Control](raspberry-pi-programming/python-robotics.md)

### Flight Controller Programming
1. Install [Mission Planner](https://ardupilot.org/planner/) or [QGroundControl](http://qgroundcontrol.com/)
2. Connect flight controller via USB or telemetry
3. Install [DroneKit](https://dronekit-python.readthedocs.io/): `pip install dronekit`
4. Run example: [Simple Takeoff Script](flight-controller-programming/ardupilot-mavlink.md#basic-example)

## Best Practices

### Code Organization
- **Modularity**: Break code into functions
- **Comments**: Explain why, not just what
- **Constants**: Define pin numbers, thresholds at top
- **Error Handling**: Check sensor readings, handle failures gracefully

### Version Control
- Use Git for all projects
- Commit frequently with clear messages
- Tag working versions before major changes

### Testing
- **Unit Tests**: Test individual functions
- **Integration Tests**: Test full system
- **Field Tests**: Real-world validation

### Safety
- **Software Kill Switch**: Emergency stop in code
- **Watchdog Timer**: Restart if code hangs
- **Bounds Checking**: Limit motor speeds, angles
- **Failsafes**: Default safe behavior if sensors fail

## Educational Activities

### Beginner Projects
1. **Blink LED**: Arduino basics
2. **Read Sensor**: Display ultrasonic distance
3. **Motor Control**: Drive single motor forward/reverse
4. **Simple Rover**: Two motors, forward/backward/turn

### Intermediate Projects
5. **Obstacle Avoidance**: Ultrasonic sensor + autonomous navigation
6. **Line Follower**: IR sensors + PID control
7. **GPS Waypoint**: Navigate to GPS coordinates
8. **FPV Control**: Wireless video + manual control

### Advanced Projects
9. **Computer Vision**: OpenCV object detection and tracking
10. **SLAM Mapping**: ROS2 + LiDAR, create 2D/3D maps
11. **Swarm Coordination**: Multiple robots, shared goal
12. **Machine Learning**: Trained model for autonomous decisions

## Competitions

### Ground Vehicle
- **Sparkfun AVC**: Autonomous vehicle challenge (GPS navigation)
- **FIRST Robotics**: High school robotics competition
- **RoboSub**: Underwater autonomous vehicle

### Aerial Vehicle
- **AUVSI SUAS**: College-level autonomous aerial systems
- **DRL (Drone Racing League)**: FPV racing competitions
- **International Aerial Robotics Competition (IARC)**: Advanced autonomous challenges

## Resources

### Learning Platforms
- **Arduino Project Hub**: Tutorials and examples
- **Raspberry Pi Projects**: Official project ideas
- **ROS Tutorials**: Official ROS/ROS2 learning path
- **YouTube**: Joshua Bardwell (drones), Paul McWhorter (Arduino/Pi)

### Documentation
- [Arduino Language Reference](https://www.arduino.cc/reference/en/)
- [Python Official Docs](https://docs.python.org/3/)
- [ArduPilot Developer Docs](https://ardupilot.org/dev/)
- [ROS2 Documentation](https://docs.ros.org/)

### Code Examples
- [Arduino Examples →](../../code/arduino/)
- [Python Examples →](../../code/raspberry-pi/)
- [Flight Controller Scripts →](../../code/flight-controllers/)

---

**Start Learning**: [Arduino Programming →](arduino-programming/) | [Raspberry Pi Programming →](raspberry-pi-programming/) | [Flight Controllers →](flight-controller-programming/)
