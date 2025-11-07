# UGV Chassis Designs

The chassis is the mechanical foundation of your UGV. Understanding different drive systems and chassis configurations is essential for selecting the right platform for your application.

## Drive System Types

### Differential Drive

**Description**: Two independently controlled wheels/tracks, plus casters for balance

**Advantages**:
- Simplest mechanically and programmatically
- Zero-radius turning (spin in place)
- Easy to control (left speed, right speed)
- Low cost

**Disadvantages**:
- Cannot move sideways
- Casters can catch on obstacles

**Best For**: Indoor robots, beginners, maze navigation, line following

**Example Platforms**: Arduino rovers, small educational robots

### Ackermann Steering

**Description**: Front wheels steer (like car), rear wheels drive

**Advantages**:
- Realistic vehicle dynamics
- Good for automotive education
- Smooth, predictable motion

**Disadvantages**:
- Cannot spin in place (larger turning radius)
- More complex mechanically (steering servo/motor)
- Drift can occur at high speeds

**Best For**: Autonomous vehicle education, outdoor navigation, RC car conversions

**Example Platforms**: RC car conversion, Donkey Car

### Mecanum Wheels

**Description**: Four wheels with angled rollers, allowing omnidirectional movement

**Advantages**:
- Moves forward, backward, sideways, diagonally
- Spin in place
- Precise positioning

**Disadvantages**:
- Expensive wheels
- Less traction (rollers slip easily)
- Complex inverse kinematics programming
- Indoor/smooth surface only

**Best For**: Warehouse robotics education, advanced projects, precise positioning tasks

### Tank/Tracked Drive

**Description**: Continuous tracks instead of wheels, differential steering

**Advantages**:
- Excellent traction
- Handles rough terrain, obstacles
- Stable platform

**Disadvantages**:
- Higher cost
- More complex mechanically (tracks, tensioners)
- Higher power consumption
- Slower than wheels

**Best For**: Outdoor rough terrain, obstacle crossing, durable platforms

### Rocker-Bogie (6-Wheel)

**Description**: Six wheels with passive suspension, no springs (Mars rover design)

**Advantages**:
- Climbs obstacles up to 2× wheel diameter
- Maintains ground contact on uneven terrain
- Stable, predictable
- Proven design (Mars rovers)

**Disadvantages**:
- Complex mechanical design
- Requires precision fabrication
- Slower speed
- Higher cost

**Best For**: Advanced builds, STEM demonstrations, Mars rover simulation, rough terrain

## Material Selection

### Chassis Materials

**Acrylic/Polycarbonate Plastic**:
- Pros: Easy to work with, laser-cuttable, inexpensive
- Cons: Brittle (acrylic), less rigid
- **Use**: Small indoor rovers, prototypes

**Aluminum**:
- Pros: Strong, lightweight, conductive (can be grounded)
- Cons: Requires metalworking tools, more expensive
- **Use**: Medium-outdoor rovers, durable builds

**Steel**:
- Pros: Very strong, cheap
- Cons: Heavy, requires welding/drilling tools
- **Use**: Large platforms, high payload

**3D Printed (PLA/PETG)**:
- Pros: Custom designs, complex shapes possible
- Cons: Time-consuming, limited strength, size constraints
- **Use**: Custom parts, small chassis, prototypes

**Foam Board/Cardboard**:
- Pros: Ultra-cheap, fast prototyping
- Cons: Not durable, indoor only
- **Use**: Rapid prototyping, disposable test platforms

## Sizing Guide

### Small (10-20cm footprint)
- **Motors**: N20 or similar micro gear motors
- **Battery**: 1S-2S LiPo (500-1000mAh) or AA batteries
- **Payload**: 100-300g
- **Speed**: Slow, indoor use
- **Cost**: $30-60
- **Use**: Desktop demos, classroom sets

### Medium (20-40cm)
- **Motors**: N20 high-torque or 25D motors
- **Battery**: 2S-3S LiPo (1500-3000mAh)
- **Payload**: 500g-1.5kg
- **Speed**: Moderate, indoor/outdoor
- **Cost**: $60-150
- **Use**: Educational projects, GPS navigation

### Large (40cm+)
- **Motors**: RS-385, RS-550, or brushless
- **Battery**: 3S-6S LiPo (3000-5000mAh) or 12V lead-acid
- **Payload**: 2-10kg
- **Speed**: Fast outdoor operation
- **Cost**: $150-400+
- **Use**: Payload delivery, outdoor autonomous, competitions

## Design Considerations

### Center of Gravity
- Keep CG low (battery and heavy components on bottom deck)
- CG should be centered between drive wheels
- Test by lifting: Should balance without tilting

### Ground Clearance
- Indoor smooth surface: 5-10mm sufficient
- Outdoor grass/gravel: 20-40mm recommended
- Rough terrain: 50mm+ with suspension

