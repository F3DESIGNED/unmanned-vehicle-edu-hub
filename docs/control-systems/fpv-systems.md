# First-Person View (FPV) Systems

First-Person View systems provide real-time video feedback from onboard cameras, allowing pilots to fly as if they were sitting in the cockpit. This technology enables beyond-line-of-sight operation, precision flying, and immersive experiences.

## FPV System Overview

An FPV system consists of four main components:

```mermaid
graph LR
    A[Camera] --> B[Video Transmitter]
    B -->|Radio Signal| C[Video Receiver]
    C --> D[Display Device]
    D --> E[Pilot]
```

### Component Breakdown

1. **Camera**: Captures live video
2. **Video Transmitter (VTx)**: Broadcasts video signal
3. **Video Receiver (VRx)**: Receives video signal
4. **Display**: Shows video (goggles or monitor)

## Camera Systems

### Camera Types

#### Analog FPV Cameras
**Characteristics:**

- Low latency (~20-40ms)
- Works in any lighting
- Affordable ($10-50)
- Standard resolution (600-1200 TVL)

**Popular Models:**

- **Caddx Ratel 2**: Excellent low-light, 1200TVL, $30
- **Foxeer Razer Mini**: Compact, good color, 1200TVL, $25
- **RunCam Phoenix 2**: Budget-friendly, 1000TVL, $20

#### HD Digital Systems
**Characteristics:**

- Higher latency (~50-70ms)
- Superior image quality
- More expensive ($180+ for system)
- Limited by system ecosystem

**Systems:**

- **DJI FPV System**: Best quality, proprietary, $130-180
- **HDZero**: Low latency digital, $200 system
- **Walksnail**: Budget digital option, $150 system

!!! tip "Educational Recommendation"
    Start with analog FPV systems. Lower cost allows equipping more students, and minimal latency is better for developing flying skills.

### Camera Specifications

#### Field of View (FOV)
- **Narrow (60-80°)**: Less distortion, long-range
- **Medium (90-120°)**: Balanced, most popular
- **Wide (140-170°)**: Immersive, better spatial awareness

**Educational Setting:** 90-120° provides good compromise

#### Image Sensor
- **CCD**: Better color, higher cost (obsolete)
- **CMOS**: Modern standard, good performance

#### Aspect Ratio
- **4:3**: Traditional FPV, better vertical view
- **16:9**: Widescreen, more cinematic

### Camera Mounting

**Tilt Angle:**
- **0-15°**: Slow, cinematic flying
- **15-30°**: General purpose, learning
- **30-45°**: Racing, aggressive flying

**Protection:**
- Case or mounting plate
- Secure with rubber dampening
- Protect lens from props

## Video Transmission

### Frequency Bands

#### 5.8 GHz (Most Common)
**Advantages:**

- Legal worldwide (check local power limits)
- Many channel options
- Compact antennas
- Good penetration

**Disadvantages:**

- Shorter range than lower frequencies
- Interference from WiFi

**Channels:**
- 40 channels across 5 bands (A, B, E, F, R)
- Use channel chart to avoid interference in group flights

#### 2.4 GHz
**Status:** Largely obsolete for FPV

- Conflicts with RC transmitters
- Limited availability

#### 1.3 GHz
**Advantages:**

- Longer range
- Better obstacle penetration

**Disadvantages:**

- Larger antennas
- May require license
- Less common

!!! warning "Regulatory Compliance"
    Check your country's regulations on frequency and power limits:
    - **USA**: FCC Part 15, max 25mW for unlicensed 5.8GHz
    - **EU**: ETSI EN 300 328, max 25mW
    - **Education**: Stay at 25mW or below to avoid licensing

### Power Levels

| Power | Range | Use Case | License Required |
|-------|-------|----------|------------------|
| 25mW | 100-300m | Indoor, short range | No |
| 200mW | 500m-1km | Outdoor flying | Varies by region |
| 600mW | 1-2km | Long range | Usually yes |
| 1W+ | 2km+ | Extreme range | Yes |

**Educational Recommendation:** 25mW for indoor, 200mW maximum for outdoor

### Video Transmitter Setup

#### VTx Configuration

**Important Settings:**

- **Power**: Start low, increase only if needed
- **Channel**: Check for conflicts before flying
- **Smart Audio/IRC Tramp**: Configuration via OSD
- **Pit Mode**: Low power mode for bench testing

#### Common VTx Models

- **TBS Unify Pro**: Reliable, SmartAudio, ~$25
- **Rush Tank**: Good value, IRC Tramp, ~$18
- **ImmersionRC Tramp HV**: High performance, ~$30

### Antennas

#### Antenna Types

**Linear (Dipole)**
- Lightweight
- Directional
- Good for racing
- Lower range

**Circular Polarized (CP)**
- Omni-directional
- Better range
- Reduces multipathing
- Heavier

**Patch/Directional**
- Long range
- Must aim at vehicle
- Ground station use
- Not for mobile pilot

#### Antenna Polarization

**RHCP (Right-Hand Circular Polarized)**: Standard in FPV
**LHCP (Left-Hand Circular Polarized)**: Alternative

