# Flight Operation Troubleshooting

Issues occurring during flight or vehicle operation. Solutions for unstable flight, drifting, unexpected behavior, and operational problems.

## Arming Problems {#arming-problems}

### Vehicle Won't Arm

**Check Pre-Arm Safety Checks:**

Connect to configurator and check status/messages tab for specific errors.

#### Common Pre-Arm Failures

| Error | Cause | Solution |
|-------|-------|----------|
| GPS Lock | <6 satellites | Wait for GPS lock outdoors |
| Compass | Not calibrated | Calibrate compass away from metal |
| Accelerometer | Not level calibrated | Calibrate on level surface |
| Throttle | Throttle not at zero | Lower throttle stick |
| Mode | Current mode doesn't allow arming | Switch to Stabilize/Manual |
| Gyro | Not calibrated/initializing | Wait or recalibrate |
| Baro | Not initialized | Reboot or check sensor |
| RC | No RC signal | Check transmitter, binding |

**Bypass Safety Checks (Educational/Testing Only):**
```
ArduPilot: ARMING_CHECK = 0 (bypasses all - UNSAFE)
Better: ARMING_CHECK = selective bits to skip specific checks
```

!!! danger "Safety Warning"
    Never bypass arming checks for flight. Only use for bench testing with propellers removed.

### Arms Then Immediately Disarms

**Causes:**

1. **Auto-Disarm Timeout**
   - Arms but no throttle applied
   - Solution: Apply throttle sooner or disable timeout

2. **Pre-Arm Becomes Fail During Arm**
   - GPS drops, compass interference
   - Solution: Address intermittent sensor issue

3. **Crash Detection**
   - Vibration triggers crash detect
   - Solution: Reduce sensitivity or disable for testing

4. **Low Battery**
   - Battery failsafe immediately triggered
   - Solution: Charge battery, check voltage thresholds

## Stability Issues {#stability-issues}

### Oscillations / Vibrations

**Diagnosis by Frequency:**

**High Frequency (Fast Buzz):**
- **Cause**: D gain too high, electrical noise
- **Test**: Reduce D term by 20%
- **Also check**: Prop balance, motor bearings

**Medium Frequency (Wobble):**
- **Cause**: P gain too high
- **Test**: Reduce P term by 10%
- **Also check**: Frame rigidity, loose screws

**Low Frequency (Slow Wave):**
- **Cause**: I gain too high
- **Test**: Reduce I term
- **Also check**: Weight distribution, CG location

**Propwash (Descending):**
- **Cause**: Turbulent air from props
- **Test**: Increase D term, enable low-pass filters
- **Common**: Normal in fast descents

### Violent Oscillations on Takeoff

!!! danger "Land Immediately"
    Violent oscillations can cause crash and injury. Land as soon as safely possible.

**Most Common Causes:**

1. **Props Wrong Direction**
   - Props installed backward
   - Check prop rotation direction marking
   - Match to motor spin direction

2. **Motor Direction Wrong**
   - Motor spinning opposite of expected
   - Test in configurator motor tab
   - Reverse in BLHeli or swap two wires

3. **P Gain Extremely High**
   - Way too aggressive
   - Reset PIDs to defaults
   - Tune gradually from baseline

4. **Gyro Orientation Wrong**
   - FC mounted rotated but not configured
   - Set board orientation parameter
   - Or physically rotate FC

### One-Sided Tilt

**Symptoms:**
- Tilts to one side consistently
- Requires trim to hover level
- Drifts in one direction

**Causes:**

| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Tilts same direction in all modes | CG offset, bent frame | Check weight distribution, frame alignment |
| Tilts in stabilize only | Accelerometer calibration | Recalibrate on level surface |
| Tilts in GPS modes | Compass calibration/orientation | Recalibrate compass, check orientation |
| Increases with throttle | Motor/ESC issue | Check individual motor thrust |

**Testing:**
1. Hover in stabilize mode
2. Note tilt direction and amount
3. Check log for motor outputs
4. All motors should be similar in hover
5. If one significantly different: investigate that motor/ESC

### Unstable in Wind

**Normal Behavior:**
- Some drift in wind is normal
- Depends on wind speed vs vehicle power

**Excessive Drift:**

