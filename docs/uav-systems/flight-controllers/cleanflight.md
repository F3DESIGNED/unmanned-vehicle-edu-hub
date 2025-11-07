# CleanFlight Flight Controller

CleanFlight is a simplified, lightweight flight controller firmware ideal for educational environments where simplicity and ease of setup are priorities.

## Overview

**CleanFlight** is the predecessor to Betaflight, offering a simplified feature set focused on stable flight without overwhelming configuration options.

### Key Features
- **Simplified Interface**: Fewer options, easier to learn
- **Stable & Reliable**: Mature codebase, well-tested
- **Low Resource Usage**: Runs well on older hardware (F1, F3 processors)
- **Self-Leveling Focus**: Emphasis on stable, educational flight
- **Standard Protocols**: Supports common receivers and ESCs

### Educational Strengths
- Easiest learning curve of racing-style firmwares
- Fewer settings to configure (less overwhelming for beginners)
- Stable defaults work well for most builds
- Good for younger students (middle school)
- Lower hardware requirements

### Limitations
- No active development (feature-complete, maintenance only)
- Missing modern features (DShot bidirectional, RPM filtering)
- Not suitable for racing or advanced FPV
- Smaller community than Betaflight
- Limited to older hardware targets

### When to Use CleanFlight
- **Elementary/Middle School** programs (simplicity priority)
- **Budget Constraints** (works on older, cheaper FCs)
- **Simple Stable Platforms** (educational demonstrations, basic flight training)
- **Simplified Curriculum** (want to avoid overwhelming students with options)

### When NOT to Use CleanFlight
- **Racing/FPV Focus**: Use Betaflight instead
- **GPS Navigation**: Use INAV or ArduPilot
- **Advanced Features Needed**: Modern FCs benefit from newer firmware
- **Latest Hardware**: New F7/H7 boards better supported in Betaflight

## Supported Hardware

### Compatible Flight Controllers

CleanFlight primarily supports older processor generations:

#### F1 Processors (Legacy)
- **Naze32**: Original CleanFlight target, still works
- **CC3D**: Common educational FC, limited features

**Note**: F1 support being phased out across all firmwares

#### F3 Processors
- **SP Racing F3**: Good CleanFlight support
- **Seriously Pro Racing F3**: Popular in 2015-2017
- **Various F3 boards**: Check CleanFlight target list

#### F4 Processors
- **Most F4 boards**: Good support, though Betaflight usually better choice
- **Omnibus F4**: Common, works well

### Recommendation

!!! note "Modern Alternative"
    For new builds, consider **Betaflight** instead. It supports all CleanFlight features plus modern improvements, with similar ease of use when using default settings.

    CleanFlight remains useful for existing builds on older hardware or when maximum simplicity is required.

## Installation & Setup

### CleanFlight Configurator

