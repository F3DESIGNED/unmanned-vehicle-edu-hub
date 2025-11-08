# Computer Vision for Unmanned Vehicles

Computer vision enables drones to perceive and understand their environment through cameras, opening possibilities for autonomous navigation, object detection, tracking, and intelligent decision-making.

## Overview

This pathway teaches students how to:
- Process images and video streams from drone cameras
- Detect and recognize objects in real-time
- Track targets and features across frames
- Enable visual-based autonomous navigation
- Apply machine learning to visual tasks

## Prerequisites

- **Programming**: Comfortable with Python, basic understanding of arrays/matrices
- **Math**: Basic algebra, understanding of coordinate systems
- **Drone Skills**: Ability to fly and program basic autonomous missions
- **Recommended**: Completed beginner and intermediate curriculum

## Learning Objectives

By completing this pathway, students will be able to:

1. **Image Processing Fundamentals**
   - Capture and process images from drone cameras
   - Apply filters and transformations
   - Extract features from images

2. **Object Detection**
   - Detect predefined objects using classical methods
   - Implement color-based detection
   - Use pre-trained ML models for object recognition

3. **Visual Tracking**
   - Track objects across video frames
   - Implement feature-based tracking
   - Handle occlusion and tracking failures

4. **Visual Navigation**
   - Use visual markers for localization
   - Implement visual servoing
   - Follow targets using vision

## Pathway Structure

### Module 1: OpenCV Basics (3-4 weeks)
Introduction to computer vision library and image processing fundamentals

- [Lesson: OpenCV Basics](./lesson-plans/opencv-basics.md)
- [Code Examples](./code-examples/)
- [Project: Color-based Landing Pad Detection](./projects/)

### Module 2: Object Detection (4-5 weeks)
Classical and modern approaches to detecting objects in images

- [Lesson: Object Detection Methods](./lesson-plans/object-detection.md)
- [Code Examples](./code-examples/)
- [Project: Autonomous Object Search](./projects/)

### Module 3: Feature Detection & Tracking (3-4 weeks)
Finding and following distinctive features across frames

- Code Examples and Projects TBD

### Module 4: Face & Pattern Recognition (2-3 weeks)
Using pre-trained models for recognition tasks

- Code Examples and Projects TBD

### Module 5: Visual Navigation (4-5 weeks)
Using vision to navigate and avoid obstacles

- Code Examples and Projects TBD

### Module 6: Real-time Processing (2-3 weeks)
Optimizing for speed and performance on embedded systems

- Code Examples and Projects TBD

### Module 7: Machine Learning Integration (4-5 weeks)
Training custom models for specific detection tasks

- Code Examples and Projects TBD

## Hardware Requirements

### Minimum Setup
- Drone with programmable camera (DJI Tello or equivalent)
- Computer for development and processing
- Good lighting conditions

### Recommended Setup
- Drone with HD camera and SDK access
- Dedicated processing computer or Raspberry Pi
- Controlled indoor environment
- Calibration patterns and targets

### Advanced Setup
- Drone with gimbal-stabilized camera
- GPU-equipped processing system
- Multiple cameras for stereo vision
- Professional lighting setup

## Software Tools

### Required
- **Python 3.7+**: Primary programming language
- **OpenCV 4.5+**: Computer vision library
- **NumPy**: Numerical computing
- **Drone SDK**: Platform-specific (DJITelloPy, DroneKit, etc.)

### Recommended
- **Matplotlib**: Visualization and debugging
- **TensorFlow/PyTorch**: Machine learning (for advanced modules)
- **Jupyter Notebooks**: Interactive development

## Projects Overview

Students complete progressively challenging projects:

1. **Color Detection**: Detect colored objects and report locations
2. **Landing Pad Recognition**: Autonomously find and land on marked pad
3. **Object Search**: Search area and photograph specific objects
4. **Target Following**: Track and follow moving target
5. **Obstacle Avoidance**: Navigate using visual obstacle detection
6. **Custom Recognition**: Train model to detect specific items
7. **Capstone Project**: Original application combining multiple techniques

See [Projects](./projects/) directory for detailed project specifications.

## Assessment Criteria

Students demonstrate mastery through:

- **Code Quality**: Clean, documented, functional implementations
- **Technical Understanding**: Explain algorithms and design decisions
- **Project Demos**: Working demonstrations of capabilities
- **Problem Solving**: Debug issues and optimize performance
- **Safety**: Maintain safe operations during vision-based flights

## Resources

### Learning Materials
- OpenCV documentation and tutorials
- Computer vision textbooks and papers
- Online courses (Coursera, Udacity, etc.)
- Research papers on drone vision applications

### Community Support
- Advanced learners study group
- Computer vision specialty forum
- Industry mentor connections
- Competition teams (SUAS, etc.)

## Career Connections

Computer vision skills prepare students for:

- **Computer Vision Engineer**: Develop vision systems for robotics
- **Autonomous Systems Developer**: Build self-driving vehicles
- **AI/ML Engineer**: Create intelligent vision applications
- **Research Scientist**: Advance state-of-the-art in visual perception
- **Drone Applications Specialist**: Industry-specific vision solutions

## Next Steps

1. **Review prerequisites** - Complete diagnostic assessment
2. **Set up development environment** - Install required software
3. **Start Module 1** - OpenCV basics and first project
4. **Join community** - Connect with other computer vision students
5. **Plan capstone** - Begin thinking about final project ideas

---

**Ready to give your drone the gift of sight? Start with [OpenCV Basics](./lesson-plans/opencv-basics.md)!**