1. **GPS Position Hold**
   - Check GPS satellite count (need 10+)
   - Verify HDOP <2.0
   - Compass calibrated correctly

2. **Altitude Hold**
   - Barometer affected by wind
   - Add airspeed sensor for better performance
   - Fly in calmer conditions

3. **Insufficient Power**
   - Can't fight wind
   - Upgrade motors/props
   - Heavier vehicle helps

## Drift and GPS Issues

### Position Hold Drift

**Slow Drift (cm/s):**
- Acceptable: GPS accuracy limitation
- Improve: Wait for more satellites, better GPS placement

**Moderate Drift (several m/min):**
- **Compass Issue**: Heading error causes position error
  - Recalibrate compass
  - Check for magnetic interference
  - Verify orientation parameter

**Fast Drift (flies away):**
- **Major GPS or Compass Problem**:
  - GPS position jumps
  - Compass 180° reversed
  - Switch to stabilize immediately
  - Land and diagnose

### Toilet Bowl Effect

**Symptoms:**
- Circles in loiter or position hold
- Circle gets larger over time
- May eventually fly away

**Cause:**
- Compass pointing wrong direction
- Vehicle thinks it's drifting when it's not
- Corrections make it worse

**Solutions:**

1. **Immediate**: Switch to stabilize mode, land safely

2. **Diagnosis**:
   - Check compass orientation
   - Look for compass interference (current, magnets)
   - Verify compass calibration

3. **Fix**:
   - Recalibrate compass outdoors
   - Check COMPASS_ORIENT parameter
   - Test compass with throttle (check for current interference)
   - May need external GPS/compass on mast

### GPS Altitude Jumps

**Symptoms:**
- Altitude suddenly changes in logs
- Not actual altitude change
- Causes altitude hold issues

**Causes:**
- Poor GPS signal
- Multipath (signal reflections)
- Transition between GPS and barometer

**Solutions:**
- Primarily use barometer for altitude (most FCs do)
- Ensure clear GPS view
- EKF fusion helps smooth
- Check LOG for GPS glitches

## Unexpected Behavior

### Flyaway

**Definition:**
- Vehicle flies away uncontrollably
- Does not respond to inputs
- Most dangerous malfunction

**Immediate Actions:**
1. Switch to stabilize mode
2. Disarm if close to ground
3. Trigger RTL if GPS available
4. Note direction for recovery

**Common Causes:**

1. **Compass Issues**
   - Reversed or wrong orientation
   - Severe magnetic interference
   - Prevention: Verify compass before flight

2. **GPS Problems**
   - Position jumps
   - Firmware expecting GPS when not available
   - Prevention: Test GPS modes nearby first

3. **RC Link Loss**
   - Failsafe not configured
   - Wrong failsafe action
   - Prevention: Test failsafe before flight

4. **Software Bug**
   - Rare but possible
   - Prevention: Use stable firmware

**Post-Flyaway:**
- Review logs thoroughly
- Fix root cause before next flight
- Test fixes incrementally

### Unexpected Flip on Takeoff

**Causes:**

1. **Props Backward**
   - Most common cause
   - Visual check: props should push air down

2. **Motor Order Wrong**
   - Wired to wrong FC outputs
   - Test: Use motor test feature
   - Match to diagram for FC

3. **Motor Direction Wrong**
   - Not spinning expected direction
   - Fix in BLHeli or swap two wires
   - Test all motors before flight

4. **Board Orientation Wrong**
   - FC mounted rotated
   - Set board_align parameters
   - Or remount FC standard orientation

### Sudden Drop/Wobble Mid-Flight

**If Occurs Once:**
- Possible desync (ESC)
- Possible motor hit debris
- Land and inspect

**If Repeating:**
- Motor bearing failure
- Loose prop
- Damaged prop
- ESC overheating/failing

**Action:**
- Land immediately
- Full inspection before next flight
- Check logs for motor output anomalies

## Throttle and Power Issues

### Loss of Altitude in Hover

**Symptoms:**
- Can't maintain altitude
- Descends in hover
- Full throttle needed

**Causes:**

| Issue | Check | Solution |
|-------|-------|----------|
| Low Battery | Voltage sag under load | Land, recharge |
| Wrong Props | Size/pitch incorrect | Match to motor specs |
| Damaged Props | Nicks, bent, imbalanced | Replace props |
| Motor Failure | One motor weak | Test motors individually |
| Too Heavy | Overloaded | Reduce weight or larger motors |
| Air Density | High altitude/temperature | Limit operation or larger props |

