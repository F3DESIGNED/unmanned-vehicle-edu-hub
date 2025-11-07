# Educational Quadcopter Build (250-500g)

Build a capable quadcopter platform for autonomous missions, programming integration, and competition use. This intermediate build teaches advanced integration skills and supports GPS waypoint navigation.

## Project Overview

**Skill Level**: Intermediate
**Build Time**: 6-10 hours
**Flight Time**: 10-15 minutes
**Cost**: $250-450
**Best For**: Programming, autonomous missions, GPS navigation, competitions

### Why Build This Platform?

- **Autonomous Capable**: GPS, mission planning, return-to-home
- **Programming Integration**: Python (DroneKit), MAVLink, ROS support
- **Competition Ready**: AUVSI SUAS, local competitions, challenges
- **Durable**: Withstands outdoor conditions and learning crashes
- **Expandable**: Payloads, sensors, companion computers
- **Career Relevant**: Industry-standard components and workflows

## Bill of Materials (BOM)

### Core Components

| Component | Specification | Qty | Unit Cost | Total | Vendor | Part Number |
|-----------|---------------|-----|-----------|-------|--------|-------------|
| **Frame** | 250mm carbon fiber X-frame | 1 | $35-50 | $35-50 | GetFPV | QAV250 or similar |
| **Motors** | 2205/2207 2300KV brushless | 4 | $15-20 | $60-80 | EMAX | RS2205 2300KV |
| **ESCs** | 30A BLHeli_S or 35A 4-in-1 | 4/1 | $10/$50 | $40-60 | Racerstar/Holybro | Various |
| **Flight Controller** | Pixhawk 2.4.8 or Matek F405 | 1 | $60-100 | $60-100 | Holybro/Matek | Multiple options |
| **Props** | 5045 tri-blade or 6045 bi-blade | 4 sets | $4-6 | $16-24 | DAL/Gemfan | 5045x3 |
| **Battery** | 3S/4S 1500-2200mAh 45C+ LiPo | 3 | $20-30 | $60-90 | Tattu/Gens Ace | Various |
| **GPS Module** | UBLOX M8N with compass | 1 | $20-35 | $20-35 | Radiolink/Holybro | M8N GPS |
| **Radio Receiver** | SBUS/Crossfire/ELRS | 1 | $15-45 | $15-45 | FrSky/TBS/ELRS | R-XSR/Crossfire Nano |
| **Power Distribution** | PDB with 5V/12V BEC | 1 | $8-15 | $8-15 | Matek | PDB-XPW |
| **Transmitter** | 2.4GHz 8+ channel | 1 | $50-150 | $50-150 | Radiomaster/FrSky | TX16S/QX7 |
| **FPV Camera** | 1200TVL micro camera (optional) | 1 | $15-25 | $15-25 | Foxeer/Runcam | Racer Nano |
| **VTX** | 25-200mW video transmitter (opt) | 1 | $15-25 | $15-25 | TBS/ImmersionRC | Unify Pro |

**Total**: $379-684 (varies by options, vendor, shipping)

**Estimated Budget**: ~$450 for complete autonomous platform

### Additional Hardware

- XT60 connectors (battery leads)
- Battery strap (velcro, 20mm wide)
- Loctite threadlocker (blue, removable)
- Heat shrink tubing (various sizes)
- M3 screws, nuts, standoffs (assorted)
- Vibration dampening mounts
- Battery voltage alarm or telemetry

### Tools Required

- Soldering station (temperature controlled)
- Solder (60/40 rosin core)
- Helping hands / PCB vise
- Hex drivers (1.5mm, 2.0mm, 2.5mm)
- Wire cutters, strippers
- Multimeter
- Propeller balancer (recommended)
- Heat gun (for heat shrink)
- Computer with USB ports (for configuration)

## Frame Assembly

### Step 1: Frame Preparation

**Inspect Frame Kit**:
- Bottom plate (main deck)
- Top plate (protects electronics)
- 4× arms (with motor mounts)
- Hardware bag (screws, standoffs, nuts)
- Optional: PDB mounting hardware

