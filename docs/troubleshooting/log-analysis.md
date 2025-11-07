# Log Analysis Guide

Flight logs contain detailed information about vehicle behavior, sensor data, and system performance. Learn to interpret logs to diagnose issues and improve performance.

## Log Types

### ArduPilot DataFlash Logs (.bin)
- High-rate logging to onboard flash or SD card
- Comprehensive sensor and state data
- Analysis with Mission Planner or UAV Log Viewer

### Betaflight Blackbox (.bbl)
- High-speed logging for PID tuning
- Motor outputs, PID terms, gyro data
- Analysis with Blackbox Explorer

### MAVLink Telemetry Logs (.tlog)
- Ground station recorded telemetry
- Lower rate than onboard logs
- Useful when onboard log not available

## Accessing Logs

### ArduPilot
**Download via Mission Planner:**
1. Connect via USB or telemetry
2. Flig

ht Data → DataFlash Logs
3. Download Log (full) or Download Latest Log
4. Save to computer

**Direct from SD Card:**
- Remove SD card from flight controller
- Copy .BIN files from SD card
- Insert card back into FC

### Betaflight/INAV
**Download Blackbox:**
1. Connect via USB
2. Blackbox tab
3. Flash chip or SD card
4. Download selected logs
5. Save as .BBL files

**Erase After Download:**
- Free space for new flights
- Keep only relevant logs

## Log Analysis Tools

### Mission Planner (ArduPilot)
**Features:**
- Built-in log review
- Graph any parameter vs time
- Pre-made graphs for common analysis
- Export to CSV

**Usage:**
1. Ctrl+F → "Log Browse"
2. Or: Flight Data → DataFlash Logs → "Review a Log"
3. Select log file
4. Choose graph preset or custom

### UAV Log Viewer
**Features:**
- Cross-platform
- Modern interface
- Multiple log comparison
- Export capabilities

**Usage:**
1. Open .bin file
2. Select parameters from list
3. Graph and analyze
4. Compare multiple flights

### Betaflight Blackbox Explorer
**Features:**
- Specialized for PID tuning
- High-resolution motor/gyro data
- Spectrum analyzer
- PID analyzer tool

**Usage:**
1. Open .BBL file
2. Navigate timeline
3. Analyze PID response
4. Export graphs

## Key Parameters to Review

### ArduPilot

**Basic Health Check:**
```
CTUN.ThO: Throttle output (hover should be 40-60%)
GPS.NSats: Satellite count (10+ ideal)
GPS.HDop: Horizontal dilution of precision (<1.5 good)
BATT.Volt: Battery voltage over time
BATT.Curr: Current draw
```

**Attitude and Control:**
```
ATT.DesRoll/DesPitch: Desired attitude
ATT.Roll/Pitch: Actual attitude
RATE.RDes/PDes: Desired rotation rate
RATE.R/P: Actual rotation rate
```

**PID Performance:**
```
PIDP.P, PIDP.I, PIDP.D: Pitch PID terms
PIDR.P, PIDR.I, PIDR.D: Roll PID terms
PIDY.P, PIDY.I, PIDY.D: Yaw PID terms
```

**Vibration:**
```
VIBE.VibeX/Y/Z: Vibration levels (<30 good, <60 acceptable)
IMU.AccX/Y/Z: Accelerometer clipping (should not clip)
```

### Betaflight

**PID Tuning:**
```
gyroADC: Raw gyro data
PID P/I/D: Individual PID term outputs
rcCommand: Stick inputs
motor[0-3]: Individual motor outputs
```

**Performance:**
```
loopIteration: Loop timing consistency
cpuLoad: Processor usage
debug: Various debug values
```

## Common Patterns and Diagnosis

### Oscillations

**High Frequency Oscillation:**
```
Pattern: Fast buzz in logs, tight oscillations
Cause: D gain too high or P gain way too high
Solution: Reduce D term, check P term
Look for: Motor output rapidly changing
```

