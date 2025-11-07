# UAV Frame Designs

The frame is the structural foundation of your UAV. Understanding frame design principles is essential for building efficient, durable, and purpose-appropriate platforms.

## Frame Design Fundamentals

### Design Considerations

**Structural Requirements**
- **Rigidity**: Minimize flexing under motor thrust and vibration
- **Weight**: Balance between strength and flight time
- **Durability**: Withstand crashes and rough handling (especially in education)
- **Vibration Damping**: Reduce motor vibrations reaching flight controller

**Material Properties**
- **Carbon Fiber**: Lightweight, rigid, expensive (competition builds)
- **Fiberglass**: Moderate weight, good strength, budget-friendly
- **Plastic/ABS**: Heavy, flexible, very durable (educational builds)
- **Wood**: Easy to work with, moderate strength (DIY builds)
- **Aluminum**: Durable, conductive (requires isolation), heavy

## Quadcopter Configurations

### X-Frame Configuration
The most common educational and competition configuration.

```
    Motor 1 (CCW)      Motor 2 (CW)
         \                  /
          \                /
            \            /
              [FC/PDB]
            /            \
          /                \
         /                  \
    Motor 4 (CW)       Motor 3 (CCW)
```

**Advantages**:
- Symmetric flight characteristics
- Easy to repair (modular arms)
- Wide availability of parts
- Good stability

**Best For**: Educational platforms, racing, aerial photography

### Plus (+) Configuration

```
           Motor 1 (CW)
                |
                |
    Motor 4 --- [FC] --- Motor 2
     (CCW)      |          (CCW)
                |
           Motor 3 (CW)
```

**Advantages**:
- Clean forward/backward flight
- Simplified camera mounting (front is clear)
- Traditional orientation

**Best For**: FPV flight, forward-facing payload missions

### H-Frame Configuration
Extended center section for increased payload space.

**Advantages**:
- Large central mounting area
- Good payload capacity
- Separated electronics compartments

**Best For**: Research platforms, multiple sensors, camera gimbals

### Stretch-X Configuration
Elongated X-frame with longer rear arms.

**Advantages**:
- Increased rear space for battery/equipment
- Propellers out of camera view
- Better forward flight efficiency

**Best For**: Aerial photography, FPV cruising

## Size Classifications

### Micro Frames (<150mm diagonal)
- **Motor to Motor**: 65mm-150mm
- **Weight**: 20-80g
- **Props**: 2"-3.5"
- **Best For**: Indoor flight, learning basics, tight spaces
- **Examples**: Tiny Whoop class, micro racers

**Educational Benefits**:
- Safe for classroom use
- Low cost for crashes
- Builds understanding of basic physics
- No FAA registration required (<250g AUW)

### Educational Frames (150-300mm)
- **Motor to Motor**: 150-300mm
- **Weight**: 80-250g
- **Props**: 4"-7"
- **Best For**: Programming, autonomous flight, outdoor training
- **Examples**: 210mm racers, 250mm quads

**Educational Benefits**:
- Durable for repeated crashes
- Programming-capable flight controllers
- Outdoor flight capable
- Competition-ready size

### Standard Frames (300-550mm)
- **Motor to Motor**: 300-550mm
- **Weight**: 300g-1.5kg
- **Props**: 7"-13"
- **Best For**: Aerial photography, sensor payloads, advanced missions
- **Examples**: DJI F450, S500, custom builds

**Educational Benefits**:
- Significant payload capacity
- Longer flight times
- Professional equipment integration
- Research applications

## Fixed-Wing Frame Designs

### Traditional Trainer Design
Classic aircraft configuration with fuselage, wings, and tail.

**Components**:
- **Fuselage**: Houses electronics, battery, payload
- **Wing**: High-mounted for stability, dihedral for self-leveling
- **Tail**: Horizontal stabilizer and rudder for control
- **Landing Gear**: Tricycle or tail-dragger configuration

**Advantages**:
- Very stable flight
- Long flight times (30-60+ minutes)
- Easy to repair (foam construction)
- Teaches aerodynamic principles

**Best For**: Introduction to fixed-wing flight, long-range missions

### Flying Wing Design
Single-wing platform without traditional fuselage.

**Advantages**:
- Highly efficient (less drag)
- Simple construction
- Excellent for FPV
- Fast flight capability

**Challenges**:
- Less stable than trainers
- Requires more skill to fly
- Limited payload space

**Best For**: FPV cruising, fast mapping missions, advanced students

### VTOL Configurations

#### Quadplane Design
Fixed-wing with quadcopter motors for vertical takeoff.

**Advantages**:
- No runway required
- Long-range fixed-wing efficiency
- Multirotor hover capability

**Challenges**:
- Complex to build and program
- Higher cost
- Requires advanced ArduPilot configuration

**Best For**: Research projects, survey missions, advanced education

## Specialty Configurations

### Tricopter
Three motors with rear motor on tilt servo.