### Throttle Doesn't Respond Linearly

**Symptoms:**
- Jumpy altitude control
- Hard to maintain smooth hover
- Overshoots and undershoots

**Solutions:**

1. **Tune Altitude Hold PIDs**
   - Reduce P gain if jumpy
   - Increase D gain for smoothness
   - I gain for steady-state hover

2. **Check Throttle Curve**
   - Should be linear for auto modes
   - Expo in manual control only

3. **Barometer Issues**
   - Ensure not in prop wash
   - Shield from wind
   - Add foam but don't seal

### Throttle Mid-Point Wrong

**Symptoms:**
- Motors idle too high/low
- Poor throttle resolution

**Configuration:**

```
Betaflight:
- Motor idle: Set minimum throttle for reliable spin
- Throttle mid: 50% default

ArduPilot:
- MOT_SPIN_MIN: Minimum throttle for spin
- MOT_SPIN_ARM: Armed but no throttle throttle
- MOT_THST_HOVER: Learned hover throttle
```

## Control Response Issues

### Sluggish Response

**Symptoms:**
- Slow to respond to stick inputs
- Feels mushy
- Hard to control precisely

**Causes:**

1. **P Gain Too Low**
   - Increase P term
   - Test in small increments
   - Stop before oscillations

2. **Rates Too Low**
   - Maximum rotation rate limited
   - Increase in transmitter or FC
   - Balance with control smoothness

3. **TPA Too Aggressive**
   - Throttle PID attenuation reducing gains
   - Adjust TPA curve
   - May need higher breakpoint

4. **Expo Too High**
   - Reduces sensitivity
   - Lower expo value
   - Find balance for control style

### Too Aggressive/Twitchy

**Symptoms:**
- Oversensitive to inputs
- Hard to fly smoothly
- Small movements cause large response

**Solutions:**

1. **Reduce Rates**
   - Lower max rotation speed
   - More precision near center stick

2. **Add Expo**
   - Reduces center stick sensitivity
   - 30-40% typical

3. **Lower P Gain**
   - If also oscillating
   - Find balance with stability

4. **Check Filters**
   - Too much filtering can cause delay
   - Then pilot overcontrols

### Delayed Response

**Symptoms:**
- Vehicle responds but after delay
- Feels like lag
- Hard to control

**Causes:**

1. **Excessive Filtering**
   - Too many low-pass filters
   - Reduces latency at cost of protection
   - Balance carefully

2. **Slow ESC Protocol**
   - Standard PWM has latency
   - Upgrade to DShot
   - Lower DShot rate if issues

3. **Receiver Latency**
   - Some receivers slower than others
   - Digital often faster
   - Consider upgrade

4. **Weak Radio Signal**
   - Packet loss causes delays
   - Check RSSI
   - Better antennas or reduce range

## Landing Issues

### Hard Landings

**Causes:**

1. **Altitude Estimation Error**
   - Barometer drift
   - GPS altitude inaccurate
   - Use rangefinder for precision

2. **Throttle Cut Too Early**
   - Land mode parameters
   - Adjust final descent rate

3. **Pilot Technique**
   - Practice smooth descents
   - Flare before touchdown
   - Reduce descent rate near ground

### Bounces on Landing

**Causes:**

1. **Ground Effect**
   - Air pressure under vehicle
   - Normal physics
   - More pronounced on hard surfaces

2. **I Term Windup**
   - Accumulated I term
   - Causes bounce-back
   - Reduce I gain or add limiter

3. **Surface Irregularities**
   - Soft ground
   - Angled surface
   - Choose better landing spot

### Won't Land (Altitude Hold Above Ground)

**Symptoms:**
- Auto land stops above ground
- Hovers at 1-2m
- Won't complete landing

**Causes:**

1. **No Rangefinder**
   - Relying on barometer or GPS
   - Not accurate enough
   - Add rangefinder for precision

2. **Rangefinder Misconfigured**
   - Wrong orientation
   - Not enabled for landing
   - Check RNGFND_LANDING = 1