!!! danger "Match Polarization"
    Transmitter and receiver antennas must use the same polarization (both RHCP or both LHCP). Mismatched polarization causes severe signal loss.

#### Popular Antennas

- **Pagoda**: DIY-friendly, good performance
- **Triumph**: Stubby, durable
- **Lollipop**: Compact, resilient

## Display Devices

### FPV Goggles

#### Box Goggles
**Characteristics:**

- Lower cost ($50-200)
- Can wear glasses underneath
- Less immersive
- Heavier

**Popular Models:**

- **Eachine EV800D**: Budget, built-in battery/DVR, $80
- **Skyzone SKY02X**: Mid-range, good optics, $200

#### Compact Goggles
**Characteristics:**

- More expensive ($300-600)
- Highly immersive
- Lighter weight
- Better optics

**Popular Models:**

- **Fatshark Attitude V6**: Classic design, $400
- **Skyzone Cobra X**: High-end features, $500
- **DJI Goggles 2**: Digital only, $600

#### Goggle Features to Consider

- **Diversity**: Multiple receivers for better signal
- **DVR**: Records video to SD card
- **Battery**: Internal vs external
- **IPD Adjustment**: Fits different face sizes
- **Diopter Adjustment**: For vision correction

### FPV Monitors

**Advantages:**

- Better for groups/teaching
- No face fatigue
- Easier setup
- Share experience

**Disadvantages:**

- Less immersive
- Harder to use in bright sunlight
- Requires mount/stand

**Recommended for Education:**
- 7" LCD monitor with diversity receiver
- Good for demonstrations and group training
- Students take turns with goggles

## Complete FPV System Setup

### Budget Educational System ($150)
```
Camera: RunCam Phoenix 2 ($20)
VTx: Rush Tank ($18)
Antennas: Pagoda set ($12)
Goggles: Eachine EV800D ($80)
Extras: Cables, mounts ($20)
```

### Mid-Range System ($400)
```
Camera: Caddx Ratel 2 ($30)
VTx: TBS Unify Pro ($25)
Antennas: Triumph set ($20)
Goggles: Skyzone SKY02X ($200)
Ground Station: 7" Monitor ($80)
Accessories: Batteries, mounts ($45)
```

### Advanced System ($800+)
```
Camera: DJI O3 Air Unit ($230)
Goggles: DJI Goggles 2 ($600)
Accessories: Extra batteries ($50)
Ground Station: Monitor with DVR ($150)
```

## FPV Flying Techniques

### Getting Started

#### First FPV Flight Checklist

1. **Verify channel**: No conflicts with others
2. **Check video**: Clear picture on ground
3. **Confirm controls**: Remove goggles quickly if needed
4. **Have spotter**: Safety observer required
5. **Start in open area**: No obstacles

#### Progressive Training

**Phase 1: Monitor First**
- Fly line-of-sight with monitor showing FPV view
- Build mental model of camera perspective
- Practice referencing monitor while maintaining LOS

**Phase 2: Goggle Assisted**
- Wear goggles but keep them raised
- Drop goggles for brief periods
- Spotter provides verbal guidance

**Phase 3: Full FPV**
- Extended goggle time in open area
- Spotter watches vehicle
- Gradually increase complexity

### Common FPV Maneuvers

#### Orientation Recovery
If disoriented:
1. Climb (throttle up)
2. Level (center sticks)
3. Check surroundings in video
4. Identify horizon line
5. Make slow, deliberate movements

#### Flying Through Gates/Obstacles
1. Approach aligned
2. Note gap size in video
3. Commit to path
4. Don't over-correct mid-gap
5. Exit clean

#### Low-Altitude Flying
1. Reference ground texture
2. Maintain consistent speed
3. Anticipate obstacles earlier
4. Use audio cues from motors

## Video Interference

### Sources of Interference

- **WiFi networks**: 2.4 GHz and 5 GHz
- **Other FPV pilots**: Nearby on same channel
- **Power lines**: Strong EMI
- **Cell towers**: Broadband interference
- **Metal structures**: Reflections and multipathing

### Reducing Interference

1. **Channel Selection**: Use frequency analyzer to find clean channels
2. **Antenna Position**: Keep VTx and VRx antennas apart, proper orientation
3. **Power Management**: Use appropriate VTx power for distance
4. **Shielding**: Keep VTx away from electrical noise sources
5. **Location**: Fly away from interference sources

### Troubleshooting Poor Video

| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Static/snow | Weak signal | Increase power, check antennas |
| Horizontal lines | Electrical noise | Check power filtering, move VTx |
| Black/white bands | Other pilot same channel | Change channels |
| Flickering | Loose connection | Check all connections |
| Total loss | No power or wrong channel | Verify VTx powered, check channel |

## Safety Considerations

### FPV-Specific Safety Rules

!!! danger "Critical Safety Requirements"
    1. **Spotter Required**: Always have a spotter watching the vehicle visually
    2. **Communication**: Establish clear verbal commands with spotter
    3. **Altitude Awareness**: Easy to lose height reference in FPV
    4. **Battery Monitoring**: Check voltage via OSD regularly
    5. **Failsafe Configured**: Set RTL or land on signal loss

