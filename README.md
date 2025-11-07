# Unmanned Vehicle Systems Education Hub

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](docs/index.md)
[![Community](https://img.shields.io/badge/community-join-brightgreen.svg)](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub/discussions)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **Comprehensive open-source resources for implementing UAV and UGV systems in K-12 STEM and CTE education**

## 🎯 Mission

Empower educators and students with accessible, standards-aligned resources for hands-on learning through unmanned vehicle systems. From basic remote control to advanced autonomous operations, this hub supports complete learning pathways in robotics, programming, and engineering principles.

Our goal is to make unmanned systems education accessible to all schools, regardless of budget or technical expertise, by providing free, open-source resources that align with educational standards and promote safe, responsible innovation.

---

## 🚁 What's Inside

- **Complete Build Guides** - Step-by-step UAV and UGV construction guides for multiple skill levels and budgets
- **Programming Resources** - Tutorials for Arduino, Raspberry Pi, ArduPilot, Betaflight, INAV, and MAVLink
- **Curriculum Integration** - Lesson plans aligned to NGSS, Common Core, ISTE, and CTE standards
- **Safety & Compliance** - Comprehensive guidance for educational settings and regulatory compliance
- **Hardware Designs** - Open-source CAD files, BOMs, and assembly instructions
- **Troubleshooting Resources** - Technical support documentation and common problem solutions
- **Assessment Tools** - Rubrics, project evaluations, and learning outcome measurements
- **Community Contributions** - Shared projects, lesson plans, and experiences from educators worldwide

---

## 🏁 Quick Start

### Choose Your Path

**New to unmanned systems?** → [Start Here](docs/getting-started/) - Begin with fundamentals and safety

**Educators preparing lessons?** → [Curriculum Integration](docs/curriculum-integration/) - Standards-aligned lesson plans

**Students building projects?** → [Student Projects](resources/student-projects/) - Hands-on project guides

**Technical staff setting up systems?** → [Setup & Configuration](docs/setup-configuration/) - Installation and setup guides

**Competition coaches?** → [Advanced Programming](docs/programming/) - Competition preparation resources

### Platform-Specific Resources

**Looking for a specific platform?**
- [UAV Systems](docs/uav-systems/) - Drones, quadcopters, and aerial platforms
- [UGV Systems](docs/ugv-systems/) - Ground vehicles, rovers, and autonomous cars
- [Programming Guides](docs/programming/) - Code examples and tutorials
- [Control Systems](docs/control-systems/) - Flight controllers and ground control stations

**Need help?** → [Troubleshooting](docs/troubleshooting/) - Common issues and solutions

---

## 🎓 Educational Levels

### Elementary (K-5)
- Basic unmanned systems concepts and terminology
- Safety awareness and responsible operation
- Simple supervised builds with adult guidance
- Introduction to remote control operations

### Middle School (6-8)
- Structured build projects with moderate complexity
- Block-based programming (Scratch, Blockly)
- Flight training and basic maneuvers
- Introduction to sensors and data collection
- Team collaboration projects

### High School (9-12)
- Advanced programming (Python, C++, Arduino)
- Autonomous navigation and mission planning
- Custom hardware integration
- Competition preparation (drone racing, autonomous challenges)
- Research projects and documentation

### Post-Secondary & Professional Development
- Advanced research applications
- Custom firmware development
- Industry-standard tools and workflows
- Career pathway exploration

---

## 🛠️ Supported Platforms

### Flight Controllers
- **ArduPilot** - Pixhawk 4, Pixhawk 6C, Cube Orange/Black, Holybro Kakute series
- **Betaflight** - Racing and acrobatic flight controllers
- **INAV** - Fixed-wing and multirotor navigation
- **Cleanflight** - Lightweight flight control
- **Navio2 + Raspberry Pi** - Linux-based flight control solution

### Embedded Systems
- **Arduino** - Uno, Mega 2560, Nano, Due, ESP32, ESP8266
- **Raspberry Pi** - Models 3B+, 4 (2GB/4GB/8GB), Zero 2 W, 5
- **STM32** - Advanced microcontroller development
- **Teensy** - High-performance Arduino-compatible boards

### Communication Protocols
- **MAVLink** - Micro Air Vehicle communication protocol
- **MSP** - MultiWii Serial Protocol for Betaflight/INAV
- **ROS/ROS2** - Robot Operating System integration
- **SBUS, PPM, IBUS** - RC receiver protocols
- **UART, SPI, I2C** - Hardware communication interfaces

### Ground Control Software
- **Mission Planner** (Windows) - Comprehensive GCS for ArduPilot
- **QGroundControl** (Cross-platform) - Universal ground control
- **Betaflight Configurator** - Setup and tuning for racing drones
- **INAV Configurator** - Configuration for INAV systems
- **MAVProxy** - Command-line GCS and routing

---

## 📚 Documentation Structure

```
docs/
├── index.md                   # Documentation hub with guided navigation
├── getting-started/           # Fundamentals, safety, first builds
├── uav-systems/               # UAV platforms, builds, and operations
├── ugv-systems/               # UGV platforms, builds, and operations
├── programming/               # Code tutorials and examples
├── setup-configuration/       # Installation and configuration guides
├── control-systems/           # Flight controllers and GCS setup
├── troubleshooting/           # Problem solving and diagnostics
├── safety-compliance/         # Safety protocols and regulations
├── curriculum-integration/    # Lesson plans and educational resources
├── references/                # Technical specifications and datasheets
└── glossary/                  # Terminology and definitions

code/
├── arduino/                   # Arduino sketches and libraries
├── raspberry-pi/              # Python scripts and Linux configurations
├── flight-controllers/        # Custom firmware and scripts
├── ground-station/            # GCS tools and automation
└── utilities/                 # Helper scripts and tools

hardware/
├── uav-designs/              # Airframe CAD files and specifications
├── ugv-designs/              # Ground vehicle designs
├── bill-of-materials/        # Component lists with sourcing info
└── assembly-guides/          # Step-by-step build instructions

resources/
├── curriculum/               # Complete curriculum packages
├── lesson-plans/             # Individual lesson plans
├── student-projects/         # Project templates and examples
└── assessment-tools/         # Rubrics and evaluation tools
```

---

## 🤝 Contributing

We welcome contributions from educators, students, industry professionals, and hobbyists! This is a community-driven project that thrives on shared knowledge and experiences.

### Ways to Contribute

- **Share lesson plans** - Help other educators with your successful activities
- **Submit student projects** - Showcase what your students have built
- **Improve documentation** - Fix errors, add clarity, or expand content
- **Add code examples** - Contribute working code and tutorials
- **Create hardware designs** - Share your build designs and BOMs
- **Report issues** - Help us identify problems and gaps
- **Suggest features** - Tell us what resources you need
- **Translate content** - Make resources accessible in other languages
- **Answer questions** - Help others in discussions

### Getting Started

1. Read our [Contributing Guidelines](CONTRIBUTING.md)
2. Check the [Code of Conduct](CODE_OF_CONDUCT.md)
3. Browse [open issues](../../issues) or create a new one
4. Fork the repository and make your changes
5. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on code style, documentation standards, and the review process.

---

## ⚖️ Safety & Legal

### Safety First

Operating unmanned systems in educational settings requires careful attention to safety protocols. Always:

- Conduct thorough risk assessments before any flight or operation
- Ensure proper supervision ratios (typically 1:5 for hands-on activities)
- Use appropriate personal protective equipment (PPE)
- Establish clear safety zones and emergency procedures
- Maintain equipment in airworthy/roadworthy condition
- Brief all participants on safety protocols before each session

### Regulatory Compliance

**United States:**
- **FAA Part 107** - Commercial drone operations (including most school uses)
- **44809 Exception** - Recreational operations in approved areas (limited school use)
- **School exemptions** - Some educational uses may qualify for special provisions

**International:**
Consult your local aviation/robotics authority:
- **Canada** - Transport Canada drone regulations
- **Europe** - EASA unmanned aircraft regulations
- **UK** - CAA drone code and registration
- **Australia** - CASA drone rules

See our complete [Safety & Compliance Guide](docs/safety-compliance/) for detailed information, risk assessment templates, and regulatory resources.

---

## 📖 License

This project uses multiple licenses to best serve the open-source education community:

- **Code & Software**: [MIT License](LICENSE) - Maximum freedom for use and modification
- **Documentation**: [Creative Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/) - Share and adapt with attribution
- **Hardware Designs**: [CERN Open Hardware License v2 - Permissive](https://ohwr.org/cern_ohl_p_v2.txt) - Open hardware with patent protection

See individual files and directories for specific license information.

---

## 💬 Community

Join our growing community of educators, students, and unmanned systems enthusiasts:

- **GitHub Discussions** - [Ask questions and share ideas](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub/discussions)
- **Issues** - [Report bugs or request features](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub/issues)
- **Email** - education@f3designed.com
- **Website** - [f3designed.com](https://f3designed.com)

### Community Guidelines

We are committed to providing a welcoming and inclusive environment. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

---

## 🌟 Featured Projects

_Coming Soon: Showcase of innovative student projects and educator implementations from our community_

Want to see your project featured here? Share it in [GitHub Discussions](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub/discussions) or submit a pull request!

---

## 📊 Project Stats

![GitHub Stars](https://img.shields.io/github/stars/F3DESIGNED/unmanned-vehicle-edu-hub?style=social)
![GitHub Forks](https://img.shields.io/github/forks/F3DESIGNED/unmanned-vehicle-edu-hub?style=social)
![GitHub Issues](https://img.shields.io/github/issues/F3DESIGNED/unmanned-vehicle-edu-hub)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/F3DESIGNED/unmanned-vehicle-edu-hub)
![Contributors](https://img.shields.io/github/contributors/F3DESIGNED/unmanned-vehicle-edu-hub)
![Last Commit](https://img.shields.io/github/last-commit/F3DESIGNED/unmanned-vehicle-edu-hub)
![License](https://img.shields.io/github/license/F3DESIGNED/unmanned-vehicle-edu-hub)

---

## 🗺️ Roadmap

### Current Focus (Q1 2025)
- [ ] Complete getting-started documentation
- [ ] Publish first set of curriculum-integrated lesson plans
- [ ] Add beginner-friendly UAV build guide
- [ ] Establish community guidelines and moderation

### Upcoming (Q2 2025)
- [ ] Advanced programming tutorials
- [ ] Competition preparation guides
- [ ] Video tutorial library
- [ ] Interactive troubleshooting tools

### Future Vision
- [ ] Multilingual support (Spanish, French, Mandarin)
- [ ] Virtual simulation environments
- [ ] Certification programs for educators
- [ ] Industry partnership program

---

## 🙏 Acknowledgments

This project builds on the incredible work of the open-source unmanned systems community, including:

- **ArduPilot** - Open-source autopilot platform
- **Betaflight** - High-performance flight control
- **INAV** - Navigation-focused flight control
- **QGroundControl** - Universal ground control software
- **PX4** - Professional autopilot platform
- **Educators worldwide** - Who contribute and provide feedback

Special thanks to all contributors who help make unmanned systems education accessible to everyone.

---

**Maintained by educators, for educators** | [F3Designed](https://f3designed.com) | [Documentation](docs/index.md) | © 2025

**[Back to Top](#unmanned-vehicle-systems-education-hub)**
