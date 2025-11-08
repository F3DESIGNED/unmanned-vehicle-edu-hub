# OpenCV Basics for Drone Vision

**Duration**: 2-3 hours | **Difficulty**: Intermediate | **Prerequisites**: Python basics, basic drone programming

## Lesson Overview (OUTLINE)

Introduction to OpenCV library and fundamental image processing operations for drone applications. Students learn to capture, display, and manipulate images from drone cameras.

## Learning Objectives

1. Install and configure OpenCV for drone camera access
2. Capture and display images from drone video stream
3. Apply basic image transformations (resize, crop, rotate)
4. Perform color space conversions (RGB, HSV, grayscale)
5. Use basic image filtering (blur, edge detection)

## Key Topics to Cover

### Part 1: OpenCV Setup & Architecture
- Installing OpenCV and dependencies
- Understanding image representation (numpy arrays)
- Connecting to drone camera feed
- Displaying images and video streams

### Part 2: Image Fundamentals
- Pixels, channels, and color spaces
- Image coordinates and regions of interest
- Reading drone camera properties
- Frame rate and resolution considerations

### Part 3: Color Space Operations
- RGB vs BGR (OpenCV quirk)
- Converting to HSV for color detection
- Grayscale conversion for processing efficiency
- When to use which color space

### Part 4: Basic Transformations
- Resizing images (upsampling/downsampling)
- Cropping regions of interest
- Rotating and flipping
- Geometric transformations

### Part 5: Filtering Operations
- Gaussian blur for noise reduction
- Edge detection (Canny)
- Thresholding for segmentation
- Morphological operations (erode, dilate)

## Hands-On Exercises

### Exercise 1: Camera Stream Capture
Connect to drone camera and display live video feed with FPS counter

### Exercise 2: Color Space Explorer
Interactive tool to convert between color spaces and visualize channels

### Exercise 3: Color Detection
Detect objects of specific colors in drone camera feed using HSV thresholding

### Exercise 4: Edge Detection
Apply Canny edge detection to identify features in drone's view

## Challenge Activity

**Target Finder**: Create a program that detects brightly colored landing targets in the drone's camera feed and draws bounding boxes around them.

**Extensions**:
- Calculate target centroid for navigation
- Display distance to target center
- Filter false positives using area thresholds

## Code Examples Structure

```python
# 01_camera_basics.py - Stream from drone camera
# 02_color_spaces.py - Explore RGB, HSV, grayscale
# 03_color_detection.py - Detect specific colors
# 04_edge_detection.py - Find edges in images
# 05_target_finder.py - Challenge solution template
```

## Assessment Criteria

- Successfully captures and displays drone camera feed
- Correctly converts between color spaces
- Implements working color-based detection
- Applies appropriate filters for task
- Code is clean and properly documented

## Common Challenges

1. **BGR vs RGB confusion**: OpenCV uses BGR by default
2. **HSV ranges**: Understanding 0-179 hue range in OpenCV
3. **Performance**: Processing speed vs image quality tradeoffs
4. **Lighting variations**: Detection robustness in different conditions

## Resources Needed

- Drone with camera (DJI Tello minimum)
- OpenCV 4.5+ installed
- Colored objects for testing (bright red, green, blue)
- Prepared test images/videos

## Next Lesson

[Object Detection Methods](./object-detection.md) - Building on color detection to identify complex objects

---

**Note**: This is an outline. Full lesson plan should be developed following the lesson-template.md structure with detailed timing, complete code examples, and assessment rubrics.
