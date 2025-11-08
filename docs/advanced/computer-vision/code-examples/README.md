# Computer Vision Code Examples

This directory contains working code examples for all computer vision lessons. Each example is fully documented and tested.

## Directory Structure

```
code-examples/
├── 01-opencv-basics/
│   ├── camera_stream.py
│   ├── color_spaces.py
│   ├── color_detection.py
│   ├── edge_detection.py
│   └── README.md
├── 02-object-detection/
│   ├── template_matching.py
│   ├── contour_detection.py
│   ├── cascade_classifier.py
│   ├── yolo_detection.py
│   └── README.md
├── 03-feature-tracking/
│   ├── feature_detection.py
│   ├── optical_flow.py
│   ├── target_tracking.py
│   └── README.md
├── 04-visual-navigation/
│   ├── aruco_detection.py
│   ├── pose_estimation.py
│   ├── visual_servoing.py
│   └── README.md
├── 05-optimization/
│   ├── profiling_example.py
│   ├── threaded_processing.py
│   ├── gpu_acceleration.py
│   └── README.md
├── 06-ml-models/
│   ├── data_collection.py
│   ├── model_training.py
│   ├── model_deployment.py
│   └── README.md
└── utils/
    ├── drone_camera.py (camera abstraction)
    ├── display_helpers.py (visualization utilities)
    ├── performance_timer.py (profiling tools)
    └── README.md
```

## Usage Guidelines

### Running Examples

1. **Install dependencies**:
```bash
pip install opencv-python opencv-contrib-python numpy djitellopy
```

2. **Connect to drone**: Ensure drone is powered on and connected

3. **Run example**:
```bash
python 01-opencv-basics/camera_stream.py
```

### Code Structure

Each example follows this pattern:

```python
"""
Example: [Name]
Description: What this example demonstrates
Prerequisites: What students need first
Learning objectives: What students will learn
"""

import cv2
import numpy as np
from utils.drone_camera import DroneCamera

def main():
    # 1. Setup
    # 2. Main processing loop
    # 3. Cleanup
    pass

if __name__ == "__main__":
    main()
```

### Keyboard Controls

Standard controls across examples:
- **q**: Quit
- **s**: Save current frame
- **p**: Pause/unpause
- **r**: Reset/restart
- **h**: Show help overlay

## Example Categories

### Beginner Examples
Clear structure, extensive comments, simplified logic
- camera_stream.py
- color_detection.py

### Intermediate Examples
More complex logic, multiple components
- object_detection.py
- feature_tracking.py

### Advanced Examples
Full applications, error handling, optimization
- visual_navigation.py
- autonomous_mission.py

## Development Guidelines

When creating new examples:

1. **Documentation**: Clear docstrings and inline comments
2. **Error Handling**: Graceful failures with helpful messages
3. **Performance**: Display FPS counter for processing speed
4. **Visualization**: Show intermediate steps for learning
5. **Safety**: Include appropriate timeouts and limits
6. **Testing**: Test on minimum spec hardware

## Common Utilities

### DroneCamera Class
Abstracts different drone camera APIs:
```python
from utils.drone_camera import DroneCamera

camera = DroneCamera(drone_type='tello')
frame = camera.get_frame()
```

### Performance Timer
Measure execution time:
```python
from utils.performance_timer import Timer

with Timer("Processing"):
    result = process_frame(frame)
```

### Display Helpers
Visualization utilities:
```python
from utils.display_helpers import show_fps, draw_bbox

show_fps(frame, fps)
draw_bbox(frame, x, y, w, h, label="Target")
```

## Troubleshooting

### Camera connection issues
- Verify drone is powered and in range
- Check WiFi connection
- Restart drone and try again

### Poor performance
- Reduce resolution
- Lower frame rate
- Skip frames if processing is slow
- Use smaller detection models

### Import errors
- Check all dependencies installed
- Verify Python version (3.7+)
- Check OpenCV version (4.5+)

## Contributing

To add new examples:
1. Follow existing code structure
2. Include comprehensive comments
3. Test on Tello (minimum hardware)
4. Update this README
5. Submit pull request

## Additional Resources

- OpenCV documentation: https://docs.opencv.org/
- DJITelloPy documentation: https://djitellopy.readthedocs.io/
- Computer vision tutorials: [link to curated list]

---

**Note**: Examples are currently under development. Priority order matches lesson sequence. Contributions welcome!
