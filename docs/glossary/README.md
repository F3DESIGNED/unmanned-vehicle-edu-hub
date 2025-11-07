# Glossary

Welcome to the Glossary - your reference for terminology used in unmanned vehicle systems.

## Purpose

This section provides clear definitions of terms, acronyms, and concepts used throughout this repository and in the unmanned systems community.

## Organization

Terms are organized by category for easy reference:

```
glossary/
├── README.md (this file)
├── aviation-terms.md         # Flight-related terminology
├── electronics-terms.md      # Hardware and components
├── programming-terms.md      # Software and coding
├── acronyms.md              # Abbreviations and acronyms
└── educational-terms.md      # Pedagogical terminology
```

## Quick Reference - Common Acronyms

### Flight Systems
- **UAV** - Unmanned Aerial Vehicle
- **UGV** - Unmanned Ground Vehicle
- **UAS** - Unmanned Aircraft System
- **RPAS** - Remotely Piloted Aircraft System
- **FPV** - First Person View
- **VLOS** - Visual Line of Sight
- **BVLOS** - Beyond Visual Line of Sight

### Flight Controllers & Software
- **ArduPilot** - Open-source autopilot software
- **PX4** - Professional autopilot platform
- **FC** - Flight Controller
- **GCS** - Ground Control Station
- **ESC** - Electronic Speed Controller
- **IMU** - Inertial Measurement Unit
- **GPS** - Global Positioning System
- **RTL** - Return to Launch

### Communication Protocols
- **MAVLink** - Micro Air Vehicle Link
- **MSP** - MultiWii Serial Protocol
- **SBUS** - Serial Bus (Futaba protocol)
- **PPM** - Pulse Position Modulation
- **PWM** - Pulse Width Modulation
- **UART** - Universal Asynchronous Receiver-Transmitter
- **I2C** - Inter-Integrated Circuit
- **SPI** - Serial Peripheral Interface

### Control & Tuning
- **PID** - Proportional, Integral, Derivative (controller)
- **AHRS** - Attitude and Heading Reference System
- **EKF** - Extended Kalman Filter
- **CG** - Center of Gravity
- **AUW** - All-Up Weight

### Regulations
- **FAA** - Federal Aviation Administration (US)
- **Part 107** - FAA regulation for commercial drone operations
- **44809** - Recreational exception for model aircraft
- **LAANC** - Low Altitude Authorization and Notification Capability
- **AGL** - Above Ground Level
- **MSL** - Mean Sea Level

## Quick Reference - Common Terms

### Aircraft Types
- **Multirotor** - Aircraft with multiple propellers (quadcopter, hexacopter)
- **Quadcopter** - Four-propeller multirotor (most common)
- **Fixed-wing** - Airplane-style aircraft
- **VTOL** - Vertical Take-Off and Landing
- **Rover** - Ground vehicle
- **RTF** - Ready-To-Fly (pre-assembled)
- **BNF** - Bind-and-Fly (requires transmitter binding)
- **ARF** - Almost-Ready-to-Fly (requires some assembly)

### Flight Modes
- **Stabilize** - Manual control with self-leveling
- **Alt Hold** - Altitude Hold (maintains height)
- **Loiter** - Position Hold (GPS required)
- **Auto** - Autonomous waypoint mission
- **RTL** - Return to Launch (autonomous return home)
- **Acro** - Acrobatic mode (no stabilization)
- **Guided** - Computer control via GCS

### Components
- **Airframe** - The physical structure
- **Propeller** - Rotating blade creating thrust
- **Motor** - Electric motor spinning propeller
- **Battery** - Power source (usually LiPo)
- **Receiver** - Receives radio signals from transmitter
- **Telemetry** - Wireless data link to ground station
- **FPV Camera** - First-person-view camera

## Content Status

📅 **Expected Completion**: Q2 2025

### Coming Soon

- [ ] Complete aviation terminology list
- [ ] Electronics and hardware terms
- [ ] Programming and software terms
- [ ] Comprehensive acronym list
- [ ] Educational terminology
- [ ] Visual diagrams for concepts
- [ ] Cross-referenced definitions

## How to Use This Glossary

### Finding Terms

1. **Browse by category** - Use the category files
2. **Search the repository** - Use GitHub search (press `/`)
3. **Check the index** - Alphabetical listing (coming soon)

### Contributing

Found a missing term? See [Contributing Guidelines](../../CONTRIBUTING.md) to add it!

### Term Conventions

- **Bold** - The term being defined
- *Italic* - Related terms with separate definitions
- `Code format` - Commands, parameters, variables

## Sample Definitions

### Autonomous

**Autonomous** - Operating without direct human control. In unmanned systems, autonomous flight means the vehicle follows a pre-programmed mission using sensors (GPS, cameras, etc.) to navigate. Contrast with *manual* control where a pilot directly controls the vehicle in real-time.

*See also: Auto mode, Waypoint, Mission Planning*

### Center of Gravity (CG)

**Center of Gravity (CG)** - The point where the weight of an aircraft is balanced. Proper CG location is critical for stable flight. Too far forward causes nose-heavy flight; too far back causes instability.

*See also: Balance Point, AUW, Trim*

### LiPo Battery

**LiPo Battery** - Lithium Polymer battery, the most common power source for UAVs. Offers high energy density but requires careful handling to prevent fire hazard. Specified by voltage (1S = 3.7V per cell) and capacity (mAh).

*See also: Battery, C-Rating, Cell Count*

## Related Resources

- [Getting Started](../getting-started/) - Fundamentals for beginners
- [References](../references/) - Technical specifications
- All documentation sections use these terms

## Educational Use

This glossary is designed for:
- Students learning unmanned systems
- Educators preparing lessons
- Technical staff setting up systems
- Anyone new to the field

Terms are explained in plain language with minimal jargon. When technical terms are necessary, they're cross-referenced.

---

**Can't find a term?**
- Search the repository
- Ask in [Discussions](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub/discussions)
- Suggest an addition via [Issue](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub/issues)

[Back to Documentation Hub](../index.md)
