---
title: Introduction to Unmanned Systems
description: Comprehensive introduction to unmanned vehicle systems, types, components, and applications
---

# Introduction to Unmanned Systems

## What Are Unmanned Vehicles?

**Unmanned vehicles** are mobile platforms that operate without a human occupant on board. They can be remotely controlled, semi-autonomous, or fully autonomous, and operate in air, on land, or in water.

### Key Characteristics

- **No onboard pilot/driver/captain**
- **Remote or autonomous operation**
- **Sensors for perception and navigation**
- **Communication systems for control/telemetry**
- **Onboard processing for decision-making**

## The Three Domains

### 🚁 Aerial - UAVs/Drones (Unmanned Aerial Vehicles)

**Description:** Aircraft that fly without a human pilot aboard

**Common Types:**

- **Multirotors** (quadcopters, hexacopters, octocopters)
- **Fixed-wing** (airplane-style)
- **Hybrid VTOL** (vertical takeoff, forward flight)
- **Helicopters** (single main rotor)

**Typical Applications:**

- Aerial photography and videography
- Mapping and surveying
- Package delivery
- Search and rescue
- Agricultural monitoring
- Infrastructure inspection
- Racing and recreation

**Example Platforms:**

- DJI Mavic series (consumer)
- DJI Phantom series (prosumer)
- Custom racing quadcopters
- Military drones (Predator, Global Hawk)

---

### 🚗 Ground - UGVs/Rovers (Unmanned Ground Vehicles)

**Description:** Vehicles that travel on land without a human driver

**Common Types:**

- **Wheeled rovers** (2WD, 4WD, 6WD)
- **Tracked vehicles** (tank-style treads)
- **Legged robots** (bipedal, quadrupedal)
- **Hybrid systems** (wheels + legs)

**Typical Applications:**

- Warehouse automation
- Planetary exploration (Mars rovers)
- Military reconnaissance
- Hazardous material handling
- Educational robotics competitions
- Agricultural automation
- Mining operations

**Example Platforms:**

- Mars Curiosity/Perseverance rovers
- Clearpath Robotics platforms
- Custom Arduino/Raspberry Pi rovers
- Boston Dynamics Spot (legged)

---

### 🚤 Marine - USVs/AUVs (Unmanned Surface/Underwater Vehicles)

**Description:** Watercraft that operate on or under water without crew

**Common Types:**

- **Surface vessels** (USVs - float on water)
- **Underwater vehicles** (AUVs/ROVs - operate submerged)
- **Hybrid systems** (can transition between modes)

**Typical Applications:**

- Oceanographic research
- Environmental monitoring
- Underwater inspection (bridges, dams, pipelines)
- Mine detection and clearance
- Search and recovery
- Coastal surveillance
- Educational STEM projects

**Example Platforms:**

- Modified RC boats (educational)
- BlueROV2 (underwater inspection)
- Wave Glider (ocean research)
- Commercial autonomous cargo vessels

## Core Components

All unmanned vehicles share common subsystems:

### 1. **Power System**
- Batteries (LiPo, Li-ion, Lead-acid)
- Power distribution (voltage regulators, ESCs)
- Charging systems
- Battery monitoring

### 2. **Propulsion**
- Motors (brushed vs. brushless)
- Propellers/wheels/thrusters
- Electronic Speed Controllers (ESCs)
- Gearboxes and transmissions

### 3. **Control System**
- Flight controller / autopilot (Pixhawk, ArduPilot)
- Microcontrollers (Arduino, Raspberry Pi)
- Sensors (IMU, GPS, compass)
- Control algorithms (PID loops, state machines)

### 4. **Communication**
- Radio control transmitter/receiver
- Telemetry links (MAVLink, etc.)
- Video transmission (FPV systems)
- Ground control station software

### 5. **Payload**
- Cameras (photo, video, thermal)
- Sensors (LiDAR, ultrasonic, multispectral)
- Manipulators (grippers, arms)
- Scientific instruments

### 6. **Structure/Airframe**
- Frame materials (carbon fiber, plastic, aluminum)
- Mounting systems
- Protective features
- Aerodynamic/hydrodynamic design

## Levels of Autonomy

Unmanned vehicles operate at different autonomy levels:

| Level | Name | Description | Human Role | Example |
|-------|------|-------------|------------|---------|
| **0** | Manual Control | Human controls all functions in real-time | Direct control of all movements | RC car with no automation |
| **1** | Assisted Control | Vehicle helps stabilize but human commands movements | Commands direction, vehicle maintains stability | Self-leveling drone |
| **2** | Partial Autonomy | Vehicle controls some functions automatically | High-level commands (go there, follow me) | GPS waypoint following |
| **3** | Conditional Autonomy | Vehicle navigates autonomously in defined scenarios | Supervision, intervention if needed | Warehouse robot on known paths |
| **4** | High Autonomy | Vehicle handles most situations autonomously | Mission planning only | Mars rover (high latency forces autonomy) |
| **5** | Full Autonomy | Complete autonomous operation | None during operation | Fully autonomous delivery drone |