**Frame Assembly**:
1. **Bottom Plate + Arms**: Secure 4 arms to bottom plate using M3 screws
   - Tighten in X-pattern (prevents warping)
   - Use threadlocker on screws (prevents loosening from vibration)
2. **Standoffs**: Install 25-30mm standoffs for FC stack mounting
3. **Inspection**: Ensure all screws tight, arms not twisted

### Step 2: Motor Installation

**Motor Mounting**:
- Motors mount to arm tips
- 4 screws per motor (usually M2 or M3)
- Apply threadlocker (critical - motors vibrate screws loose)

**Motor Orientation**:
- Wires face inward toward center of frame
- Rotate motor if needed (loosen screws, rotate, retighten)
- Leave some wire slack (arms flex in crashes)

**Motor Labeling**:
- Label motor wires: M1, M2, M3, M4
- Prevents confusion during ESC wiring

```
Quadcopter Motor Layout (X-configuration):
       FRONT
   M1(CCW)  M2(CW)
      \       /
       \     /
        [FC]
       /     \
      /       \
   M4(CW)  M3(CCW)
       BACK
```

## Power System

### Step 3: Power Distribution Board (PDB)

**PDB Installation**:
1. Mount PDB to bottom plate (usually directly above or below FC)
2. Solder battery leads (XT60 connector):
   - Red wire → BAT+ pad
   - Black wire → GND pad
   - Use heavy gauge wire (12-14 AWG) for main power
3. Verify polarity with multimeter BEFORE connecting battery

**BEC Outputs**:
- 5V pads: For FC, receiver, camera
- 12V pads (if available): For VTX or other accessories
- Test voltages with multimeter

### Step 4: ESC Installation & Wiring

#### Option A: Individual ESCs

**Mounting**:
- Zip-tie ESCs to arms near motors
- Use heat shrink over ESC (protection + mounting)

