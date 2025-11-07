# Betaflight Flight Controller

Betaflight is the leading firmware for FPV racing and acrobatic flight, offering exceptional manual flight performance and extensive tuning capabilities.

## Overview

**Betaflight** is optimized for responsive manual control, FPV racing, and freestyle acrobatics. It's the de facto standard in the racing drone community.

### Key Features
- **Fastest Loop Times**: 8kHz+ gyro sampling, sub-millisecond latency
- **Advanced Filtering**: Bidirectional DShot, dynamic filtering, RPM filters
- **OSD (On-Screen Display)**: Real-time flight telemetry in FPV goggles
- **Blackbox Logging**: High-resolution flight data for analysis
- **LUA Scripts**: Custom functions on OpenTX/EdgeTX radios
- **Extensive Tuning**: Slider-based tuning, presets for different styles

### Educational Strengths
- Excellent for teaching manual flight skills
- Great FPV integration (immersive learning)
- Strong community support and tutorials
- Lower cost than autonomous platforms
- Teaches PID tuning and control theory

### Challenges
- Limited autonomous capabilities (no waypoint missions)
- Requires manual piloting skill
- Less suitable for sensor integration
- Not ideal for mapping/survey applications

## Supported Hardware

### Flight Controllers

Most modern F4, F7, and H7 flight controllers support Betaflight.

#### Entry-Level (F4 Processors)
- **Matek F405-STD/CTR**: Full-featured, affordable ($30-40)
- **Holybro Kakute F4**: Integrated OSD, current sensor ($35-45)
- **MAMBA F405**: Popular stack with ESC ($50-70)

**Best For**: Budget builds, learning, classroom sets

#### Mid-Range (F7 Processors)
- **Matek F722**: Excellent sensor suite, SD card ($40-50)
- **SpeedyBee F7 V3**: Popular, WiFi app configuration ($45-55)
- **Holybro Kakute F7**: Well-supported, compact ($50-60)

**Best For**: Most educational builds, good performance-to-cost ratio

#### High-Performance (H7 Processors)
- **Matek H743**: Fastest processing, best filtering ($60-80)
- **SpeedyBee F7 V3 H7**: Top-end features ($70-90)

**Best For**: Advanced racing, high-refresh FPV systems

### Recommended Stacks (FC + 4-in-1 ESC)
- **iFlight SucceX-E F4/F7**: Complete stack, good value ($60-90)
- **Holybro Tekko32 + Kakute**: Quality stack ($80-110)
- **GEPRC Stack**: Ready-to-fly stacks ($70-100)

## Installation & Setup

### Betaflight Configurator