### Wheelbase & Track Width
- Longer wheelbase: More stable, larger turning radius
- Wider track: More stable (tip resistance), less maneuverable
- Rule of thumb: Track width ~70-90% of wheelbase

### Modularity
- Stackable decks (Arduino shields, custom PCBs)
- Removable battery (quick swaps)
- Accessible mounting holes
- Expandable sensor mounts

## Commercial Chassis Options

### Budget Platforms ($20-50)

**2WD/4WD Arduino Car Kits**:
- Acrylic chassis, N20 motors, battery holder
- Simple differential drive
- Good for Arduino learning
- Available: Amazon, AliExpress
- **Example**: "Arduino Smart Car Kit"

**RC Car Conversion**:
- Use old RC car as base ($10-30 secondhand)
- Replace RC receiver with Arduino/Pi
- Ackermann steering (realistic)
- Already durable, tested

### Mid-Range ($50-150)

**ROSbot 2.0 Chassis** ($80-120):
- Differential drive
- Designed for ROS
- Good build quality
- Expandable

**Wild Thumper 6WD** ($90-130):
- 6-wheel all-terrain chassis
- Large payload capacity
- Powerful motors included
- Rocker suspension

### Premium ($150-400)

**TurtleBot3 Burger/Waffle** ($300-500):
- Official ROS platform
- LiDAR-ready
- Excellent documentation
- Research-grade

**Custom CNC Aluminum**:
- Precision-cut chassis
- Design in CAD, order from service
- High strength-to-weight
- Expensive but professional

## DIY Chassis Building

### Laser-Cut Chassis

**Advantages**: Precise, professional, repeatable
**Tools Required**: Access to laser cutter (makerspace)
**Materials**: 3-5mm acrylic or plywood

**Process**:
1. Design in CAD (Fusion 360, OnShape)
2. Export DXF for laser cutting
3. Cut at makerspace or online service (Ponoko, SendCutSend)
4. Assemble with screws, standoffs

### 3D Printed Chassis

**Advantages**: Complex geometries, fully custom
**Limitations**: Size (printer bed), print time, strength

**Tips**:
- Design in sections (fit printer bed)
- Use PETG or ABS (stronger than PLA)
- Increase infill (30-50%) for structural parts
- Print motor mounts solid (100%)

### Scratch-Build (Hand Tools)

**Materials**: Foam board, cardboard, wood

**Process**:
1. Draw chassis outline on material
2. Cut with utility knife or saw
3. Hot glue or wood glue assembly
4. Reinforce with tape/wood strips
5. Mount components with hot glue, zip ties

**Pros**: Fastest prototyping, ultra-cheap
**Cons**: Not durable, not precise

## Example Chassis Specifications

### Educational Arduino Rover
- **Type**: Differential drive, 2WD
- **Size**: 15cm × 12cm
- **Material**: Acrylic
- **Motors**: N20 6V gear motors (150 RPM)
- **Wheels**: 65mm diameter rubber
- **Battery**: 2S LiPo 1000mAh or 6× AA
- **Payload**: Arduino Uno, motor driver, ultrasonic sensor, breadboard
- **Cost**: $40-60

### GPS Autonomous Rover
- **Type**: Differential drive, 4WD
- **Size**: 30cm × 25cm
- **Material**: Aluminum or thick acrylic
- **Motors**: 25D 12V gear motors (100 RPM)
- **Wheels**: 100mm diameter rubber with tread
- **Battery**: 3S LiPo 2200mAh
- **Payload**: Raspberry Pi 4, GPS, compass, IMU, camera
- **Cost**: $120-200

### Rocker-Bogie Mars Rover Replica
- **Type**: 6-wheel rocker-bogie
- **Size**: 50cm × 40cm
- **Material**: Aluminum extrusion + 3D printed joints
- **Motors**: RS-385 12V w/ encoders (6×)
- **Wheels**: 120mm diameter with foam tires
- **Battery**: 4S LiPo 5000mAh or 12V SLA
- **Payload**: Pixhawk, GPS, cameras, robotic arm
- **Cost**: $300-500

## Resources

### CAD Files & Designs
- [UGV Chassis CAD Library](../../hardware/ugv-designs/)
- [Thingiverse UGV Collection](https://www.thingiverse.com/search?q=rover+chassis)
- [OnShape CAD Templates](https://cad.onshape.com/)

### Build Guides
- [Basic Arduino Rover Build →](build-guides/basic-arduino-rover.md)
- [Pi Autonomous Navigator →](build-guides/pi-autonomous-navigator.md)
- [Advanced ROS Platform →](build-guides/advanced-ros-platform.md)

### Vendors
- **Pololu**: High-quality robot chassis and parts
- **ServoCity/Actobotics**: Modular building system
- **GoBilda**: Excellent educational robotics system
- **OpenBuilds**: Aluminum extrusion systems

---

**Next**: [Propulsion & Steering →](propulsion-steering.md) | [Back to UGV Overview →](index.md)