**Medium Frequency Oscillation:**
```
Pattern: Noticeable wobble, ~5-10Hz
Cause: P gain too high
Solution: Reduce P term
Look for: Difference between desired and actual rate/angle
```

**Low Frequency Oscillation:**
```
Pattern: Slow wave, <1Hz
Cause: I gain too high
Solution: Reduce I term
Look for: I term growing large and oscillating
```

### Motor Issues

**Unbalanced Motors:**
```
Pattern: One motor consistently different output
Location: RCOU (ArduPilot) or motor outputs (Betaflight)
Cause: Mechanical issue, damaged motor, bad ESC
Action: Inspect that motor/ESC/prop
```

**Desyncs:**
```
Pattern: Motor output drops to zero briefly
Location: Motor output channels
Cause: ESC losing sync with motor
Solution: Check timing, protocol, connections
```

**Motor Saturation:**
```
Pattern: One or more motors at 100% frequently
Cause: CG offset, bent frame, insufficient power
Action: Balance weight, check frame, larger motors
```

### GPS Issues

**GPS Glitches:**
```
Pattern: Sudden jumps in Lat/Lon
Location: GPS.Lat, GPS.Lng, GPS.Alt
Cause: Poor signal, interference, multipath
Effect: Position hold drift, navigation errors
```

**Poor GPS Performance:**
```
Indicators:
- NSats < 10
- HDop > 2.0
- Velocity noise
Cause: Obstructed view, interference
```

### Vibration Problems

**Excessive Vibration:**
```
Thresholds:
- VibeX/Y/Z < 30: Excellent
- 30-60: Acceptable
- >60: Problem

Causes:
- Unbalanced props
- Bent frame
- Loose screws
- Bad motor bearings
```

**Accelerometer Clipping:**
```
Pattern: Flat-topped acceleration spikes
Location: IMU.AccX/Y/Z
Cause: Vibration exceeding sensor range
Effect: Attitude estimation errors
Solution: Reduce vibration, soft-mount FC
```

### Battery/Power Issues

**Voltage Sag:**
```
Pattern: Voltage drops under throttle
Normal: Some sag expected
Excessive: >1V drop per cell problematic
Causes: Weak battery, high current, bad connections
```

**Brownout:**
```
Pattern: Voltage drops below minimum, reboot
Location: BATT.Volt, GPS gaps in log
Cause: Insufficient battery capacity or bad connection
Critical: Can cause crash
```

## Crash Analysis

### Analyzing a Crash Log

**Steps:**

1. **Identify Crash Point**
   - Look for sudden attitude change
   - Motor outputs go to extremes
   - Rapid altitude loss

2. **Review Preceding Events**
   - What happened 5-10 seconds before?
   - Mode changes?
   - Control inputs?
   - Sensor anomalies?

3. **Check for Warnings**
   - Pre-arm failures ignored?
   - EKF variances?
   - Compass issues?

4. **Determine Root Cause**
   - Pilot error?
   - Hardware failure?
   - Software bug?
   - Environmental factors?

### Common Crash Causes in Logs

**Loss of Control:**
```
Signs:
- Desired attitude very different from actual
- One motor not responding
- Extreme PID outputs
- Gyro data erratic
```

**Flyaway:**
```
Signs:
- Vehicle position moving rapidly
- Compass heading wrong
- GPS position jumps
- Vehicle fighting pilot inputs
```

**Power Loss:**
```
Signs:
- Voltage drops to zero
- All sensors stop
- Immediate end of log
```

**ESC Failure:**
```
Signs:
- One motor output drops to zero
- Attitude rolls to one side
- Other motors compensate (high output)
```

## PID Tuning with Logs

### Betaflight PID Analysis

**Using PID Analyzer:**

1. Record blackbox during test flight
2. Open in Blackbox Explorer
3. Tools → PID Analyzer
4. Select axis and time range
5. Review PID response

**Good PID Tune Indicators:**
- Gyro tracks setpoint closely
- Minimal overshoot
- No oscillation
- P, I, D terms balanced