**Download**: [Betaflight Configurator](https://github.com/betaflight/betaflight-configurator/releases)

Available for Windows, Mac, Linux, and as Chrome app.

### Firmware Installation

1. **Connect FC via USB**
2. **Configurator** → **Firmware Flasher** tab
3. **Select Board**: Auto-detect or choose manually
4. **Select Version**: Latest stable (4.4+ as of 2024)
5. **Flash Firmware**: Wait for completion
6. **Disconnect/Reconnect**: FC will reboot with new firmware

**Tips**:
- Use "Full Chip Erase" for clean install
- Select appropriate target for your FC model
- Keep configurator updated

### Initial Setup Wizard

Modern Betaflight includes a setup wizard for beginners.

#### 1. Board Alignment
- Ensure FC mounted level to frame
- If not, set custom alignment angles
- Most builds: all 0° (default)

#### 2. Receiver Type
- **Serial (SBUS/CRSF)**: Most common modern receivers
- **PPM**: Older receivers, single wire
- **MSP**: Rare, special cases

**SBUS Setup** (Most Common):
- Connect receiver SBUS wire to TX pad on FC (counterintuitively)
- Set receiver protocol to "Serial-based receiver"
- Select UART matching your connection
- Protocol: SBUS or CRSF (for TBS Crossfire/ELRS)

#### 3. Motor Direction
- Verify motor spin direction
- Props OFF for safety
- Motors should spin in correct direction for selected configuration

**Change Direction**:
- Enable "Motor Direction is Reversed" for affected motors (BLHeli_32/DShot only)
- OR swap any two motor wires

#### 4. ESC Protocol
- **DShot600**: Recommended for most builds
- **DShot300**: Slower, but very reliable
- **DShot150**: Compatibility mode
- **Multishot/Oneshot**: Legacy, avoid if possible

**Bidirectional DShot**:
- Enable if ESCs support it (BLHeli_32 required)
- Allows RPM filtering (significant noise reduction)
- Check ESC specs for support

#### 5. Flight Modes
Configure switch positions for different modes.

**Recommended Educational Setup**:
- **No switches**: Angle mode always (safest for beginners)
- **1 switch**: Angle ↔ Horizon mode
- **2 switches**: Angle ↔ Horizon ↔ Acro (progression)
- **Advanced**: Add Air Mode, Flip Over After Crash, Turtle Mode

## Flight Modes

### Angle Mode (Self-Leveling)
- FC maintains level orientation
- Sticks control tilt angle (max angle settable)
- Releases sticks → returns to level
- **Best For**: Beginners, line-of-sight flight, stable video

### Horizon Mode (Semi-Acro)
- Self-leveling with center sticks
- Allows flips/rolls with full stick deflection
- Blend of Angle and Acro
- **Best For**: Transition to acrobatic flight

### Acro Mode (Rate/Manual)
- No self-leveling, full manual control
- Sticks control rotation rates
- Industry standard for racing/freestyle
- **Best For**: FPV flight, racing, advanced pilots

### Air Mode
- Maintains motor authority at zero throttle
- Allows control during descents and flips
- Enable for racing/freestyle, disable for training

### Turtle Mode (Flip Over After Crash)
- Reverses motors to flip upside-down quad
- Requires DShot ESC protocol
- Saves walking to crashed drone

## Configuration Tabs

### Ports Tab
Configure UART assignments for peripherals.

**Common Assignments**:
- **UART1**: GPS (if used)
- **UART2**: Receiver (SBUS/CRSF)
- **UART3**: VTX control (SmartAudio/Tramp)
- **UART4**: ESC Telemetry
- **UART6**: External logging device

### Configuration Tab

#### System Configuration
- **Gyro Update Frequency**: 8kHz (F7/H7), 4kHz (F4)
- **PID Loop Frequency**: 4kHz typical
- **Motor PWM Protocol**: DShot600
- **Motor Poles**: 14 (check your motor specs)

#### Board & Sensor Alignment
- Set board orientation if FC not mounted flat
- Enable/disable sensors (Barometer usually off for racing)

#### Receiver
- Set receiver protocol (SBUS, CRSF, etc.)
- Stick deadband: 3-5 typical

#### Arming
- **Maximum Arm Angle**: 25° (prevents arming on uneven surface)
- **Disarm Kill Switch**: Optional safety feature

### Failsafe Tab
Configure behavior when signal lost.

**Stage 1: Initial Action**
- **Drop**: Cut throttle immediately (can damage props on landing)
- **Landing**: Descend slowly, disarm on ground (recommended)
- **GPS Return Home**: Requires GPS and INAV/ArduPilot

**Stage 2: Settings**
- **Guard Time**: Delay before failsafe (300ms typical)
- **Throttle Low Delay**: Time at low throttle before disarm (10s)

**Procedure**: Set sticks to desired failsafe positions, click "Set" button

### PID Tuning Tab
Adjust flight characteristics.

#### Tuning Sliders (Easy Mode)
- **Master Multiplier**: Overall PID strength
- **PD Balance**: More D for smooth, less D for responsive
- **Roll/Pitch Ratio**: Usually equal, adjust for asymmetric builds
- **Filtering**: Lower for smoother, higher for more responsive (with more noise)

**Presets**:
- **Tune**: Race, Freestyle, Cinematic, HD Freestyle
- Start with preset matching your goal

#### Advanced PID Tuning
Manual PID value adjustment for experts.

**P (Proportional)**: Strength of correction
- Too low: Sluggish, drifts
- Too high: Oscillations

**I (Integral)**: Correction of sustained errors
- Too low: Drift in wind, won't hold attitude
- Too high: Slow oscillations, "wobble of death"

**D (Derivative)**: Dampening, reduces overshooting
- Too low: Overshoots, bounces back
- Too high: Feels "locked in", motor heat

### Receiver Tab
Map transmitter channels to flight controller functions.

**Standard Mapping** (Mode 2 transmitter):
- **Roll**: Aileron (channel 1)
- **Pitch**: Elevator (channel 2)
- **Throttle**: Throttle (channel 3)
- **Yaw**: Rudder (channel 4)
- **AUX1-4**: Switches for modes, arming, etc.

**Calibration**:
- Move sticks to verify channel response
- Reverse channels if needed
- Set midpoint and endpoints

### Modes Tab
Assign flight modes and functions to switches.

**Essential Modes**:
- **ARM**: Dedicated switch recommended (AUX1 common)
- **ANGLE**: Self-leveling mode
- **HORIZON**: Semi-acro mode
- **AIR MODE**: For racing/freestyle

**Optional Modes**:
- **BEEPER**: Lost model alarm
- **FLIP OVER AFTER CRASH**: Turtle mode
- **PREARM**: Extra safety, must enable before arming

**Range Setup**:
- Move switch to desired positions
- Click range bar to set activation range
- Multiple ranges per mode possible (not usually needed)

### Motors Tab
Test motor operation.

!!! danger "Safety Critical"
    **REMOVE PROPELLERS** before testing motors in configurator!

**Motor Order** (Betaflight Standard):
```
  Motor 1 (rear-right)     Motor 2 (front-right)
           \                  /
            \                /
              [Flight Controller]
            /                \
           /                  \
  Motor 3 (rear-left)      Motor 4 (front-left)
```

**Testing**:
1. Enable "Motor Test Mode" (requires props removed)
2. Slowly raise sliders to test individual motors
3. Verify motor direction and order
4. If wrong, adjust wiring or enable motor direction reversal

### OSD Tab
Configure on-screen display for FPV goggles.

**Recommended Elements**:
- **Battery Voltage**: Critical for safety
- **Timer**: Track flight time
- **Warnings**: Low voltage, disarmed, etc.
- **Artificial Horizon**: Orientation reference
- **Throttle Position**: Current power output
- **RSSI/Link Quality**: Radio signal strength

**Positioning**:
- Drag elements to desired screen location
- Use different profiles for different conditions

### Blackbox Tab
High-resolution flight data logging.

**Enable Logging**:
- Set "Device": SD Card (if available) or Flash
- Set "Sample Rate**: 1kHz typical (higher for advanced tuning)
- Logs saved to onboard storage

**Analysis**:
- Download logs via Configurator
- Open in Blackbox Explorer (included with configurator)
- Analyze vibration, PID performance, motor issues

## Pre-Flight Setup

### 1. Accelerometer Calibration
**Setup** → **Calibration** → **Calibrate Accelerometer**
- Place quad on level surface
- Ensure battery connected
- Click "Calibrate"
- Do not move until complete

### 2. Receiver Setup
**Receiver Tab** → Test all channels respond correctly
- Full stick deflection reaches 1000-2000μs
- Center is ~1500μs
- No channel reversals needed (do this on transmitter)

### 3. Mode Setup
**Modes Tab** → Configure at minimum:
- ARM on dedicated switch
- ANGLE mode for beginners
- Ensure modes activate correctly as you flip switches

### 4. ESC Calibration (If Needed)
Some ESCs require calibration for full throttle range:
1. Remove props
2. Full throttle stick, connect battery (ESCs beep)
3. Lower throttle to zero (ESCs beep confirmation)

**Note**: Many modern ESCs don't require calibration

### 5. Motor Direction Check
1. **Motors Tab** → Enable motor test, props OFF
2. Verify correct spin direction per diagram
3. Correct if needed (swap wires or enable reversal)

## CLI (Command Line Interface)

Advanced configuration via text commands.

**Access**: Click "CLI" tab in Configurator

### Common Commands

**View Settings**:
```
dump                    # Show all settings
dump profile            # Show current profile settings
diff all                # Show only non-default settings
```

**Change Settings**:
```
set motor_pwm_protocol = DSHOT600
set small_angle = 25
set acc_calibration = 0,0,0
save                    # Save and reboot (required!)
```

**Useful Commands**:
```
status                  # System status, sensor info
tasks                   # View task scheduling
resources               # Show pin assignments
bl                      # Enter bootloader (for firmware flash)
```

### Backup/Restore Configuration

**Backup** (save to file):
```
dump all
```
Copy entire output to text file.

**Restore** (paste back into CLI):
1. Open CLI
2. Paste saved configuration
3. Type `save` to apply

## Tuning for Different Use Cases

### Beginner/Educational Platform
**Goals**: Stable, forgiving, safe

**Settings**:
- **Rates**: Low (400-500°/s max)
- **RC Expo**: 0.30-0.40 (gentler near center)
- **Master Multiplier**: 0.8-1.0 (reduced P and D)
- **TPA**: Disabled (simpler)
- **Angle Mode Limit**: 40-50° (prevents extreme tilts)

### Cinematic/Camera Platform
**Goals**: Smooth, stable video

**Settings**:
- Use "Cinematic" preset as starting point
- **Rates**: Medium (500-600°/s)
- **Filtering**: Aggressive (reduce jello in video)
- **Master Multiplier**: 1.0-1.2 (smooth movements)
- **I-term**: Slightly higher (holds position better)

### Racing
**Goals**: Fast response, maximum agility

**Settings**:
- Use "Race" preset
- **Rates**: High (700-900°/s)
- **RC Expo**: 0.50+ (fine control at center, fast at edges)
- **Master Multiplier**: 1.2-1.5 (crisp response)
- **Filtering**: Minimal (priority on latency)
- **Air Mode**: Enabled always

### Freestyle
**Goals**: Control during tricks, smooth flow

**Settings**:
- Use "Freestyle" preset
- **Rates**: Very high (800-1000°/s)
- **PD Balance**: Slightly more D (smooth stop after flips)
- **I-term Relax**: Enabled (prevents bounce-back)
- **TPA**: Moderate (reduces oscillation at high throttle)

## Rates & Expo

Controls stick sensitivity and maximum rotation speeds.

**Betaflight Rates** (most common):
- **RC Rate**: Overall sensitivity multiplier
- **Super Rate**: Additional rate scaling at stick extremes
- **Expo**: Flattens response near center (precision), steeper at edges (speed)

**Recommended Starting Points**:
- **Beginners**: RC Rate 1.0, Super 0.70, Expo 0.30
- **Intermediate**: RC Rate 1.2, Super 0.75, Expo 0.40
- **Advanced**: RC Rate 1.5, Super 0.80, Expo 0.50

**Testing Rates**: Use [Betaflight Rate Calculator](https://www.desmos.com/calculator/r2svkbmhlu)

## LUA Scripts (OpenTX/EdgeTX Radios)

Custom functions accessible from transmitter.

### Betaflight TX Lua Scripts
Download from [Betaflight TX Lua Scripts GitHub](https://github.com/betaflight/betaflight-tx-lua-scripts)

**Features**:
- Change PIDs from transmitter
- Adjust rates mid-flight
- Enable/disable features
- View flight controller status

**Installation**:
1. Copy scripts to radio SD card
2. Set up telemetry sensors (SmartPort for FrSky)
3. Assign script to screen in radio

**Educational Use**: Students can tune without computer, great for field testing

## Troubleshooting

### Arming Issues

**"Arm switch is in unsafe position"**
- Arm switch activated before enabling prearm (if used)
- Solution: Set switch to disarmed position, try again

**"Angle too great"**
- Quad not level, exceeds max arm angle
- Solution: Place on level surface, or reduce `small_angle` in CLI

**"Throttle is not low"**
- Throttle stick not at zero
- Solution: Lower throttle stick fully

**"Accelerometer not calibrated"**
- Solution: Calibrate accelerometer

### Flight Issues

**Oscillations**
- Tune is too aggressive
- Solution: Reduce Master Multiplier by 10%, test again

**Feels Sluggish**
- Tune too soft, or rates too low
- Solution: Increase Master Multiplier slightly, or increase rates

**Motors Get Hot**
- D-term too high, or props/motors mismatched
- Solution: Reduce D gain, check propulsion system match

**Video Jello**
- Vibrations too high
- Solution: Balance props, check for loose arms, increase filtering

### OSD Issues

**No OSD Display**
- VTX not connected to FC UART, or wrong protocol
- Solution: Check wiring, enable MSP on correct UART, select OSD type

**Garbled OSD**
- PAL/NTSC mismatch
- Solution: Set OSD video standard to match camera/VTX

## Blackbox Analysis

### Recording Flight Data

1. **Blackbox Tab** → Enable logging to SD card
2. Fly normally
3. **Blackbox Tab** → Download logs after flight
4. Open in **Blackbox Explorer** (included with Configurator)

### What to Analyze

**Gyro Trace**
- Check for noise, oscillations
- Smooth trace = good tune
- High-frequency noise = vibration issues
- Low-frequency oscillations = P or D too high

**Motor Output**
- Motors should respond smoothly to commands
- Erratic motor output = tune issue or mechanical problem

**PID Controller**
- Desired vs Actual: Should track closely
- Large errors = tune needs work

## Educational Activities

### Lab Projects

1. **PID Tuning Exercise**: Start with very low PIDs, gradually increase, feel the difference
2. **Rates Comparison**: Fly with different rate presets, discuss control feel
3. **Blackbox Analysis**: Record flights, analyze in lab to find issues
4. **Build Competition**: Students build identical quads, compare performance
5. **FPV Simulator Training**: Use simulators (Liftoff, DRL Sim) with real transmitter

### FPV Racing
- Set up classroom racing gates
- Time trials with identical quads
- Teach racing lines and techniques
- Tournament-style competitions

### Freestyle Challenges
- Create trick list (flip, roll, power loop)
- Score-based on difficulty and style
- Teach video editing for recap videos

## Safety & Best Practices

### Pre-Flight Checklist
- [ ] Propellers correct size and direction
- [ ] Battery voltage correct (not over-discharged)
- [ ] Arm switch in disarmed position during plugin
- [ ] All screws tight (motors, standoffs, FC)
- [ ] Radio signal strong (check RSSI)
- [ ] Flight area clear of people

### During Flight
- Keep FPV flights within visual range (spotter required)
- Monitor battery voltage (land at 3.5V per cell minimum)
- Have kill switch or disarm ready at all times

### After Flight
- Check motors for heat (should be warm, not too hot to touch)
- Inspect props for damage
- Download blackbox logs if troubleshooting

## Resources

### Software Downloads
- [Betaflight Configurator](https://github.com/betaflight/betaflight-configurator/releases)
- [Blackbox Explorer](https://github.com/betaflight/blackbox-log-viewer/releases)
- [Betaflight TX Lua Scripts](https://github.com/betaflight/betaflight-tx-lua-scripts)

### Learning Resources
- [Betaflight Wiki](https://betaflight.com/docs/wiki)
- [Joshua Bardwell YouTube](https://www.youtube.com/c/JoshuaBardwell) - Excellent detailed tutorials
- [Oscar Liang Blog](https://oscarliang.com/) - Comprehensive guides
- [Betaflight Discord](https://discord.betaflight.com/) - Community support

### FPV Simulators
- **Liftoff**: Best graphics, realistic physics ($20)
- **DRL Sim**: Official DRL simulator, great for racing (Free tier available)
- **Velocidrone**: Hardcore simulator, very realistic ($20)
- **FPV Freerider**: Budget-friendly, good for beginners ($5)

### Example Configurations
- [Betaflight Config Examples](../../../code/flight-controllers/betaflight-configs/)

---

**Next**: [INAV →](inav.md) | [Back to Flight Controllers →](../index.md)
