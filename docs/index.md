---
title: Unmanned Vehicle Systems Education Hub
description: Comprehensive educational resource for learning unmanned vehicle systems including drones, rovers, and boats
---

# Welcome to the Unmanned Vehicle Systems Education Hub

## Our Mission

Empowering the next generation of engineers and innovators through hands-on experience with unmanned vehicle systems. This hub provides comprehensive, accessible resources for students, educators, hobbyists, and researchers to explore aerial, ground, and marine autonomous platforms.

## Navigation Map

```mermaid
graph TD
    A[Education Hub] --> B[Getting Started]
    A --> C[Platform Guides]
    A --> D[Safety & Compliance]
    A --> E[Curriculum Resources]

    B --> B1[Introduction to Unmanned Systems]
    B --> B2[Selecting Your Platform]
    B --> B3[Prerequisites]
    B --> B4[First Build Pathways]

    C --> C1[Aerial - Drones/UAVs]
    C --> C2[Ground - Rovers/UGVs]
    C --> C3[Marine - Boats/USVs]
    C --> C4[Hybrid Systems]

    D --> D1[FAA Regulations]
    D --> D2[School Policies]
    D --> D3[Safety Procedures]
    D --> D4[Battery Safety]

    E --> E1[Lesson Plans]
    E --> E2[Student Worksheets]
    E --> E3[Assessment Tools]
    E --> E4[Project Ideas]
```

## Quick Start by User Role

### 👨‍🎓 Students
**"I want to build my first drone/rover/boat"**

1. Start with [Introduction to Unmanned Systems](getting-started/introduction-to-unmanned-systems.md)
2. Review [Safety Procedures](safety-compliance/safety-procedures.md) and [Battery Safety](safety-compliance/battery-safety.md)
3. Choose your path in [First Build Pathways](getting-started/first-build-pathways.md)
4. Explore the [Glossary](glossary/index.md) for terminology

**Recommended Starting Point:** Level 1 - Ready-to-Fly (RTF) platforms

---

### 👨‍🏫 Educators & Teachers
**"I want to integrate unmanned systems into my curriculum"**

1. Review [School Policies](safety-compliance/school-policies.md) and templates
2. Complete [Student Safety Training](safety-compliance/student-safety-training.md) requirements
3. Browse [Curriculum Resources](../resources/lesson-plans/.gitkeep) (coming in Phase 2)
4. Use [Platform Selection Guide](getting-started/selecting-your-platform.md) for budget planning

**Key Resource:** Downloadable safety policy templates for your institution

---

### 🔧 Hobbyists & Makers
**"I want to customize and experiment with autonomous systems"**

1. Check [Prerequisites](getting-started/prerequisites.md) for required skills
2. Jump to [First Build Pathways](getting-started/first-build-pathways.md) - Level 2 or 3
3. Explore platform-specific guides (coming in Phase 2)
4. Join the community through [Contributing](../CONTRIBUTING.md)

**Recommended Starting Point:** Level 2 - Bind-and-Fly (BNF) or Almost-Ready-to-Fly (ARF)

---

### 🔬 Researchers & Advanced Users
**"I need a platform for algorithm development and testing"**

1. Start with [Platform Selection Guide](getting-started/selecting-your-platform.md) for technical comparisons
2. Review Level 4 (Custom Builds) in [First Build Pathways](getting-started/first-build-pathways.md)
3. Access code libraries and examples (coming in Phase 2)
4. Explore integration with research frameworks (PX4, ArduPilot, ROS)

**Recommended Starting Point:** Level 3-4 - ARF or Custom builds with open-source flight controllers

---

## Platform Selection Decision Tree

```mermaid
graph TD
    Start[Choose Your Platform] --> Q1{What environment?}

    Q1 -->|Air| Q2A{Indoor or Outdoor?}
    Q1 -->|Land| Q2B{Terrain Type?}
    Q1 -->|Water| Q2C{Freshwater or Saltwater?}

    Q2A -->|Indoor| A1[Small Quadcopter<br/>Tello, Crazyflie]
    Q2A -->|Outdoor| A2[Medium-Large UAV<br/>DJI, Custom builds]

    Q2B -->|Smooth/Indoor| B1[Wheeled Rover<br/>Low complexity]
    Q2B -->|Rough/Outdoor| B2[Tracked or 6WD<br/>Higher capability]

    Q2C -->|Freshwater| C1[Basic USV<br/>Standard electronics]
    Q2C -->|Saltwater| C2[Marine-Grade USV<br/>Corrosion protection]

    A1 --> Budget[See Budget Matrix]
    A2 --> Budget
    B1 --> Budget
    B2 --> Budget
    C1 --> Budget
    C2 --> Budget
```

## Featured Pathways

### 🚁 **Aerial Systems (UAVs/Drones)**
Perfect for: Photography, surveying, research, racing
- **Beginner:** DJI Tello ($100) - programmable indoor drone
- **Intermediate:** Custom 250mm racing quad ($200-400)
- **Advanced:** Pixhawk-based mapping drone ($600+)

[Explore Aerial Platforms →](platforms/.gitkeep)

### 🚗 **Ground Systems (UGVs/Rovers)**
Perfect for: Robotics education, autonomous navigation, STEM competitions
- **Beginner:** Modified RC car with Arduino ($75-150)
- **Intermediate:** ROS-based rover with sensors ($300-500)
- **Advanced:** Custom outdoor autonomous platform ($800+)

[Explore Ground Platforms →](platforms/.gitkeep)

### 🚤 **Marine Systems (USVs/Boats)**
Perfect for: Environmental monitoring, unique engineering challenges
- **Beginner:** Modified RC boat ($100-200)
- **Intermediate:** Pixhawk marine platform ($400-600)
- **Advanced:** Custom research vessel ($1000+)

[Explore Marine Platforms →](platforms/.gitkeep)

## Safety First! ⚠️

Before starting any build or flight:

!!! danger "Critical Safety Requirements"
    - **ALWAYS** read [Battery Safety](safety-compliance/battery-safety.md) before charging/using LiPo batteries
    - Review [FAA Regulations](safety-compliance/faa-regulations.md) for legal flight requirements
    - Complete [Safety Procedures](safety-compliance/safety-procedures.md) training
    - Use appropriate [Personal Protective Equipment](safety-compliance/safety-procedures.md#ppe)

## Community & Support

- **Questions?** Check our [Glossary](glossary/index.md) for definitions
- **Found an issue?** See our [Contributing Guide](../CONTRIBUTING.md)
- **New to the field?** Start with [Introduction to Unmanned Systems](getting-started/introduction-to-unmanned-systems.md)

## What's Available Now (Phase 1)

✅ Getting Started Documentation
✅ Safety and Compliance Guides
✅ Platform Selection Tools
✅ Comprehensive Glossary
✅ Community Guidelines

## Coming Soon

🔜 **Phase 2:** Platform-specific build guides (Aerial, Ground, Marine)
🔜 **Phase 3:** Curriculum resources and lesson plans
🔜 **Phase 4:** Code examples and libraries
🔜 **Phase 5:** Hardware designs and CAD files

---

**Last Updated:** November 2025
**License:** Documentation under CC-BY-SA 4.0 | Code under MIT License

[View on GitHub](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub) | [Report Issues](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub/issues)
