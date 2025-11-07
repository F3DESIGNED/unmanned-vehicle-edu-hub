# Contributing to Unmanned Vehicle Systems Education Hub

Thank you for your interest in contributing to the Unmanned Vehicle Systems Education Hub! This project thrives on the collective knowledge and experience of educators, students, industry professionals, and unmanned systems enthusiasts worldwide.

Whether you're fixing a typo, adding a lesson plan, contributing code, or sharing a hardware design, your contribution makes a difference in making unmanned systems education accessible to everyone.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Ways to Contribute](#ways-to-contribute)
- [Getting Started](#getting-started)
- [Contribution Workflow](#contribution-workflow)
- [Style Guidelines](#style-guidelines)
- [Documentation Standards](#documentation-standards)
- [Code Standards](#code-standards)
- [Hardware Contributions](#hardware-contributions)
- [Testing Requirements](#testing-requirements)
- [Review Process](#review-process)
- [Recognition](#recognition)
- [Questions?](#questions)

---

## Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct. By participating, you are expected to uphold this code. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

We are committed to providing a welcoming, inclusive, and harassment-free experience for everyone, regardless of:
- Age, body size, disability, ethnicity, gender identity and expression
- Level of experience, education, or socioeconomic status
- Nationality, personal appearance, race, religion
- Sexual identity and orientation

---

## Ways to Contribute

### 📝 Documentation

- **Fix errors** - Typos, broken links, or technical inaccuracies
- **Add clarity** - Improve explanations or add missing details
- **Create tutorials** - Write step-by-step guides for new topics
- **Translate content** - Make resources accessible in other languages
- **Add diagrams** - Create visual aids to explain complex concepts

### 💻 Code

- **Example code** - Arduino sketches, Python scripts, configuration files
- **Utility tools** - Scripts that help with setup, testing, or troubleshooting
- **Ground control software** - GCS plugins or automation tools
- **Bug fixes** - Fix issues reported in the issue tracker

### 🔧 Hardware

- **Build designs** - CAD files for UAV/UGV frames and components
- **Bills of materials** - Component lists with sourcing information
- **Assembly guides** - Step-by-step build instructions with photos
- **Testing reports** - Performance data and evaluation results

### 🎓 Educational Resources

- **Lesson plans** - Complete activities aligned to educational standards
- **Curriculum packages** - Multi-lesson units with assessments
- **Student projects** - Project templates and examples
- **Assessment tools** - Rubrics, quizzes, and evaluation criteria
- **Safety procedures** - Risk assessments and safety protocols

### 🐛 Issues and Ideas

- **Report bugs** - Help us identify problems
- **Request features** - Suggest new resources or improvements
- **Answer questions** - Help others in discussions and issues
- **Provide feedback** - Share your experience using these resources

---

## Getting Started

### Prerequisites

Before you begin, ensure you have:

1. **GitHub Account** - [Sign up](https://github.com/signup) if you don't have one
2. **Git Installed** - [Download Git](https://git-scm.com/downloads)
3. **Text Editor** - VS Code, Atom, Sublime, or similar
4. **Markdown Knowledge** - [Markdown Guide](https://www.markdownguide.org/) (for documentation)

### First-Time Contributors

If you're new to open source, welcome! Here are some resources to help you get started:

- [First Contributions Guide](https://github.com/firstcontributions/first-contributions)
- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)

Look for issues labeled `good first issue` or `help wanted` - these are great starting points!

---

## Contribution Workflow

### 1. Fork the Repository

Click the "Fork" button at the top right of the repository page to create your own copy.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/unmanned-vehicle-edu-hub.git
cd unmanned-vehicle-edu-hub
```

### 3. Create a Branch

Create a descriptive branch name based on your contribution:

```bash
# For features
git checkout -b feature/add-arducopter-tutorial

# For bug fixes
git checkout -b fix/broken-link-in-readme

# For documentation
git checkout -b docs/improve-safety-guide

# For lessons/curriculum
git checkout -b lesson/middle-school-drone-basics
```

### 4. Make Your Changes

- Follow the style guidelines for your contribution type
- Test your changes thoroughly
- Commit often with clear messages

### 5. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "Add ArduCopter setup tutorial for beginners"
```

**Commit Message Guidelines:**

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Start with a capital letter
- No period at the end
- Keep first line under 50 characters
- Add detailed description after blank line if needed

**Examples:**

```
Good: Add Betaflight configuration guide for racing drones
Bad: added betaflight stuff

Good: Fix broken links in troubleshooting section
Bad: fixed links

Good: Update lesson plan with NGSS alignment
Bad: updates
```

### 6. Push to Your Fork

```bash
git push origin your-branch-name
```

### 7. Create a Pull Request

1. Go to the original repository on GitHub
2. Click "Pull Requests" → "New Pull Request"
3. Click "compare across forks"
4. Select your fork and branch
5. Fill out the PR template with:
   - **Clear title** describing the change
   - **Description** of what you changed and why
   - **Related issues** (use "Closes #123" to auto-close issues)
   - **Testing performed**
   - **Screenshots** (if applicable)

---

## Style Guidelines

### General Principles

- **Clarity over brevity** - Explain thoroughly for diverse audiences
- **Inclusive language** - Use gender-neutral terms, avoid jargon
- **Accessibility** - Consider screen readers and visual impairments
- **Safety first** - Always emphasize safety protocols
- **Educational focus** - Remember the K-12 audience

### File Naming Conventions

- Use lowercase with hyphens: `getting-started-guide.md`
- Be descriptive: `pixhawk-4-setup.md` not `px4-setup.md`
- Include version numbers when relevant: `qgroundcontrol-v4.2-guide.md`

---

## Documentation Standards

All documentation should follow these standards for consistency and readability.

### Markdown Formatting

#### Heading Hierarchy

Use proper heading levels - never skip levels:

```markdown
# H1 - Document Title (only one per file)

## H2 - Major Section

### H3 - Subsection

#### H4 - Minor Point

##### H5 - Rarely used

###### H6 - Avoid if possible
```

#### Lists

Use consistent spacing and formatting:

```markdown
- Use hyphens for unordered lists
  - Indent with 2 spaces for nested items
  - Keep consistent throughout

1. Use numbers for ordered lists
2. GitHub will auto-number in display
3. But keep source sequential for readability
```

#### Code Blocks

Always specify the language for syntax highlighting:

````markdown
```python
# Python example
import time
print("Hello World")
```

```cpp
// Arduino C++ example
void setup() {
  Serial.begin(9600);
}
```

```bash
# Shell commands
cd /path/to/directory
ls -la
```
````

#### Links

- **Internal links** - Use relative paths: `[Getting Started](docs/getting-started/)`
- **External links** - Use full URLs: `[ArduPilot](https://ardupilot.org)`
- **Anchor links** - For in-page navigation: `[Back to Top](#top)`

#### Images

```markdown
![Alt text describing the image](../media/images/pixhawk-wiring.jpg)
```

- Always include alt text for accessibility
- Use relative paths for repository images
- Optimize images (< 1MB preferred)
- Use PNG for screenshots, JPG for photos

### YAML Frontmatter

Add frontmatter to documentation files for static site generators:

```yaml
---
title: "ArduCopter Setup Guide"
description: "Complete setup guide for ArduCopter on Pixhawk 4"
author: "Your Name"
date: 2025-01-15
category: "UAV Systems"
difficulty: "Beginner"
platform: "ArduPilot"
---
```

### Document Structure

Long documents (>500 words) should include:

1. **Title** (H1)
2. **Brief description/summary**
3. **Table of contents** (auto-generated or manual)
4. **Content sections** (H2/H3)
5. **Related resources** section
6. **Back to top** link at bottom

**Example:**

```markdown
# Advanced Waypoint Navigation

This guide covers creating and executing complex waypoint missions using QGroundControl.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Creating Waypoints](#creating-waypoints)
- [Advanced Options](#advanced-options)
- [Troubleshooting](#troubleshooting)

## Prerequisites

[Content...]

## Creating Waypoints

[Content...]

---

**Related Resources:**
- [QGroundControl Installation](qgc-install.md)
- [MAVLink Protocol Basics](../references/mavlink-basics.md)

[Back to Top](#advanced-waypoint-navigation)
```

### Writing Style

- **Use second person** ("you") when addressing readers
- **Active voice** preferred over passive
- **Short sentences** - aim for 15-20 words average
- **Short paragraphs** - 2-4 sentences ideal
- **Bullet points** for lists of items
- **Numbered lists** for sequential steps
- **Bold** for emphasis, **not** CAPS
- **Code formatting** for commands, file names, variable names

---

## Code Standards

### Python

Follow **PEP 8** style guide:

```python
# Good
def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate distance between two GPS coordinates.

    Args:
        lat1 (float): Latitude of first point
        lon1 (float): Longitude of first point
        lat2 (float): Latitude of second point
        lon2 (float): Longitude of second point

    Returns:
        float: Distance in meters
    """
    # Implementation here
    return distance

# Bad
def calcDist(a,b,c,d):
    return dist
```

**Key points:**
- 4 spaces for indentation (not tabs)
- Maximum line length: 79 characters
- Docstrings for all functions
- Descriptive variable names
- Type hints when appropriate

### Arduino/C++

Follow **Arduino Style Guide**:

```cpp
// Good
const int LED_PIN = 13;
int sensorValue = 0;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(A0);
  digitalWrite(LED_PIN, HIGH);
  delay(1000);
}

// Bad
int lp=13;
int sv=0;
void setup(){pinMode(lp,OUTPUT);Serial.begin(9600);}
void loop(){sv=analogRead(A0);digitalWrite(lp,HIGH);delay(1000);}
```

**Key points:**
- 2 spaces for indentation
- `camelCase` for variables and functions
- `UPPER_CASE` for constants
- Opening braces on same line
- Comments for complex logic
- Descriptive names

### Shell Scripts

```bash
#!/bin/bash

# Good - Clear and documented
install_dependencies() {
  echo "Installing required packages..."
  sudo apt-get update
  sudo apt-get install -y \
    python3-pip \
    git \
    screen
}

# Bad - No comments, unclear
inst_deps() {
  sudo apt-get update && sudo apt-get install -y python3-pip git screen
}
```

### Configuration Files

- **Use comments** to explain non-obvious settings
- **Provide examples** with common values
- **Document units** (meters, seconds, etc.)
- **Group related** settings together

---

## Hardware Contributions

### CAD Files

- **Provide source files** (STEP, Fusion 360, SolidWorks, etc.)
- **Include STL** files for 3D printing
- **Add renders** showing the design
- **Specify units** (mm preferred)

### Bills of Materials (BOM)

Use this template:

| Qty | Part | Description | Approx. Cost | Supplier Link |
|-----|------|-------------|--------------|---------------|
| 1 | Pixhawk 4 | Flight controller | $180 | [Link] |
| 4 | 2205 Motors | 2300KV brushless | $60 | [Link] |

- Include total cost estimate
- List multiple suppliers when possible
- Note regional availability
- Specify compatible alternatives

### Assembly Guides

- **Step-by-step** with numbered instructions
- **High-quality photos** at each step
- **Highlight critical** connections
- **Note common mistakes**
- **Include tool list** needed
- **Estimate time** required

---

## Testing Requirements

### Documentation

- **Check all links** work correctly
- **Verify code snippets** are correct
- **Test commands** in relevant environment
- **Preview markdown** rendering

### Code

- **Test on target platform** (Arduino board, Raspberry Pi, etc.)
- **Verify compatibility** with stated versions
- **Include test results** in PR description
- **Document dependencies**

### Hardware

- **Build and test** the design if possible
- **Document testing** conditions and results
- **Note any issues** or improvements needed
- **Provide photos/videos** of built hardware

---

## Review Process

### What to Expect

1. **Initial Review** - A maintainer will review within 3-5 days
2. **Feedback** - You may be asked to make changes
3. **Discussion** - Engage constructively with feedback
4. **Approval** - Two maintainer approvals required for merge
5. **Merge** - Your contribution is added to the project!

### Common Feedback

- Formatting issues
- Missing documentation
- Style guide violations
- Insufficient testing
- Licensing concerns

**Don't be discouraged by feedback!** It's part of the process and helps maintain quality.

### After Merge

- Your contribution will appear in the repository
- You'll be added to the contributors list
- Consider subscribing to issue notifications
- Help review others' contributions!

---

## Recognition

We value all contributions, large and small! Contributors are recognized:

- **Contributors list** in README.md
- **Git commit history** preserves authorship
- **Release notes** highlight significant contributions
- **Community showcase** for exceptional work

Special recognition badges available for:
- First-time contributors
- Regular contributors
- Documentation champions
- Code contributors
- Hardware designers
- Curriculum developers

---

## Questions?

### Where to Ask

- **General questions** - [GitHub Discussions](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub/discussions)
- **Contribution process** - Open an issue with "Question" label
- **Code review questions** - Comment on your PR
- **Private matters** - education@f3designed.com

### Additional Resources

- [GitHub Documentation](https://docs.github.com)
- [Markdown Guide](https://www.markdownguide.org)
- [PEP 8 Python Style Guide](https://pep8.org)
- [Arduino Style Guide](https://www.arduino.cc/en/Reference/StyleGuide)

---

## Thank You!

Your contributions help make unmanned systems education accessible to students and educators worldwide. Whether you're fixing a typo or contributing a complete curriculum unit, your work matters.

**Happy Contributing!**

---

**Related Documents:**
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [README](README.md)
- [License Information](LICENSE)

[Back to Top](#contributing-to-unmanned-vehicle-systems-education-hub)