**Download**: [CleanFlight Configurator](https://github.com/cleanflight/cleanflight-configurator/releases)

Available for Windows, Mac, Linux (Chrome app).

**Note**: Interface similar to Betaflight/INAV configurators (same origins).

### Firmware Installation

1. **Connect FC via USB**
2. **Firmware Flasher** tab
3. **Select Board**: Choose your FC model from list
4. **Select Version**: Latest stable (2.5.0 as of final release)
5. **Flash Firmware**: Wait for completion
6. **Reconnect**: FC reboots with CleanFlight

### Initial Configuration

#### 1. Ports Tab
Assign peripherals to UART ports.

**Common Setup**:
- **UART1**: GPS (if used, though limited support)
- **UART2**: Receiver (SBUS, etc.)
- **MSP**: USB and/or UART for configuration

#### 2. Configuration Tab

**Mixer**:
- Select Quad X (most common) or appropriate configuration

**Features**:
- **RX_SERIAL**: Enable for SBUS/serial receivers
- **MOTOR_STOP**: Motors stop at zero throttle (safer for beginners)
- **SERVO_TILT**: For camera gimbals
- **SOFTSERIAL**: Software UART if hardware UARTs insufficient

**Board Alignment**:
- Set if FC not mounted flat (usually 0°,0°,0°)

**Receiver**:
- **RX Type**: Select PPM, SBUS, or other
- **RSSI Channel**: If receiver provides signal strength

#### 3. Receiver Tab

**Channel Map**: Usually AETR1234 (Aileron, Elevator, Throttle, Rudder)

**Channel Preview**:
- Move sticks and switches
- Verify all channels respond correctly
- Endpoints should be ~1000-2000

#### 4. Modes Tab

**ARM Mode**:
- Assign to switch (AUX 1 common)
- Set range to cover switch position

**ANGLE Mode**:
- Self-leveling mode (recommended for education)
- Can assign to switch, or leave always-on

**HORIZON Mode**:
- Optional: Allows flips while maintaining some leveling

**BARO Mode** (if barometer present):
- Altitude hold
- Requires calibration

#### 5. Adjustments Tab (Optional)
- PID tuning via transmitter channels
- Rate adjustments
- Mostly unused in educational contexts

#### 6. Calibration

**Accelerometer**:
1. Place quad level
2. Click "Calibrate Accelerometer"
3. Wait for completion

**Magnetometer** (if present):
- Less common on racing FCs
- Follow prompts if available

## Flight Modes

### ANGLE Mode (Recommended)
- **Description**: Self-leveling, sticks control tilt angle
- **Behavior**: Release sticks → returns to level
- **Best For**: All educational use, line-of-sight, beginners

### HORIZON Mode
- **Description**: Blended self-leveling and acro
- **Behavior**: Leveling near center, flips at extremes
- **Best For**: Transition to acrobatic flight

### ACRO Mode
- **Description**: Manual rate control, no leveling
- **Behavior**: Sticks control rotation rates only
- **Best For**: Advanced pilots, not recommended for education

### BARO Mode (If Available)
- **Description**: Barometric altitude hold
- **Behavior**: Maintains altitude automatically
- **Best For**: Stable hovering, easier flight

### Additional Modes
- **HEADFREE**: Directional lock (confusing for most, avoid)
- **BEEPER**: Activate lost model alarm
- **FAILSAFE**: Handled automatically, not a switch mode

## PID Tuning

CleanFlight includes simple PID tuning for flight characteristics.

### Default Tuning
- Works well for most educational platforms
- Start with defaults before making changes

### PID Tuning Tab

**Roll/Pitch/Yaw PIDs**:
- **P (Proportional)**: Strength of correction (higher = more aggressive)
- **I (Integral)**: Corrects persistent errors (wind, imbalance)
- **D (Derivative)**: Dampens oscillations

**Typical Starting Values**:
```
Roll:  P=40, I=30, D=23
Pitch: P=40, I=30, D=23
Yaw:   P=85, I=45, D=0
```

### When to Adjust

**Oscillations (shaking in flight)**:
- Reduce P by 10%
- Reduce D if high-frequency oscillation
- Test and repeat if needed

**Sluggish Response**:
- Increase P by 10%
- Increase D slightly
- Test and repeat

**Drifting**:
- Increase I slightly
- Check accelerometer calibration first

**For Education**:
- Slightly lower PIDs = safer, more forgiving
- Prioritize stability over performance

## Rates Configuration

Controls stick sensitivity and maximum rotation speed.

### Rate Settings

**RC Rate**: Overall sensitivity multiplier (0.90-1.20 typical)

**RC Expo**: Reduces sensitivity near center (0.30-0.50 typical)
- Higher expo = finer control at center
- 0 = linear response

**Rates**: Maximum rotation speed at full stick (600-800°/s for education)

### Recommended Educational Settings
```
RC Rate: 1.0
RC Expo: 0.40 (gentle center, progressive edges)
Roll/Pitch Rate: 600°/s (safe, not too fast)
Yaw Rate: 400°/s (slower yaw for orientation)
```

## ESC/Motor Configuration

### ESC Protocol

**Oneshot125**: Standard, works with most ESCs
**Multishot**: Faster, requires compatible ESCs
**PWM**: Legacy, slow, avoid if possible

**Recommendation**: Oneshot125 for educational builds

### Motor Direction

**Checking**:
1. Remove propellers
2. Motors tab → spin motors individually
3. Verify rotation direction matches diagram

**Correcting**:
- Swap any TWO motor wires to reverse direction
- CleanFlight doesn't support software direction reversal (DShot feature)

### ESC Calibration

Some ESCs require throttle range calibration:

1. Set throttle stick to maximum
2. Connect battery (ESCs beep)
3. Lower throttle to minimum (ESCs beep again)
4. Calibration complete

**Note**: Modern ESCs often don't require this

## Failsafe Configuration

Defines behavior when radio signal lost.

### Failsafe Stage 1
**Action when signal lost**:
- **Drop**: Cut throttle immediately (not recommended - prop strikes)
- **Land**: Descend slowly, disarm on ground (recommended)

### Failsafe Stage 2
**Extended signal loss**:
- Disarm after specified time at low throttle
- Prevents battery drain

### Procedure
1. Set throttle to desired failsafe position (typically low)
2. Set other channels to safe positions (centered usually)
3. Click "Save" in Failsafe tab

**Test Failsafe**:
- Arm quad (props off)
- Turn off transmitter
- Verify failsafe behavior

## Pre-Flight Checklist

### Configuration Verification
- [ ] Accelerometer calibrated
- [ ] Receiver channels responding correctly
- [ ] ARM switch assigned and working
- [ ] ANGLE mode enabled (for beginners)
- [ ] Failsafe configured and tested
- [ ] Motor directions verified (props off)

### Physical Inspection
- [ ] All screws tight (motors, arms, FC, battery)
- [ ] Propellers correct size and orientation
- [ ] Battery fully charged and secure
- [ ] No loose wires or exposed connections
- [ ] Radio transmitter charged and bound

### First Flight
- [ ] Open area, no obstacles
- [ ] Wind <10mph for first flight
- [ ] Spotter or instructor present
- [ ] Clear understanding of ARM/DISARM
- [ ] Know how to cut power (drop throttle)

## Basic Flight Training

### Flight Progression

**Stage 1: Ground Familiarization**
- Practice arming/disarming on ground
- Test throttle response (props off)
- Understand trim (should be minimal/none in CleanFlight)

**Stage 2: Hover Training**
- Takeoff to knee height
- Hover in place (ANGLE mode)
- Small stick inputs, smooth control
- Land gently

**Stage 3: Basic Translation**
- Hover, then move forward slowly
- Return to hover
- Repeat for backward, left, right

**Stage 4: Orientation**
- Fly in squares facing same direction
- Practice coordinated turns
- Build muscle memory

**Stage 5: Advanced**
- Figure-8 patterns
- Nose-in hover (facing pilot)
- Fly around obstacles

### Educational Flight Exercises

1. **Hover Duration**: How long can you hover within 1-meter box?
2. **Figure-8 Course**: Fly smooth figure-8 pattern
3. **Landing Precision**: Land on target pad
4. **Timed Course**: Fly through waypoint cones for time
5. **Emergency Procedures**: Practice failsafe (controlled)

## Troubleshooting

### Won't Arm

**"Arm switch in unsafe position"**
- Switch activated before powering on
- Solution: Power on first, then flip arm switch

**"Throttle too high"**
- Throttle stick not at zero
- Solution: Lower throttle stick fully

**"Angle too high"**
- Quad not level (exceeds max angle)
- Solution: Place on level surface

**"Calibration incomplete"**
- Accelerometer not calibrated
- Solution: Calibrate accelerometer

### Flight Issues

**Drifts to one side**
- Accelerometer calibration off
- Solution: Re-calibrate on level surface with battery connected

**Oscillations/bouncing**
- PIDs too high
- Props damaged or unbalanced
- Solution: Reduce PIDs by 10%, check props

**Sluggish response**
- PIDs too low
- Battery voltage low
- Solution: Increase PIDs slightly, check battery

**Motors getting hot**
- Props too large for motors
- Motors binding or damaged
- Solution: Check motor-prop pairing, test motors by hand

### Configurator Issues

**Can't connect**
- Wrong USB cable (needs data, not just power)
- Driver issues (install CP210x or STM VCP drivers)
- Wrong COM port selected

**Settings not saving**
- Must click "Save" button after changes
- Some settings require reboot to take effect

## Comparison to Other Firmwares

| Feature | CleanFlight | Betaflight | INAV | ArduPilot |
|---------|------------|-----------|------|-----------|
| **Ease of Use** | ★★★★★ | ★★★★☆ | ★★★☆☆ | ★★☆☆☆ |
| **Racing/FPV** | ★★☆☆☆ | ★★★★★ | ★★☆☆☆ | ★☆☆☆☆ |
| **GPS/Autonomy** | ☆☆☆☆☆ | ☆☆☆☆☆ | ★★★★☆ | ★★★★★ |
| **Education** | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★★☆ |
| **Active Development** | ☆☆☆☆☆ | ★★★★★ | ★★★★☆ | ★★★★★ |
| **Community** | ★★☆☆☆ | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| **Hardware Support** | ★★☆☆☆ | ★★★★★ | ★★★★☆ | ★★★★☆ |

### Migration Path

**From CleanFlight → Betaflight**:
- Same configurator interface
- All CleanFlight features present in Betaflight
- Can flash Betaflight over CleanFlight easily
- Settings may need minor adjustment

**Recommendation**: Start with CleanFlight for simplicity, migrate to Betaflight as students advance.

## Educational Activities

### Lab Projects

1. **PID Tuning Exercise**: Intentionally detune, feel the difference, restore to optimal
2. **Failsafe Testing**: Trigger failsafe in controlled environment, observe behavior
3. **Flight Time Optimization**: Test different batteries, props, weights - calculate efficiency
4. **Build Competition**: Identical parts, students build and fly, compare performance

### Flight Challenges

- **Precision Landing**: Target pad, score by accuracy
- **Timed Obstacle Course**: Fly through hoops/around cones
- **Endurance Contest**: Longest single-battery flight time
- **Relay Race**: Team passes object from takeoff to landing zone

### Classroom Integration

- **Physics**: Thrust, torque, forces in flight
- **Math**: Calculate flight time from battery capacity
- **Programming**: Introduce concept of control loops (PIDs)
- **Engineering Design**: Optimize frame/prop combinations

## Safety & Best Practices

### Safety Rules

1. **Propellers OFF** for all configuration and testing
2. **Clear flight area** - no people within 20 feet
3. **Eye protection** recommended for indoor flight
4. **ARM switch** always accessible to pilot
5. **Throttle down** before disarming

### Battery Safety
- Never leave charging unattended
- Use LiPo-safe bags or ammo cans
- Check for puffing/damage before each flight
- Store at 3.8V per cell for longevity
- See [Battery Safety Guide](../../safety-compliance/battery-safety.md)

### First-Flight Safety
- Instructor/experienced pilot supervises
- Open area with no obstacles
- Low altitude (2-3 meters maximum)
- ANGLE mode enabled
- Understand how to disarm quickly

## Resources

### Software Downloads
- [CleanFlight Configurator](https://github.com/cleanflight/cleanflight-configurator/releases)
- [CleanFlight Firmware](https://github.com/cleanflight/cleanflight/releases)

### Documentation
- [CleanFlight Docs](https://github.com/cleanflight/cleanflight/tree/master/docs)
- [RCGroups CleanFlight Forum](https://www.rcgroups.com/cleanflight-flight-controller-32) - Community support

### Transition Resources
- [Betaflight (Upgrade Path)](betaflight.md)
- [INAV (GPS Navigation)](inav.md)
- [ArduPilot (Full Autonomy)](ardupilot.md)

### Example Configurations
- [CleanFlight Basic Configs](../../../code/flight-controllers/cleanflight-configs/)

## Conclusion

CleanFlight serves as an excellent introduction to flight controller configuration for educational environments. Its simplified feature set reduces cognitive load for beginners while still providing stable, reliable flight.

**Best Use Cases**:
- Middle school drone programs
- First-time builders
- Budget-constrained programs
- Simple stable platforms
- Teaching basic flight and control concepts

**When to Graduate**:
- Students comfortable with basic concepts → Betaflight (advanced features)
- Need GPS navigation → INAV
- Research/autonomous projects → ArduPilot

---

**Back to**: [Flight Controllers Overview →](../index.md) | [UAV Systems →](../index.md)
