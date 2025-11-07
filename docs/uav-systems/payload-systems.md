# UAV Payload Systems

Payload integration extends UAV capabilities beyond basic flight, enabling data collection, imaging, delivery, and research applications essential for advanced STEM education.

## Overview

**Payloads** are devices carried by the UAV to accomplish mission objectives beyond flight itself. Understanding payload integration teaches systems thinking, power management, and mission planning.

### Educational Value
- Real-world applications (mapping, inspection, delivery)
- Integration challenges (weight, power, mounting)
- Data collection and analysis
- Interdisciplinary connections (geography, environmental science, photography)
- Competition preparation (AUVSI SUAS, delivery challenges)

## Payload Categories

### 1. Imaging Systems
**Purpose**: Visual data collection, inspection, mapping

**Types**:
- Action cameras (GoPro, Insta360)
- FPV cameras (real-time piloting)
- Smartphone cameras (budget option)
- Machine vision cameras (OpenCV integration)
- Thermal cameras (FLIR, Seek Thermal)
- Multispectral (agricultural analysis)

### 2. Sensors & Data Collection
**Purpose**: Environmental monitoring, research

**Types**:
- GPS modules (location tracking)
- Temperature/humidity sensors
- Air quality sensors (particulate, CO2)
- Radiation detectors
- Magnetometers (metal detection)
- Ultrasonic rangefinders

### 3. Delivery Systems
**Purpose**: Transport and release mechanisms

**Types**:
- Servo-actuated release mechanisms
- Gripper systems
- Parachute deployment
- Water/powder dispensers
- Medical supply delivery

### 4. Communication Systems
**Purpose**: Extended range, data relay

**Types**:
- Long-range telemetry radios
- 4G/LTE modems
- Mesh networking modules
- Amateur radio repeaters

## Imaging Systems

### Action Cameras

#### GoPro / Similar Action Cameras
**Specifications**:
- Weight: 100-150g
- Resolution: 4K/60fps, 5K/30fps
- Stabilization: Built-in (GoPro HyperSmooth)
- Battery Life: 1-2 hours
- Control: WiFi, USB, trigger cable

**Integration**:
- **Mounting**: 3D printed mounts, rubber vibration dampeners
- **Power**: Internal battery (no external power needed)
- **Triggering**: Flight controller PWM output → servo lead adapter
- **Best For**: High-quality video, established workflow, easy post-processing

**Educational Projects**:
- Aerial photography/videography
- Mapping with photogrammetry software
- Event coverage (sports, school functions)
- Real estate mock projects

#### FPV Cameras
**Specifications**:
- Weight: 5-15g
- Resolution: Analog (NTSC/PAL) or Digital (DJI, HDZero)
- Latency: <50ms (analog), <30ms (digital)
- Field of View: 120-170° adjustable

**Integration**:
- **Power**: 5V from FC or PDB
- **Video Out**: To VTX (video transmitter)
- **Best For**: Real-time piloting, FPV flight training, immersive experience

**Educational Value**:
- Teaches RF principles (video transmission)
- Piloting from onboard perspective
- Latency awareness

#### Smartphone/Raspberry Pi Camera
**Specifications**:
- Weight: 3g (Pi Camera), 150g+ (smartphone)
- Resolution: Varies, typically 1080p-4K
- Control: Programmable (Python on Pi)
- Cost: $25 (Pi Camera) vs $0 (old smartphones)

**Integration**:
- **Raspberry Pi Camera**: Direct CSI connection to Pi
- **Smartphone**: Custom mount, WiFi control or scheduled recording
- **Best For**: Budget builds, programming integration, CV projects

**Educational Projects**:
- Computer vision (OpenCV object detection)
- Automated photography missions
- QR code / marker detection
- Low-cost mapping

### Gimbal Systems

**Purpose**: Stabilize camera for smooth footage

**Types**:
- **2-Axis**: Roll + Pitch stabilization
- **3-Axis**: Roll + Pitch + Yaw stabilization