3. **Object Detection**
   - Some systems avoid landing on obstacles
   - May detect grass/rough surface as obstacle

## Emergency Procedures

### Loss of Control Recovery

**Steps:**

1. **Don't Panic** - Clear thinking essential
2. **Center Sticks** - Return to neutral
3. **Switch to Stabilize** - Most predictable mode
4. **Assess Situation** - Altitude, obstacles, wind
5. **Plan Landing** - Find safest spot
6. **Execute** - Smooth, controlled descent

### Failsafe Activation

**When Failsafe Triggers:**

1. **Do Not Fight It**
   - Let failsafe complete
   - Designed for safety

2. **Monitor Descent**
   - Ensure safe trajectory
   - Clear area if possible

3. **Be Ready to Intervene**
   - If heading toward danger
   - Switch to manual control if able

4. **Post-Event**
   - Investigate cause
   - Test failsafe intentionally
   - Verify correct operation

### Low Battery in Flight

**Actions:**

1. **Land Immediately**
   - Find nearest safe spot
   - Don't try to return if too far

2. **Reduce Power Draw**
   - Gentle flight
   - Maintain altitude
   - No aggressive maneuvers

3. **Monitor Voltage**
   - Watch OSD or telemetry
   - Have voltage alarm configured

4. **Emergency Landing**
   - If voltage critical
   - Survive landing, protect people first

## Post-Flight Analysis

### Using Logs to Diagnose

After problematic flight:

1. **Download Logs**
   - ArduPilot: .bin files
   - Betaflight: Blackbox .bbl files

2. **Review in Analysis Software**
   - Mission Planner (ArduPilot)
   - Betaflight Blackbox Explorer

3. **Look for Patterns**
   - Motor outputs: Should be similar in hover
   - PID terms: Oscillation indicates tuning issue
   - Sensors: Spikes or dropouts
   - RC input: Verify control inputs

4. **Compare to Known Good Flight**
   - What's different?
   - When did behavior start?

[→ Detailed Log Analysis Guide](log-analysis.md)

### Test Flight Progression

After fixing issue:

1. **Bench Test**
   - Props off
   - Verify fix
   - Test all functions

2. **Hover Test**
   - Open area
   - Low altitude (1-2m)
   - Verify stability
   - Test modes

3. **Pattern Flight**
   - Figure-8s, circles
   - Test control response
   - Gradually increase envelope

4. **Normal Operation**
   - Only after confidence restored
   - Monitor for issues
   - Keep detailed logs

## Common Mistakes

**Pilot Error:**
- Wrong mode for situation
- Loss of orientation
- Insufficient practice
- Ignoring warnings

**Configuration Error:**
- Untuned or default PIDs
- Wrong sensor orientation
- Mismatched protocols
- Skipped calibration

**Maintenance Error:**
- Loose components
- Damaged props
- Degraded battery
- Worn bearings

## Prevention Strategies

**Pre-Flight:**
- Complete checklist every time
- Test all functions on ground
- Verify GPS lock and sensor health
- Check battery voltage

**During Flight:**
- Monitor telemetry
- Stay within limits
- Plan before acting
- Keep escape options

**Post-Flight:**
- Inspect for damage
- Review logs for anomalies
- Document issues
- Maintain regularly

## Next Steps

- [Log Analysis](log-analysis.md) - Detailed flight log review
- [Hardware Issues](hardware-issues.md) - Physical problem diagnosis
- [Software Issues](software-issues.md) - Configuration problems
- [Safety Incident Response](safety-incident-response.md) - Crash procedures
- [Preventive Maintenance](preventive-maintenance.md) - Avoid problems

## Educational Applications

### Learning Activities

**Flight Test Analysis:**
- Record specific maneuver
- Analyze logs
- Identify areas for improvement
- Document findings

**Troubleshooting Scenarios:**
- Present common issues
- Students diagnose
- Propose solutions
- Test fixes

**Emergency Response Drill:**
- Simulate emergencies in controlled environment
- Practice procedures
- Build muscle memory
- Debrief and learn

## Safety Emphasis

!!! warning "Safety First"
    - **Never** fly over people
    - **Always** maintain visual line of sight
    - **Keep** emergency procedures in mind
    - **Land** at first sign of trouble
    - **Inspect** after every incident
    - **Learn** from every flight
