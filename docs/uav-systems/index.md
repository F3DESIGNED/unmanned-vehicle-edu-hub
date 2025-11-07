# UAV Systems Overview

Welcome to the Unmanned Aerial Vehicle (UAV) systems documentation. This section provides comprehensive resources for building, configuring, and operating educational drone platforms.

## Platform Types

### Multirotor Systems
Multi-rotor UAVs are the most common educational platforms due to their stability, ease of control, and vertical takeoff/landing capabilities.

- **Quadcopters**: Four-motor configuration, most stable and beginner-friendly
- **Hexacopters**: Six-motor configuration, increased payload capacity and redundancy
- **Octocopters**: Eight-motor configuration, maximum payload and fault tolerance

### Fixed-Wing Systems
Fixed-wing platforms offer longer flight times and higher speeds, ideal for survey missions and advanced aerodynamics education.

- **Trainer Aircraft**: Stable, slow-flying platforms for learning
- **Flying Wings**: Efficient design for FPV and autonomous missions
- **VTOL Hybrid**: Combines multirotor and fixed-wing advantages

### Specialty Configurations
- **Tricopters**: Three motors with servo-tilting mechanism
- **Bicopters**: Two motors with complex servo control
- **Coaxial**: Stacked propellers for compact designs

## Platform Comparison Table

| Platform Type | Skill Level | Flight Time | Payload | Stability | Cost | Best For |
|--------------|-------------|-------------|---------|-----------|------|----------|
| **Micro Quadcopter (<250g)** | Beginner | 5-8 min | Minimal | High | $-$$ | Indoor learning, basic flight training |
| **Educational Quad (250-500g)** | Beginner-Intermediate | 10-15 min | Light camera | High | $$-$$$ | Programming, autonomous flight, competitions |
| **Standard Quad (500g-2kg)** | Intermediate | 15-25 min | Action camera, sensors | High | $$$-$$$$ | Advanced autonomy, payload missions |
| **Fixed-Wing Trainer** | Intermediate | 30-45 min | Light sensors | Medium | $$-$$$ | Aerodynamics, long-range missions |
| **VTOL Hybrid** | Advanced | 40-60 min | Multiple sensors | Medium | $$$$-$$$$$ | Research, complex missions |
| **Racing Quad** | Intermediate-Advanced | 3-5 min | FPV camera | Medium-Low | $$-$$$ | Manual control skills, FPV piloting |

**Cost Legend**: $ (<$100), $$ ($100-$300), $$$ ($300-$600), $$$$ ($600-$1500), $$$$$ (>$1500)

## Key Components Overview

### Essential Systems
1. **Frame & Structure**: [Frame Designs →](frame-designs.md)
2. **Propulsion**: [Propulsion Systems →](propulsion-systems.md)
3. **Flight Controller**: [Flight Controllers →](flight-controllers/)
4. **Power System**: Batteries, BEC, power distribution
5. **Radio System**: Transmitter, receiver, protocols
6. **Payload Systems**: [Payload Integration →](payload-systems.md)

## Build Guides

Choose a build guide that matches your educational goals and skill level:

### Beginner Builds
- **[Micro Quadcopter Build](build-guides/micro-quadcopter-build.md)** (<250g, FAA registration-exempt)
  - Perfect for classroom use
  - Indoor-safe propellers
  - No registration required in US
  - Budget: $80-150

### Intermediate Builds
- **[Educational Quadcopter Build](build-guides/educational-quadcopter-build.md)** (250-500g)
  - Programming-friendly platform
  - Autonomous mission capable
  - Competition-ready
  - Budget: $250-450

### Advanced Builds
- **[Fixed-Wing Trainer Build](build-guides/fixed-wing-trainer-build.md)**
  - Long-range missions
  - Advanced flight dynamics
  - Survey and mapping capable
  - Budget: $300-600

## Flight Controller Options

Select the flight controller firmware that best matches your curriculum:

| Controller | Best For | Programming | Difficulty | Documentation |
|-----------|----------|-------------|------------|---------------|
| **[ArduPilot](flight-controllers/ardupilot.md)** | Autonomous missions, research | Python (DroneKit), MAVLink | Advanced | Excellent |
| **[Betaflight](flight-controllers/betaflight.md)** | Racing, FPV, manual control | CLI, LUA scripts | Intermediate | Good |
| **[INAV](flight-controllers/inav.md)** | GPS navigation, waypoints | CLI, limited scripting | Intermediate | Good |
| **[CleanFlight](flight-controllers/cleanflight.md)** | Educational simplicity | CLI only | Beginner | Good |

## Educational Pathways

### Elementary & Middle School (Grades K-8)
1. Start with [Micro Quadcopter](build-guides/micro-quadcopter-build.md)
2. Focus on manual flight skills and safety
3. Introduction to basic components
4. Supervised outdoor flights in controlled areas

### High School (Grades 9-12)
1. Progress to [Educational Quadcopter](build-guides/educational-quadcopter-build.md)
2. Learn programming with [ArduPilot](flight-controllers/ardupilot.md) or [INAV](flight-controllers/inav.md)
3. Implement autonomous missions
4. Participate in competitions (AUVSI SUAS, other)

### Post-Secondary & Research
1. Advanced platforms with custom modifications
2. ROS/ROS2 integration for complex autonomy
3. Computer vision and AI applications
4. Multi-vehicle coordination

## Safety Considerations

!!! warning "Safety First"
    - Always follow [FAA regulations](../safety-compliance/faa-regulations.md)
    - Complete [safety training](../safety-compliance/safety-procedures.md)
    - Review [battery safety](../safety-compliance/battery-safety.md) before charging
    - Use propeller guards for indoor/classroom use
    - Maintain appropriate insurance coverage

## Getting Started

**New to UAV systems?**
1. Review [Prerequisites](../getting-started/prerequisites.md)
2. Understand [Safety & Compliance](../safety-compliance/)
3. Choose your platform from the comparison table above
4. Follow the appropriate [Build Guide](build-guides/)
5. Complete [Setup & Configuration](../setup-configuration/)
6. Start with [Basic Programming](../programming/)

## Additional Resources

- **Troubleshooting**: [Common UAV Issues →](../troubleshooting/)
- **Programming**: [UAV Programming Guide →](../programming/)
- **Hardware Designs**: [CAD Files & BOMs →](../../hardware/uav-designs/)
- **Code Examples**: [Sample Projects →](../../code/flight-controllers/)

## Community & Support

- Share your builds in [GitHub Discussions](#)
- Report issues or ask questions in [Issues](#)
- Contribute improvements via [Pull Requests](#)

---

**Next Steps**: Choose a [Build Guide →](build-guides/) or explore [Flight Controllers →](flight-controllers/)
