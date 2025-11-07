# References

Welcome to the References section, your technical library for unmanned vehicle systems.

## Purpose

This section provides technical specifications, datasheets, protocol documentation, pinout diagrams, and curated external resources for in-depth technical information.

## What You'll Find Here

- **Component Datasheets** - Detailed specifications for hardware
- **Protocol Specifications** - MAVLink, MSP, SBUS, etc.
- **Pinout Diagrams** - Connection references
- **Technical Standards** - Industry specifications
- **External Resources** - Curated links to quality content
- **Research Papers** - Academic publications
- **Books & Publications** - Recommended reading

## Content Organization

```
references/
├── README.md (this file)
├── datasheets/              # Component specifications
├── protocols/               # Communication protocol docs
├── pinouts/                 # Connection diagrams
├── standards/               # Industry standards
├── external-resources/      # Curated web resources
└── publications/            # Books and papers
```

## Key Protocol Documentation

### MAVLink
- **What**: Micro Air Vehicle Link protocol
- **Used By**: ArduPilot, PX4, most autopilots
- **Documentation**: [mavlink.io](https://mavlink.io)
- **Version**: MAVLink 2.0 (current)

### MSP (MultiWii Serial Protocol)
- **What**: Betaflight/INAV communication protocol
- **Used By**: Betaflight, INAV, Cleanflight
- **Documentation**: [Betaflight Wiki](https://github.com/betaflight/betaflight/wiki)

### SBUS / PPM / IBUS
- **What**: Radio receiver protocols
- **SBUS**: Futaba digital protocol (16 channels)
- **PPM**: Pulse Position Modulation (analog)
- **IBUS**: FlySky digital protocol

### UART / I2C / SPI
- **What**: Hardware communication interfaces
- **UART**: Serial communication (GPS, telemetry)
- **I2C**: Multi-device bus (sensors)
- **SPI**: High-speed serial (SD cards, displays)

## Common Component References

### Flight Controllers

| Controller | Processor | Specs | Documentation |
|-----------|-----------|-------|---------------|
| Pixhawk 4 | STM32F7 | [Link] | [ArduPilot Docs] |
| Cube Orange | STM32H7 | [Link] | [CubePilot Docs] |
| Kakute H7 | STM32H7 | [Link] | [Holybro Docs] |

### Sensors

- **IMU** - Inertial Measurement Unit (gyro + accelerometer)
- **Compass** - Magnetometer for heading
- **Barometer** - Altitude measurement
- **GPS** - Position and velocity
- **Optical Flow** - Visual positioning
- **LIDAR** - Distance/altitude measurement

### Communication

- **Telemetry Radios** - 433MHz, 915MHz
- **RC Receivers** - SBUS, PPM, IBUS
- **WiFi Modules** - ESP8266, ESP32
- **4G/LTE** - Long-range communication

## Pinout References

### Common Flight Controller Connections

```
UART1 → GPS
UART2 → Telemetry Radio
UART3 → Available
UART4 → Available
I2C   → Compass, Sensors
SPI   → SD Card
PWM   → Motors (via ESCs)
```

### Arduino Pin Functions

```
Digital Pins → GPIO, PWM (3, 5, 6, 9, 10, 11)
Analog Pins  → Sensor reading (A0-A5)
TX/RX        → Serial communication
SDA/SCL      → I2C bus
```

## Content Status

📅 **Expected Completion**: Q2-Q3 2025

### Coming Soon

- [ ] MAVLink protocol overview
- [ ] Common flight controller pinouts
- [ ] Component datasheet library
- [ ] Curated external resource list
- [ ] Protocol comparison guide
- [ ] Arduino/Raspberry Pi pinouts
- [ ] Sensor specifications
- [ ] Recommended books and courses

## External Resource Categories

### Official Documentation
- ArduPilot Documentation
- PX4 User Guide
- Betaflight Wiki
- Arduino Reference
- Raspberry Pi Documentation

### Learning Platforms
- Udemy courses
- YouTube channels
- Online tutorials
- Academic courses

### Community Forums
- ArduPilot Forum
- RC Groups
- DIY Drones
- Reddit communities

### Tools & Software
- Mission Planner
- QGroundControl
- Betaflight Configurator
- Arduino IDE
- PlatformIO

## Recommended Reading

### Beginner Level
- "Make: Drones" by David McGriffy
- "Arduino Project Handbook"
- Official ArduPilot documentation

### Intermediate Level
- "Small Unmanned Aircraft" by Beard & McLain
- "Programming Drones with Python"
- PX4 Development Guide

### Advanced Level
- "Principles of Robot Motion" by Choset et al.
- Academic papers on control systems
- Firmware source code documentation

## Academic Research

Topics of interest:
- Autonomous navigation algorithms
- Computer vision for UAVs
- Swarm robotics
- Control theory
- Safety systems
- Regulatory studies

## Technical Standards

- **ASTM** - Drone standards
- **IEEE** - Communication standards
- **ISO** - Quality standards
- **FAA AC** - Advisory circulars

## Related Resources

- [Programming](../programming/) - Apply protocols in code
- [Setup & Configuration](../setup-configuration/) - Use specs for setup
- [Control Systems](../control-systems/) - Technical details
- [Glossary](../glossary/) - Term definitions

---

[Back to Documentation Hub](../index.md)