```
    Motor 1 (CW)       Motor 2 (CCW)
         \                  /
          \                /
            \            /
              [FC/PDB]
                 |
                 | (Tilt Servo)
                 |
            Motor 3 (CW)
```

**Advantages**:
- Excellent yaw authority
- Efficient design
- Unique educational value (mechanical + electrical control)

**Best For**: Advanced builds, demonstrating control theory

### Hexacopter & Octocopter
Six or eight motor configurations for increased payload and redundancy.

**Advantages**:
- Can lose one motor and still fly (with proper configuration)
- Increased payload capacity
- Smoother flight with less vibration

**Challenges**:
- Higher cost
- Increased complexity
- Shorter flight times (more motors)

**Best For**: Heavy payload missions, professional equipment

## Frame Selection Guide

### For Elementary/Middle School
**Recommended**: Micro or Small Quadcopter (X-Frame, plastic/durable ABS)
- Prioritize durability over performance
- Select frames with prop guards
- Choose readily available replacement arms
- Budget: $20-40 for frame kit

### For High School
**Recommended**: 210-250mm Quadcopter (X-Frame, carbon fiber or fiberglass)
- Balance durability with performance
- Competition-ready size
- Good parts availability
- Budget: $40-80 for frame kit

### For Post-Secondary/Research
**Recommended**: 450-550mm Quadcopter or Fixed-Wing platform
- Optimize for mission requirements
- Professional build quality
- Custom modifications possible
- Budget: $80-200+ for frame kit

## Frame Assembly Best Practices

### 1. Prepare Workspace
- Clean, organized assembly area
- Good lighting
- Small parts containers
- Tools organized and accessible

### 2. Dry-Fit Components
- Test fit all components before final assembly
- Plan wire routing paths
- Identify potential interference issues
- Mark mounting positions

### 3. Assembly Sequence
1. **Bottom Plate**: Attach arms to lower plate
2. **Electronics**: Mount PDB, ESCs (if underslung)
3. **Flight Controller**: Use vibration dampers, level orientation
4. **Top Plate**: Secure while managing wire routing
5. **Accessories**: Camera mounts, GPS mast, receiver antenna

### 4. Wire Management
- Use zip ties sparingly (allow for disassembly)
- Keep motor wires short but not taut
- Route ESC signal wires away from power wires
- Secure loose wires that could contact props

### 5. Center of Gravity
- Balance battery position for neutral CG
- Flight controller should be near CG
- Heavy components (battery, camera) as low as possible
- Test balance before first flight

## Frame Modifications

### Adding Prop Guards
Essential for indoor and beginner flights.

**Options**:
- 3D printed guards (custom fit)
- Commercial guard kits
- DIY wire/foam guards

### Landing Gear
Protect components during landing.

**Types**:
- Fixed legs (lightweight, simple)
- Spring-loaded legs (absorb impact)
- Retractable gear (expensive, advanced)

### Payload Mounts
- Camera gimbals (2-axis or 3-axis)
- Sensor pods (environmental, imaging)
- Custom 3D printed mounts
- GPS mast (elevated for clear signal)

## Common Frame Issues

### Vibration Problems
**Symptoms**: Jello in video, poor flight performance
**Solutions**:
- Add vibration dampers under flight controller
- Balance propellers
- Check for loose screws/arms
- Replace damaged motors

### Structural Damage
**Symptoms**: Cracks, bent arms, broken mounts
**Solutions**:
- Replace damaged arms immediately
- Reinforce high-stress areas with epoxy
- Keep spare arms in stock
- Consider more durable material

### Weight Issues
**Symptoms**: Short flight times, sluggish performance
**Solutions**:
- Review component weight vs necessity
- Use lighter battery if flight time adequate
- Remove unnecessary mounts/accessories
- Consider higher capacity battery if needed

## Frame Design Project Ideas

### Educational Activities

1. **Frame Comparison Study**: Build same components on different frame sizes, compare performance
2. **Material Testing**: Test different frame materials for strength/weight ratio
3. **Custom Frame Design**: Use CAD software to design custom frame, 3D print or laser cut
4. **Vibration Analysis**: Use flight controller logs to compare vibration on different frames
5. **Aerodynamics Experiment**: Test different arm angles, prop spacing, body shapes

## Resources

### Frame Manufacturers
- **GetFPV**, **Armattan**, **iFlight**: Quality racing/educational frames
- **Flite Test**: Foam fixed-wing kits, very educational
- **HobbyKing**: Budget-friendly frame options
- **Local Makerspaces**: Custom frame fabrication

### Design Tools
- **Fusion 360**: Free for education, full CAD capabilities
- **OnShape**: Web-based CAD, collaboration-friendly
- **eCalc**: Frame/propulsion calculator for design validation

### Documentation
- **CAD Files**: See [hardware/uav-designs/](../../hardware/uav-designs/)
- **Build Guides**: [Build Guides →](build-guides/)
- **Assembly Tips**: [Setup & Configuration →](../setup-configuration/)

---

**Next**: [Propulsion Systems →](propulsion-systems.md) | [Back to UAV Overview →](index.md)