**Wiring**:
1. **Motor Wires**: Solder motor wires to ESC output pads
   - Any order initially (we'll fix direction later)
   - Tin wires and pads before soldering
2. **Power Wires**: Solder red/black to PDB BAT+/GND
3. **Signal Wire**: Run to FC motor output pads

#### Option B: 4-in-1 ESC (Easier, Recommended)

**Mounting**:
- Mounts in stack with FC (using same standoffs)
- Usually between PDB and FC

**Wiring**:
1. **Battery**: Solder to PDB or directly to ESC BAT pads
2. **Motors**: Solder motor wires to M1, M2, M3, M4 pads
3. **Signal**: Connects to FC via stack connector or wires

### Step 5: Flight Controller Mounting

**Pixhawk Installation** (ArduPilot):
1. Use vibration damping foam/grommets (critical for Pixhawk)
2. Arrow points forward
3. Secure with screws or adhesive foam
4. Keep away from high-current wires (interference)

**Alternative FC (Matek F405, etc.)**:
1. Moderate vibration damping (not as critical as Pixhawk)
2. Orient per board markings
3. Stack configuration if using 4-in-1 ESC

**Wiring**:
- Motor signal wires (M1-M4) to corresponding pads
- 5V and GND from PDB
- GPS/compass connector (prepare for GPS module)
- Receiver connector (SBUS usually UART1 or designated pad)

## GPS & Sensors

### Step 6: GPS Module Installation

**Mounting Location**:
- Top of frame, elevated on mast/standoff
- Clear view of sky (no carbon fiber blocking)
- Away from power wires (magnetic interference)

**Mounting Options**:
- 3D printed GPS mast
- Tall standoffs (50-70mm)
- Commercial GPS mount

**Wiring**:
- 6-pin connector (usually): VCC, GND, TX, RX, SCL, SDA
- Route cable down to FC (may need extension cable)
- Keep away from motor wires
- Secure with zip ties (prevent vibration)

**Compass Calibration**:
- Required before first flight
- Do outdoors, away from metal, electronics
- Rotate drone in all axes per calibration instructions

## Radio & Telemetry

### Step 7: Receiver Installation

**SBUS Receivers** (FrSky, etc.):
- Connect signal wire to FC UART RX pin (counterintuitive!)
- Connect VCC (5V) and GND
- Mount with foam tape (vibration isolation)
- Position antennas perpendicular, away from carbon fiber

**Crossfire/ELRS**:
- CRSF protocol, single wire connection
- Mount receiver with clear view (or external antenna)
- Bind to transmitter per manufacturer instructions

**Antenna Placement**:
- Spread antennas apart (diversity)
- Keep away from metal (blocks RF)
- Secure with zip ties (prevent damage)

### Step 8: Telemetry Radio (Optional)

**Purpose**: Wireless configuration, mission planning, real-time data

**Options**:
- 915MHz (US) or 433MHz (EU) telemetry radios
- Bluetooth modules (short range)
- WiFi (ESP8266/ESP32 modules)

**Installation**:
- Connect to FC telemetry port (UART)
- Mount externally or internally
- Antenna outside frame for best range

## FPV System (Optional)

### Step 9: FPV Camera

**Mounting**:
- Front of frame, slightly angled up (10-20°)
- Use camera mount (3D printed or included)
- Secure with screws or foam tape

**Wiring**:
- VCC (5V or VBAT, check camera specs)
- GND
- Video out → VTX video in

### Step 10: Video Transmitter (VTX)

**Mounting**:
- Top plate (heat dissipation)
- Keep away from GPS (interference)

**Wiring**:
- Power (usually VBAT, filtered if possible)
- GND
- Video in (from camera)
- Control wire (SmartAudio/Tramp to FC, optional)

**Antenna**:
- Secure antenna upright
- NEVER power on VTX without antenna (burns out immediately)
- Use antenna zip-tied to standoff

## Final Assembly

### Step 11: Top Plate Installation

**Before Closing**:
- Check all solder joints (no cold joints, no shorts)
- Verify no wires near props
- Check for loose components
- Take photos (helps with troubleshooting later)

**Top Plate**:
1. Route wires cleanly through frame
2. Ensure no pinched wires
3. Secure plate with screws
4. Don't over-tighten (carbon fiber can crack)

### Step 12: Battery Mounting

**Battery Strap**:
- Velcro strap on bottom of frame
- Or side-mount if bottom clearance needed

**Balance**:
- Battery centered (fore-aft and left-right)
- CG should be near FC location
- Test by balancing on finger (should level roughly)

**Voltage Alarm** (highly recommended):
- Small buzzer that plugs into balance connector
- Alerts when voltage drops (prevents over-discharge)

## Software Configuration

### Step 13: Firmware Installation

#### For ArduPilot (Pixhawk):
1. Download [Mission Planner](https://ardupilot.org/planner/) or [QGroundControl](http://qgroundcontrol.com/)
2. Connect FC via USB
3. Install Firmware → Select "Copter" (quadcopter)
4. Wait for installation complete

#### For Betaflight/INAV (Alternative FCs):
1. Download appropriate Configurator
2. Flash firmware for your FC model
3. Follow configurator setup wizard

**Detailed Configuration**: See [ArduPilot Setup Guide](../flight-controllers/ardupilot.md)

### Step 14: Mandatory Calibrations

**Accelerometer**:
- Place quad level on table
- Run accelerometer calibration
- Follow prompts for 6 orientations (level, nose up, nose down, left, right, upside down)

**Compass**:
- Take quad outdoors
- Run compass calibration (rotation in all axes)
- Keep away from metal, power lines, buildings

**Radio Calibration**:
- Bind transmitter to receiver
- Run radio calibration (move all sticks to extremes)
- Verify all channels mapped correctly

**ESC Calibration**:
- May not be needed (many ESCs auto-calibrate)
- If needed, follow FC-specific procedure

### Step 15: Configuration Parameters

**Frame Type**: Quad X (standard)

**Flight Modes** (ArduPilot example):
- Mode 1: Stabilize (manual, self-leveling)
- Mode 2: Alt Hold (holds altitude)
- Mode 3: Loiter (GPS position hold)
- Mode 4: RTL (return to launch)
- Mode 5: Auto (waypoint missions)

**Failsafes**:
- Low battery → RTL or Land
- Radio loss → RTL
- GPS loss → Land (if in GPS mode)

**Battery Monitoring**:
- Enter battery capacity (mAh)
- Calibrate voltage sensor (use multimeter)
- Set low voltage warning (3.5V per cell)

## Pre-Flight Testing

### Step 16: Motor Testing

!!! danger "Props OFF for All Testing"

**Motor Order**:
1. Connect via USB, open configurator
2. Motor test tab → spin each motor
3. Verify motor number matches frame position
4. Front-right should be M1 (or M2, depending on FC)

**Motor Direction**:
- Verify rotation matches diagram (CCW or CW)
- If wrong: Swap any TWO motor wires OR enable software reversal (DShot)

### Step 17: Ground Tests

**With Battery, Props OFF**:
1. Connect battery (wear safety glasses)
2. Verify FC powers up (LEDs, sounds)
3. Transmitter range check (walk 50+ feet, test controls)
4. Arm test (verify arming works)
5. Throttle response (motors spin up smoothly)

**GPS Test**:
- Check GPS status (needs 10+ satellites)
- May take 5+ minutes for first lock
- Verify home position set (if using ArduPilot/INAV)

### Step 18: Propeller Installation

**Propeller Identification**:
- CW props: Normal threads (tighten clockwise)
- CCW props: Reverse threads (tighten counterclockwise) OR marked CCW
- Identify by blade slant: Leading edge tilts down in rotation direction

**Installation**:
1. Match prop type (CW/CCW) to motor direction
2. Place prop on motor shaft
3. Secure with prop nut (or self-tightening prop)
4. Tighten firmly (will self-tighten during flight)
5. Check each prop spins freely, doesn't hit frame

**Final Inspection**:
- [ ] All 4 props correct direction
- [ ] Props secure (wiggle test)
- [ ] No cracks or damage
- [ ] Battery secure and balanced
- [ ] All screws tight
- [ ] Transmitter on and bound
- [ ] GPS lock (10+ satellites)

## First Flight

### Step 19: Manual Test Flight

**Location**: Open field, grass surface, no obstacles, minimal wind

**Procedure**:
1. Place quad on level ground
2. Power transmitter, then quad
3. Wait for GPS lock (if using GPS modes)
4. ARM quad (props will spin slowly)
5. Slowly increase throttle
6. Lift to 1-2 meters altitude
7. **Hover** for 30 seconds (make small corrections)
8. Test forward, back, left, right (gentle inputs)
9. **Land** gently (reduce throttle slowly)
10. DISARM

**Success Criteria**:
- Quad lifts smoothly (no immediate flip)
- Responds correctly to inputs
- Hovers relatively stable
- No unusual vibrations or sounds
- Lands under control

**If Problems**:
- Immediate flip: Motor order or direction wrong → Land immediately, fix
- Strong drift: Recalibrate accelerometer/compass
- Oscillations: Reduce PID gains
- Low power: Check battery voltage, prop size vs motor KV

### Step 20: GPS Testing (If Applicable)

**After Successful Manual Flights**:
1. Test **Alt Hold**: Should maintain altitude automatically
2. Test **Loiter** (or PosHold): Should hold position
3. Test **RTL**: Fly 20m away, activate RTL, should return to launch point
4. **Only after RTL verified**: Attempt waypoint missions

## Mission Operations

### Autonomous Flight (ArduPilot/INAV)

**Mission Planning**:
1. Use Mission Planner or QGroundControl
2. Create simple 4-waypoint square pattern
3. Altitude: 15-20m (safe height)
4. Speed: Moderate (5 m/s typical)
5. Upload mission to FC

**Mission Flight**:
1. Manual takeoff to mission altitude
2. Verify GPS lock, home position
3. Switch to AUTO mode (mission starts)
4. Monitor progress, ready to switch to manual if needed
5. Mission completes with RTL or land

**Safety**:
- Always have manual override ready
- Visual observer required
- Abort mission if unexpected behavior
- Never fly beyond visual range (VLOS required)

## Educational Projects

### Beginner Projects
1. **Basic Flight Training**: Master manual control in Stabilize/Angle mode
2. **GPS Position Hold**: Test Loiter mode, measure drift over time
3. **Return to Home**: Test RTH from various distances
4. **Flight Time Optimization**: Test different batteries, props, weights

### Intermediate Projects
5. **Waypoint Missions**: Plan and execute autonomous square, triangle patterns
6. **Payload Integration**: Add camera, sensor, create data collection mission
7. **Competition Preparation**: Practice competition tasks (delivery, landing accuracy)
8. **Parameter Tuning**: Log flights, analyze data, optimize PID settings

### Advanced Projects
9. **DroneKit Programming**: Write Python scripts for custom missions
10. **Computer Vision**: Add Raspberry Pi, implement object detection
11. **Multi-Vehicle Operations**: Coordinate 2+ drones in shared mission
12. **Research Application**: Agricultural survey, mapping, inspection

## Maintenance

### After Each Flight
- Inspect props (cracks, chips → replace)
- Check battery voltage (should be >3.3V per cell)
- Tighten any loose screws
- Wipe off dirt/debris

### Every 5-10 Flights
- Download and review logs
- Check motor temps after flight (should be warm, not too hot to touch)
- Inspect frame for cracks
- Check solder joints for cracks
- Verify GPS antenna secure

### Battery Maintenance
- Don't over-discharge (<3.0V per cell damages battery)
- Store at 3.8V per cell (storage charge)
- Check for puffing before each flight
- Cycle batteries (use oldest first, rotate stock)

## Troubleshooting

### Build Issues
**No power**: Check battery voltage, connections, PDB solder joints
**Motors don't spin**: Verify ESC connections, FC configuration, arming disabled?
**GPS no lock**: Needs clear sky view, may take 5+ min first time, check antenna orientation

### Flight Issues
**Strong drift in GPS mode**: Compass interference or calibration, recalibrate outdoors
**Oscillations**: PIDs too high, reduce gains or use autotune
**Poor altitude hold**: Vibration affecting barometer, check FC damping
**Short flight time**: Battery degraded, too small, or excessive weight/aggressive flying

### Advanced Troubleshooting
- Review flight logs in Mission Planner
- Check vibration levels (should be <30 m/s² in ArduPilot logs)
- Verify GPS HDOP <2.0 for good accuracy
- Check motor balance (all should draw similar current)

## Safety & Compliance

### Operational Safety
- **Preflight checklist**: Use checklist every flight
- **Weather limits**: <15mph wind for GPS flights, no rain
- **Altitude**: Stay below 400ft AGL (US FAA limit)
- **Distance**: Maintain visual line of sight
- **People**: Never fly over crowds or moving vehicles

### Legal Compliance (US)
- **Registration**: Required for >250g (most educational quads)
- **Part 107**: Required for commercial/research use (age 16+)
- **Airspace**: Check for controlled airspace (LAANC authorization may be needed)
- **School Policy**: Follow institutional rules

**See**: [FAA Regulations Guide](../../safety-compliance/faa-regulations.md)

## Resources

### Hardware Files
- [Complete BOM (CSV)](../../../hardware/uav-designs/educational-quad-250/bom.csv)
- [Wiring Diagram](../../../hardware/uav-designs/educational-quad-250/wiring-diagram.png)
- [Assembly Guide (PDF)](../../../hardware/uav-designs/educational-quad-250/assembly-guide.pdf)

### Configuration Files
- [ArduPilot Parameter File](../../../code/flight-controllers/ardupilot-missions/educational-quad-params.param)
- [Mission Examples](../../../code/flight-controllers/ardupilot-missions/)

### Documentation
- [ArduPilot Documentation](../flight-controllers/ardupilot.md)
- [Programming Guide](../../programming/)
- [Troubleshooting](../../troubleshooting/)

### Community
- **ArduPilot Discourse**: Community forum for troubleshooting
- **GitHub Discussions**: Share your build, ask questions
- **Local Makerspaces**: Hands-on build help

## Next Steps

**After Mastering This Build**:
1. Advanced autonomous missions (delivery, search patterns)
2. Add [Payload Systems](../payload-systems.md) (camera, sensors)
3. Learn [DroneKit Programming](../../programming/flight-controller-programming/ardupilot-mavlink.md)
4. Try [Fixed-Wing Build](fixed-wing-trainer-build.md) for longer range
5. Compete in AUVSI SUAS or local drone competitions

---

**Back to**: [UAV Build Guides →](../index.md) | [UAV Systems →](../index.md)