### Legal Requirements

**FAA Part 107 (USA) for FPV:**
- Visual observer required for FPV flight
- Pilot must be able to see vehicle with visual observer
- Maximum altitude 400 feet AGL
- Maintain situational awareness

**Educational Exemptions:**
- Check if special rules apply to educational institutions
- Some areas have designated flying fields with different rules
- Always file LAANC requests for controlled airspace

### Common FPV Hazards

1. **Disorientation**: Loss of spatial awareness
2. **Target Fixation**: Focusing only on video, missing other dangers
3. **Altitude Misjudgment**: Ground rush happens fast
4. **Battery Depletion**: Video continues after flight time exhausted
5. **Signal Loss**: Range limits or interference

## FPV for Different Applications

### Racing
- High camera tilt (30-40°)
- Wide FOV camera
- Low latency critical
- Practice gates and timing

### Freestyle
- Medium camera tilt (25-35°)
- Balanced FOV
- Smooth video for tricks
- Focus on flow

### Cinematic
- Low camera tilt (0-15°)
- Narrow FOV for less distortion
- Stable flying priority
- Often use HD system

### Education
- Medium tilt (15-25°)
- Standard FOV (90-120°)
- Analog for reliability
- DVR for review/grading

## OSD (On-Screen Display)

### Essential OSD Elements

- **Battery Voltage**: Critical for safety
- **Flight Time**: Remaining time estimate
- **RSSI**: Signal strength
- **Flight Mode**: Current mode indicator
- **Throttle**: Current throttle position
- **Altitude**: Height above takeoff
- **Artificial Horizon**: Orientation reference

### OSD Configuration

Configure through flight controller software (Betaflight, INAV, ArduPilot):

1. Connect via USB
2. Access OSD tab
3. Drag elements to desired positions
4. Configure warnings (voltage, RSSI)
5. Test on bench with video feed

**Recommended Layout for Education:**
```
[Battery] [Flight Time]        [RSSI]
[Flight Mode]

         [Artificial Horizon]

[Altitude]               [Throttle %]
```

## Learning Activities

### Activity 1: FPV System Assembly
**Duration:** 2 hours
**Objectives:** Understand component connections, signal flow
**Materials:** FPV camera, VTx, goggles, power source, cables

1. Identify components and cables
2. Wire camera to VTx
3. Connect to power
4. Power on and tune receiver
5. Test different channels
6. Document with photos

### Activity 2: FPV Simulator Training
**Duration:** 5+ hours over multiple sessions
**Objectives:** Build FPV flying skills without risk
**Materials:** FPV simulator, transmitter

Recommended simulators:
- **Liftoff**: Realistic physics, multiplayer
- **DRL Sim**: Professional tracks
- **Velocidrone**: Best for racing
- **FPV Freerider**: Budget-friendly

### Activity 3: Antenna Range Testing
**Duration:** 1 hour
**Objectives:** Understand impact of antenna choice and orientation
**Materials:** Complete FPV system, range test equipment

1. Set VTx to 25mW
2. Walk away while monitoring RSSI
3. Test different antenna orientations
4. Compare different antenna types
5. Plot range vs. RSSI graph

## Assessment Rubric

| Skill | Novice | Developing | Proficient | Expert |
|-------|--------|-----------|-----------|--------|
| FPV Setup | Needs help wiring | Connects with reference | Independent setup | Troubleshoots issues |
| Channel Selection | Doesn't check | Selects randomly | Checks for conflicts | Uses analyzer |
| FPV Orientation | Gets disoriented | Recovers slowly | Good awareness | Instinctive |
| Video Quality | Ignores problems | Notices issues | Troubleshoots | Optimizes system |

## Maintenance and Care

### Regular Maintenance

- **Antenna Inspection**: Check for damage, secure connections
- **Camera Cleaning**: Keep lens clean, check mounting
- **Solder Joints**: Inspect for cracks, re-solder if needed
- **Goggle Maintenance**: Clean lenses, check foam padding
- **Cable Management**: Secure wires, prevent chafing

### Common Failures and Solutions

| Issue | Cause | Prevention |
|-------|-------|------------|
| Broken antenna | Crash damage | Use flexible mount |
| Burnt VTx | No antenna connected | Always connect antenna first |
| Blown camera | Voltage spike | Use filtered power, capacitor |
| Foggy lens | Moisture/temperature | Use anti-fog, let acclimate |

## Next Steps

- Explore [Autonomous Control](autonomous-control.md) for mission-based flying
- Learn [Advanced Control](advanced-control.md) for optimizing PID tuning
- Review [Troubleshooting](../troubleshooting/hardware-issues.md) for common FPV problems

## Additional Resources

- **ImmersionRC**: FPV equipment and guides
- **GetFPV.com**: Educational resources and product guides
- **Joshua Bardwell YouTube**: Comprehensive FPV tutorials
- **Oscar Liang Blog**: Technical FPV information and reviews