**Integration**:
- Gimbal controller (SimpleBGC, Storm32)
- PWM control from flight controller
- Dedicated power circuit (clean power critical)

**Weight/Cost**:
- 2-Axis: 100-200g, $40-80
- 3-Axis: 200-400g, $80-200

**Educational Consideration**:
- Adds significant weight (larger platform needed)
- Complex to tune
- Great for demonstrating control systems

### Thermal Imaging

**Purpose**: Temperature mapping, night vision, energy audits

**Options**:
- **FLIR One**: Smartphone attachment, 80×60 resolution, ~$200
- **Seek Thermal**: Standalone, 206×156 resolution, $250-500
- **High-End Thermal**: FLIR Vue, 640×512, $3000+

**Educational Applications**:
- Building energy audits (heat loss detection)
- Wildlife observation (night missions)
- Search and rescue simulation
- STEM/physics demonstrations (heat transfer)

**Integration Challenges**:
- Weight (150-250g for entry-level)
- Data logging (requires companion computer or SD recording)
- Calibration complexity

## Sensors & Data Collection

### Environmental Sensors

#### Temperature & Humidity
**Sensors**: DHT22, BME280, SHT31
- **Weight**: <5g
- **Interface**: I2C, 1-Wire
- **Cost**: $5-25
- **Integration**: Arduino or Raspberry Pi companion

**Projects**:
- Altitude-temperature correlation study
- Microclimate mapping
- Weather data collection

#### Air Quality
**Sensors**: PMS5003, SDS011 (particulate), MQ-series (gas)
- **Weight**: 20-40g
- **Interface**: UART, analog
- **Cost**: $15-50
- **Power**: 5V, 100-200mA

**Projects**:
- Urban air quality mapping
- Pollution hotspot identification
- Environmental science integration
- Post-fire air quality assessment

#### Atmospheric Pressure
**Sensors**: BMP280, MS5611 (same as in flight controllers)
- **Weight**: <2g
- **Interface**: I2C, SPI
- **Cost**: $5-15

**Projects**:
- Altitude profile logging
- Weather system observation
- Pressure-altitude calculations (physics)

### Radiation Detection
**Sensors**: Geiger counter modules
- **Weight**: 50-100g
- **Interface**: Serial, pulse counting
- **Cost**: $80-200

**Safety Note**: For educational demonstration only, with appropriate supervision and radiation sources.

### GPS Data Logging
**Purpose**: Track flight path for analysis

**Options**:
- Built-in FC logging (ArduPilot, INAV)
- Separate GPS logger (higher sampling rate)
- Smartphone app (if phone mounted)

**Educational Use**:
- Analyze actual vs planned flight path
- Calculate speed, distance, efficiency
- GIS integration (import tracks into QGIS/ArcGIS)

## Delivery & Actuation Systems

### Servo Release Mechanisms

**Design**: Servo rotates to release payload

**Components**:
- Micro servo (9g): ~$3-5
- 3D printed release arm
- PWM signal from flight controller

**Integration**:
- Assign servo output in FC configuration
- Map to transmitter switch or autonomous trigger
- Test extensively before flight

**Educational Projects**:
- Precision drop challenges (land payload on target)
- Search and rescue supply delivery simulation
- Parachute deployment mechanisms
- Humanitarian aid scenario exercises

### Gripper Systems

**Design**: Servo or ESC-controlled claws

**Types**:
- **Passive Gripper**: Spring-loaded, servo releases
- **Active Gripper**: Servo opens and closes jaws

**Educational Projects**:
- Pick and place challenges
- Retrieve objects from ground
- Cooperative missions (multiple drones)

### Water/Powder Dispensers

**Purpose**: Firefighting simulation, seeding, sample delivery

**Design**:
- Reservoir (bottle, bag)
- Release valve (servo-actuated or pump)
- Weight consideration critical

**Safety**:
- Ensure liquid doesn't damage electronics
- Balance weight distribution
- Calculate impact on flight time

## Companion Computers