**Poor Tune Indicators:**
- Large difference between setpoint and gyro
- Oscillation (too much P or D)
- Sluggish response (too little P)
- Steady-state error (too little I)

### ArduPilot PID Tuning

**Review PID Terms:**

1. Graph RATE.RDes vs RATE.R (desired vs actual roll rate)
2. Graph PIDR.P, PIDR.I, PIDR.D (PID terms)
3. Make stick inputs in flight
4. Analyze response:
   - Should track well
   - No oscillation
   - Return to zero smoothly

## Educational Uses

### Classroom Activities

**Activity 1: Log Interpretation**
- Provide sample logs
- Students identify issues
- Discuss findings
- Compare conclusions

**Activity 2: Before/After Tuning**
- Compare logs pre and post PID tuning
- Quantify improvement
- Understand PID effects

**Activity 3: Crash Investigation**
- Analyze crash logs
- Determine root cause
- Propose prevention measures
- Document findings

### Assessment

**Rubric:**

| Skill | Novice | Proficient | Expert |
|-------|--------|-----------|--------|
| Log Access | Needs help downloading | Downloads independently | Configures logging |
| Parameter Identification | Finds with guidance | Selects relevant parameters | Knows where to look |
| Pattern Recognition | Misses issues | Identifies obvious problems | Catches subtle anomalies |
| Root Cause Analysis | Guesses | Systematic diagnosis | Comprehensive analysis |

## Advanced Analysis

### Spectral Analysis

**Betaflight Spectrum Analyzer:**
- Identify noise frequencies
- Tune filters accordingly
- Reduce motor heat
- Improve flight performance

**Process:**
1. Record blackbox with copter on bench (motors on)
2. Open in Blackbox Explorer
3. Tools → Spectrum Analyzer
4. Identify noise peaks
5. Adjust filter frequencies to target peaks

### Comparing Multiple Flights

**Use Cases:**
- Before/after modifications
- Different conditions
- Tuning progression
- Performance validation

**Method:**
1. Standardize test flights (same maneuvers)
2. Log each flight
3. Overlay parameters in analysis tool
4. Compare quantitatively

### Exporting Data

**For External Analysis:**
1. Export to CSV from log viewer
2. Import to spreadsheet or MATLAB
3. Custom analysis and graphing
4. Statistical analysis

## Troubleshooting Log Issues

### No Logs Available

**Causes:**
- Logging not enabled
- Flash full
- SD card missing/full
- Logging rate too low

**Solutions:**
- Enable logging in configuration
- Erase old logs
- Insert/format SD card
- Increase log rate

### Incomplete Logs

**Causes:**
- Crash damaged log file
- Log rate too high (buffer overflow)
- SD card write errors

**Solutions:**
- Some data may be recoverable
- Reduce log rate
- Use faster SD card (Class 10)

### Corrupted Logs

**Causes:**
- Interrupted download
- Hardware failure
- File system corruption

**Solutions:**
- Re-download if possible
- Use log repair tools
- May be unrecoverable

## Best Practices

**Log Everything:**
- Keep logs of all flights
- Especially important flights and problematic flights
- Storage is cheap

**Organize Logs:**
- Name descriptively (date, vehicle, notes)
- Folder structure by vehicle/date
- Document significant flights

**Review Regularly:**
- Check logs after each flight session
- Catch problems early
- Track performance trends

**Share Appropriately:**
- Include logs when asking for help
- Contribute to research
- Respect privacy (GPS coordinates)

## Next Steps

- [Hardware Issues](hardware-issues.md) - Physical problems
- [Software Issues](software-issues.md) - Configuration issues
- [Flight Operation Issues](flight-operation-issues.md) - Flying problems
- [Advanced Control](../control-systems/advanced-control.md) - PID tuning theory

## Resources

- Mission Planner Log Analysis Guide
- Betaflight Blackbox Explorer Wiki
- UAV Log Viewer Documentation
- ArduPilot Log Message Definitions
- Community Forum Log Analysis Threads