**Note:** Most educational and hobbyist platforms operate at Levels 1-3.

## Real-World Applications

### Commercial
- **Amazon Prime Air:** Package delivery drones
- **Zipline:** Medical supply delivery in remote areas
- **John Deere:** Autonomous tractors for farming
- **Kiva/Amazon Robotics:** Warehouse automation

### Research & Exploration
- **NASA Mars Rovers:** Planetary exploration
- **NOAA USVs:** Ocean mapping and monitoring
- **University research:** Algorithm development and testing

### Public Safety
- **Police/Fire departments:** Search and rescue, surveillance
- **Lifeguard drones:** Water rescue equipment delivery
- **Disaster response:** Damage assessment after natural disasters

### Education
- **STEM programs:** Hands-on engineering learning
- **Robotics competitions:** FIRST Robotics, RoboCup
- **University courses:** Controls, AI, computer vision

## Why Study Unmanned Systems?

### Career Opportunities

The unmanned systems industry is **rapidly growing** with diverse opportunities:

- **Aerospace Engineer:** Design next-generation UAVs
- **Robotics Engineer:** Develop autonomous navigation
- **Software Engineer:** Create control and AI systems
- **Computer Vision Specialist:** Perception and object detection
- **Systems Integrator:** Combine hardware and software
- **Field Technician:** Operations and maintenance
- **Regulatory Specialist:** Compliance and certification
- **Entrepreneur:** Start unmanned systems company

**Industry Growth:** The global drone market alone is projected to exceed $50 billion by 2030.

### Educational Benefits

- **Interdisciplinary learning:** Combines mechanical, electrical, and software engineering
- **Problem-solving skills:** Real-world engineering challenges
- **Hands-on experience:** Physical systems you can see and touch
- **Rapid feedback:** See results of your code immediately
- **Scalable complexity:** From simple RC control to advanced AI
- **Team collaboration:** Most projects require diverse skills

### Accessible Entry Points

Unlike many advanced technologies, unmanned systems have:

- **Low-cost entry:** Start with $75-200 platforms
- **Open-source ecosystem:** Free software (ArduPilot, PX4, ROS)
- **Active communities:** Forums, Discord, Reddit support
- **Abundant tutorials:** YouTube, documentation, courses
- **Physical feedback:** Debugging by observing behavior

## Key Terms to Know

Before diving deeper, familiarize yourself with these essential terms. See the [Glossary](../glossary/index.md) for complete definitions.

- **UAV/UAS:** Unmanned Aerial Vehicle/System
- **UGV:** Unmanned Ground Vehicle
- **USV/AUV:** Unmanned Surface/Underwater Vehicle
- **FPV:** First-Person View (camera-based piloting)
- **LOS:** Line of Sight (visual piloting)
- **RTF/BNF/ARF:** Ready-to-Fly, Bind-and-Fly, Almost-Ready-to-Fly
- **ESC:** Electronic Speed Controller
- **LiPo:** Lithium Polymer battery
- **IMU:** Inertial Measurement Unit (accelerometer + gyroscope)
- **GPS:** Global Positioning System
- **MAVLink:** Micro Air Vehicle Link (communication protocol)
- **PID:** Proportional-Integral-Derivative (control algorithm)
- **PWM:** Pulse Width Modulation (motor control signal)

## Safety and Responsibility

!!! warning "Critical Safety Mindset"

    With the excitement of unmanned systems comes **serious responsibility:**

    - **Safety first:** Vehicles can cause injury or property damage
    - **Legal compliance:** Aviation and local regulations apply
    - **Ethical use:** Privacy and security concerns are real
    - **Environmental impact:** Be mindful of wildlife and ecosystems
    - **Continuous learning:** Technology and regulations evolve constantly

**Before proceeding further, thoroughly review all [Safety & Compliance](../safety-compliance/index.md) documentation.**

## The Journey Ahead

You're at the beginning of an exciting learning path. This introduction covered:

- ✅ What unmanned vehicles are and the three domains (aerial, ground, marine)
- ✅ Core components shared across all platforms
- ✅ Levels of autonomy and real-world applications
- ✅ Career opportunities and educational benefits
- ✅ Essential terminology and safety mindset

## Next Steps

Now that you understand the fundamentals:

1. **Review Prerequisites:** Check [Prerequisites](prerequisites.md) for required knowledge and tools
2. **Choose Your Platform:** Use [Platform Selection Guide](selecting-your-platform.md) to find your best fit
3. **Safety First:** Read [Safety & Compliance](../safety-compliance/index.md) documentation thoroughly
4. **Start Building:** Follow [First Build Pathways](first-build-pathways.md) for hands-on experience

**Questions?** Check the [Glossary](../glossary/index.md) or [open an issue](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub/issues).

---

**Last Updated:** November 2025
**Related Topics:** [Prerequisites](prerequisites.md) | [Platform Selection](selecting-your-platform.md) | [Glossary](../glossary/index.md)