**Purpose**: Onboard processing for advanced payloads

### Raspberry Pi Integration

**Models for UAV Use**:
- **Raspberry Pi 4 (4GB)**: Best performance, ~100g
- **Raspberry Pi Zero 2 W**: Lightweight, ~20g, sufficient for many tasks

**Common Uses**:
- Computer vision (OpenCV)
- Data logging from multiple sensors
- Mission scripting (DroneKit for ArduPilot)
- Image processing (reduce data transmission)
- Machine learning inference

**Power Requirements**:
- Pi 4: 5V, 2-3A (use BEC or dedicated regulator)
- Pi Zero 2: 5V, 1A

**Communication with FC**:
- **Serial (UART)**: MAVLink for ArduPilot
- **USB**: Configuration and control
- **Network**: WiFi telemetry

**Educational Projects**:
- Autonomous marker detection and landing
- Object tracking (follow person/vehicle)
- Real-time image classification
- QR code scanning missions
- Collision avoidance with camera

### NVIDIA Jetson Nano

**Purpose**: High-performance computer vision and AI

**Specifications**:
- Weight: 100g (module only)
- Power: 5V, 2-4A (power-hungry)
- Performance: 472 GFLOPS

**Use Cases**:
- Deep learning inference (object detection)
- Real-time video processing
- Multi-sensor fusion
- Research projects

**Educational Level**: Advanced (college/university)

## Payload Integration Challenges

### Weight & Balance

**Weight Budget**:
1. Calculate max takeoff weight for platform
2. Subtract airframe + battery + electronics weight
3. Remaining capacity = payload budget

**Example**:
- Platform max weight: 1200g
- Frame + motors + FC + ESCs: 400g
- Battery (4S 1500mAh): 180g
- Remaining for payload: 620g

**Center of Gravity**:
- Payload should be mounted near CG (usually center, slightly forward)
- Heavy payloads mounted low (stability)
- Test hover before full flight (check balance)

### Power Management

**Payload Power Sources**:
1. **Flight Controller BEC**: Light sensors only (<500mA)
2. **Dedicated BEC/Regulator**: Cameras, Pi (~2-3A)
3. **Separate Battery**: Power-hungry payloads (Jetson, long missions)

**Voltage Considerations**:
- Most sensors: 3.3V or 5V
- Action cameras: Internal battery (no external power)
- Raspberry Pi: 5V ±5% (important!)
- Servos: 5-6V

**Wiring**:
- Use appropriate gauge for current
- Keep power wires short
- Add filtering capacitors for noisy payloads

### Mounting & Vibration

**Vibration Isolation**:
- Cameras: Soft-mount with rubber grommets
- Sensors: Depends on sensor type (some need rigid mount)
- Companion computers: Moderate isolation

**Mounting Methods**:
- 3D printed custom brackets
- Velcro straps (quick release)
- Zip ties (semi-permanent)
- Carbon fiber plates (rigid, professional)

**Design Considerations**:
- Aerodynamics (minimize drag)
- Prop clearance (nothing near spinning propellers)
- Accessibility (easy to swap batteries, SD cards)
- Crash protection (payload protected in crash)

### Data Management

**Recording Methods**:
1. **Onboard Storage**: SD card on camera/computer
2. **Telemetry**: Real-time transmission to ground station
3. **Hybrid**: Thumbnail/preview telemetry + full onboard recording

**Data Retrieval**:
- WiFi transfer (Raspberry Pi)
- Remove SD card post-flight
- USB cable connection

**Backup Strategy**:
- Always have extra SD cards
- Download data immediately after flight
- Multiple copies before deleting originals

## Educational Projects by Level

### Beginner (Middle School)

**Project 1: Basic Aerial Photography**
- Mount action camera (GoPro or similar)
- Record entire flight
- Create short video compilation
- **Skills**: Mounting, video editing, flight planning

**Project 2: GPS Track Logging**
- Use FC built-in GPS logging
- Export flight path
- Import into Google Earth
- **Skills**: GPS concepts, data export, GIS basics

