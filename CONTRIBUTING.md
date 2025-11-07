# Contributing to Unmanned Vehicle Systems Education Hub

Thank you for your interest in contributing! This project aims to provide comprehensive, accessible educational resources for unmanned vehicle systems.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Contribution Guidelines](#contribution-guidelines)
- [Style Guide](#style-guide)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### 1. Documentation

**Most valuable contributions:**
- Platform-specific build guides (aerial, ground, marine)
- Troubleshooting guides
- Lesson plans and curriculum resources
- Translations to other languages
- Improving clarity of existing docs
- Adding diagrams and visual aids

### 2. Code Examples

- Arduino/Python code examples
- Flight controller configuration examples
- Sensor integration tutorials
- Autonomous navigation examples
- Testing and validation scripts

### 3. Hardware Designs

- CAD files for 3D-printable parts
- Bill of Materials (BOMs) for builds
- Assembly guides with photos
- Wiring diagrams

### 4. Resources

- Lesson plans (with learning objectives)
- Worksheets and activities
- Assessment rubrics
- Presentation slides

### 5. Bug Reports and Feature Requests

See our [Issue Templates](.github/ISSUE_TEMPLATE/) for:
- Bug reports
- Feature requests
- Documentation improvements

## Getting Started

### Prerequisites

- Git installed on your computer
- Text editor (VS Code, Sublime, etc.)
- Basic markdown knowledge
- MkDocs (for testing documentation locally)

### Setting Up Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/unmanned-vehicle-edu-hub.git
   cd unmanned-vehicle-edu-hub
   ```

3. **Add upstream remote:**
   ```bash
   git remote add upstream https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub.git
   ```

4. **Install MkDocs** (for testing documentation):
   ```bash
   pip install -r requirements.txt
   ```

5. **Serve documentation locally:**
   ```bash
   mkdocs serve
   ```
   Visit http://localhost:8000 to view

### Branching Strategy

- `main` - Stable, published content
- `develop` - Integration branch for new features
- Feature branches - Your contributions

**Create a feature branch:**
```bash
git checkout -b feature/your-feature-name
```

Use descriptive branch names:
- `docs/battery-safety-expansion`
- `guide/pixhawk-rover-build`
- `fix/broken-links-getting-started`
- `resource/lesson-plan-intro-to-drones`

## Contribution Guidelines

### Documentation Contributions

#### Content Requirements

✅ **Do:**
- Write in clear, accessible language
- Use proper grammar and spelling
- Include code blocks with syntax highlighting
- Add images/diagrams when helpful (optimize file size)
- Cross-reference related topics
- Test all links
- Include YAML frontmatter (title, description)
- Follow existing structure and style

❌ **Don't:**
- Use overly technical jargon without explanation
- Copy content from copyrighted sources without permission
- Include personal contact information
- Link to commercial products without disclosure
- Make safety claims without verification

#### Safety Content

Safety-related documentation requires **extra scrutiny**:

- **Accuracy is critical** - verify all safety procedures
- **Cite sources** for regulations and standards
- **Be comprehensive** - don't leave out important warnings
- **Use proper formatting** - admonitions for warnings/dangers
- **Review carefully** - safety errors can cause harm

Example of proper safety warning:
```markdown
!!! danger "Critical Safety Warning"
    Never charge LiPo batteries unattended. Fires can start rapidly and spread quickly. Always use a LiPo safe bag and stay in the same room during charging.
```

#### Documentation Structure

All documentation should include:

**Frontmatter:**
```yaml
---
title: Your Page Title
description: Brief description for SEO and navigation
---
```

**Sections:**
- Introduction/Overview
- Prerequisites (if applicable)
- Main content (logical sections)
- Examples/Demonstrations
- Troubleshooting (if applicable)
- Related Topics/Next Steps
- Last Updated date

### Code Contributions

#### Code Requirements

- **Tested** - Code must be verified to work
- **Commented** - Explain complex sections
- **Safe** - No unsafe practices (especially with hardware)
- **Documented** - README explaining usage
- **Licensed** - Compatible with MIT license (code)

#### Code Structure

```
code/
  examples/
    platform-name/
      feature-name/
        README.md          # Purpose, requirements, usage
        main.ino|.py|.cpp  # Main code file
        wiring-diagram.png # Circuit diagram (if applicable)
        requirements.txt   # Dependencies (if applicable)
```

#### Example README Template

```markdown
# Feature Name

Brief description of what this code does.

## Hardware Requirements

- Platform: [e.g., Arduino Uno, Raspberry Pi 4]
- Sensors: [e.g., MPU6050 IMU]
- Other: [motors, ESCs, etc.]

## Wiring

[Description or reference to diagram]

## Dependencies

- Library name (version)

## Installation

1. Install dependencies
2. Upload code
3. Configure

## Usage

How to run and use the code.

## Expected Output

What should happen when running correctly.

## Troubleshooting

Common issues and solutions.

## License

MIT License - See LICENSE file
```

### Hardware Contributions

#### CAD Files

- **Format:** STEP, STL (for 3D printing), or Fusion 360 (.f3d)
- **Units:** Clearly specified (mm, inches)
- **Orientation:** Print-ready for STL files
- **Tested:** Actually printed/manufactured if possible

#### Bill of Materials (BOM)

Use markdown table format:

```markdown
| Part | Quantity | Description | Source | Est. Cost |
|------|----------|-------------|--------|-----------|
| Frame | 1 | 5" carbon fiber frame | Generic | $30-50 |
| Motors | 4 | 2207 2450KV brushless | Multiple | $60-80 |
```

### Resource Contributions

#### Lesson Plans

Must include:
- **Grade/Age Level:** Target audience
- **Duration:** Time required
- **Learning Objectives:** What students will learn
- **Materials Needed:** Complete list
- **Procedure:** Step-by-step instructions
- **Assessment:** How to evaluate learning
- **Standards Alignment:** (if applicable) NGSS, ISTE, etc.

## Style Guide

### Markdown Formatting

**Headings:**
```markdown
# Page Title (H1 - one per page)
## Major Section (H2)
### Subsection (H3)
#### Minor Section (H4)
```

**Lists:**
```markdown
- Unordered list
- Another item
  - Nested item

1. Ordered list
2. Another item
```

**Code:**
```markdown
Inline code: `variable_name`

Code block:
```python
def function():
    return "Hello"
```
```

**Links:**
```markdown
[Link text](relative/path/to/file.md)
[External link](https://example.com)
```

**Images:**
```markdown
![Alt text](relative/path/to/image.png)
```

**Tables:**
```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

**Admonitions:**
```markdown
!!! note "Optional Title"
    Note content

!!! tip "Helpful Tip"
    Tip content

!!! warning "Warning"
    Warning content

!!! danger "Critical Warning"
    Danger content
```

### Writing Style

**Voice:**
- Active voice preferred: "Connect the battery" not "The battery should be connected"
- Second person: "You will need" not "One will need"
- Present tense: "The motor spins" not "The motor will spin"

**Tone:**
- Professional but approachable
- Educational, not condescending
- Encouraging for beginners
- Precise for technical content

**Terminology:**
- Use terms from [Glossary](docs/glossary/index.md)
- Define technical terms on first use
- Be consistent with terminology
- Spell out acronyms on first use: "Unmanned Aerial Vehicle (UAV)"

### File Naming

**Markdown files:**
- Lowercase with hyphens: `getting-started.md`
- Descriptive: `battery-safety.md` not `safety1.md`

**Images:**
- Descriptive: `pixhawk-wiring-diagram.png`
- Include platform/topic: `tello-programming-scratch-example.png`

**Code files:**
- Follow language conventions:
  - Python: `snake_case.py`
  - C++/Arduino: `camelCase.cpp` or `snake_case.ino`

### Image Guidelines

- **Format:** PNG for diagrams/screenshots, JPEG for photos
- **Size:** Optimize for web (<500KB preferred)
- **Resolution:** 72-96 DPI for web
- **Width:** Max 1200px wide
- **Alt text:** Always include descriptive alt text
- **Location:** Store in `media/images/` with organized subdirectories

## Submitting Changes

### Pull Request Process

1. **Update your fork:**
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**

4. **Test locally:**
   ```bash
   mkdocs serve
   # Visit http://localhost:8000 and verify your changes
   ```

5. **Commit with clear message:**
   ```bash
   git add .
   git commit -m "Add detailed battery charging guide to safety section"
   ```

6. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create Pull Request** on GitHub:
   - Use descriptive title
   - Reference any related issues
   - Describe changes in detail
   - Add screenshots if relevant
   - Check "Allow edits from maintainers"

### Pull Request Template

```markdown
## Description

Brief description of changes.

## Type of Change

- [ ] Documentation update
- [ ] New guide/tutorial
- [ ] Code example
- [ ] Hardware design
- [ ] Bug fix
- [ ] Other (describe)

## Checklist

- [ ] Tested locally with `mkdocs serve`
- [ ] All links work correctly
- [ ] Images optimized and include alt text
- [ ] Followed style guide
- [ ] Updated navigation in mkdocs.yml (if new pages)
- [ ] No spelling/grammar errors
- [ ] Safety content reviewed carefully (if applicable)

## Related Issues

Closes #123
Related to #456

## Screenshots (if applicable)

[Add screenshots of new pages/features]

## Additional Notes

Any other context about the changes.
```

### Review Process

1. **Automated checks** - PR must pass:
   - Markdown linting
   - Link checking
   - MkDocs build

2. **Maintainer review** - Will check:
   - Content accuracy
   - Style compliance
   - Safety information correctness
   - Overall quality

3. **Feedback** - Maintainers may request changes

4. **Approval and merge** - Once approved, PR will be merged

### After Merging

- Your contribution is live!
- You'll be added to contributors list
- Thank you for improving the hub!

## Recognition

Contributors will be recognized in:
- Repository contributors list (automatic)
- Annual acknowledgments
- Community highlights

## Questions?

- **General questions:** [Open a discussion](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub/discussions)
- **Bug reports:** [Open an issue](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub/issues)
- **Security concerns:** See SECURITY.md

## License

By contributing, you agree that your contributions will be licensed under:
- **Code:** MIT License
- **Documentation:** Creative Commons Attribution-ShareAlike 4.0 (CC-BY-SA 4.0)

See [LICENSE](LICENSE) and [LICENSE-docs](LICENSE-docs) files for details.

---

**Thank you for contributing to unmanned vehicle systems education!**