### Intermediate (High School)

**Project 3: Environmental Sensor Payload**
- Arduino + BME280 sensor
- Log temperature, pressure, humidity vs altitude
- Create graphs in Excel/Python
- **Skills**: Arduino programming, sensor integration, data analysis

**Project 4: Precision Drop Challenge**
- Build servo release mechanism
- Program autonomous drop at waypoint
- Measure accuracy
- **Skills**: Mechanical design, servo control, autonomous missions

**Project 5: Thermal Imaging Survey**
- Mount FLIR One on smartphone
- Survey school building for heat loss
- Create thermal map
- **Skills**: Thermal imaging, energy audit, report writing

### Advanced (Post-Secondary)

**Project 6: Computer Vision Landing**
- Raspberry Pi + camera
- OpenCV marker detection
- Autonomous precision landing
- **Skills**: Python, OpenCV, DroneKit, autonomous control

**Project 7: Agricultural Multispectral Analysis**
- Multispectral camera payload
- Survey test plot
- Calculate NDVI (vegetation index)
- **Skills**: Agriculture tech, image processing, GIS analysis

**Project 8: Search and Rescue Simulation**
- Computer vision person detection
- Autonomous grid search pattern
- GPS logging of detections
- **Skills**: Advanced autonomy, AI/ML, mission planning

## Safety Considerations

### Weight Limits
- **FAA <250g Rule**: Stay under for registration exemption
- **Platform Limits**: Don't exceed max takeoff weight
- **Pilot Skill**: Heavier platforms harder to control

### Electrical Safety
- **Proper Isolation**: Avoid shorts between payload and flight electronics
- **Clean Power**: Filtered power for cameras (avoid noise in video)
- **Fusing**: Protect against payload shorts

### Drop Testing
- **Test All Release Mechanisms**: On ground first, low hover, then normal flight
- **Failure Modes**: What happens if servo fails? Design for safety
- **Drop Zone Safety**: Ensure clear area, no people below

### Privacy & Ethics
- **Camera Use**: Follow school/local policies on photography
- **Data Protection**: Blur faces in public footage
- **Permission**: Get consent before filming private property
- **Responsible Use**: Discuss ethical implications in class

## Payload Project Planning Worksheet

**Use this template for student projects**:

1. **Mission Objective**: What does the payload need to accomplish?
2. **Payload Selection**: What device(s) will you use?
3. **Weight Budget**: Calculate total weight, check platform capability
4. **Power Plan**: How will payload be powered? Calculate battery impact
5. **Mounting Design**: Sketch or CAD mounting solution
6. **Data Collection**: How will data be recorded/transmitted?
7. **Testing Plan**: Ground tests, hover tests, mission flights
8. **Safety Checks**: Identify risks, mitigation strategies
9. **Success Criteria**: How will you measure project success?

## Resources

### Hardware Suppliers
- **Adafruit**: Sensors, Raspberry Pi, educational kits
- **SparkFun**: Sensors, GPS modules, prototyping supplies
- **Amazon**: Action cameras, smartphone mounts
- **Thingiverse**: 3D printable mounts and mechanisms

### Software Tools
- **OpenCV**: Computer vision library
- **DroneKit**: Python API for ArduPilot control
- **QGIS**: Free GIS software for mapping projects
- **Agisoft Metashape**: Photogrammetry (free educational license)

### Example Code & Designs
- [Sensor Integration Code](../../code/raspberry-pi/sensor-examples/)
- [Payload Mount CAD Files](../../hardware/uav-designs/payload-mounts/)
- [Computer Vision Examples](../../code/raspberry-pi/opencv-examples/)

### Further Reading
- [Raspberry Pi Programming Guide](../programming/raspberry-pi-programming/)
- [Arduino Sensor Integration](../programming/arduino-programming/sensor-integration.md)
- [Setup & Configuration](../setup-configuration/)

---

**Back to**: [UAV Systems Overview →](index.md)
