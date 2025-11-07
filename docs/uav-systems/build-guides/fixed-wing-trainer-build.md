# Fixed-Wing Trainer Build Guide

Build a foam fixed-wing trainer platform for learning aerodynamics, long-range missions, and autonomous navigation with extended flight times.

## Project Overview

**Skill Level**: Intermediate-Advanced
**Build Time**: 8-12 hours
**Flight Time**: 30-60+ minutes
**Cost**: $200-400
**Best For**: Aerodynamics education, long-range missions, mapping/survey, advanced autonomy

### Why Fixed-Wing?

- **Long Flight Times**: 3-5× multirotor endurance
- **Efficiency**: Cover large areas (mapping, survey)
- **Aerodynamics**: Teaches lift, drag, airfoils, stability
- **Real Aviation Principles**: Translates to full-scale aircraft
- **Advanced Autonomy**: ArduPlane waypoint missions, autonomous launch/land

### Challenges vs Multirotors

- Requires runway or hand-launch
- Landing is more complex (needs skill or auto-land)
- Larger operating space needed
- Can't hover (always moving forward)
- Stall awareness critical

## Bill of Materials

### Airframe Options

**Option A: Foam Trainer Kit (Recommended for beginners)**
- Flite Test Simple Cub/Scout: $40-60 (laser-cut kit) + foam board
- Volantex Ranger EX: $120-150 (RTF minus electronics)
- Bixler 3: $80-100 (EPO foam ARF)

**Option B: Scratch Build** (Advanced)
- Foam board (Dollar Tree): $5-10
- Flite Test plans (free download)
- Hot glue, tape, hobby knife
- Cost: $10-20 for airframe

### Electronics (**~$180-300 total**)

| Component | Spec | Qty | Cost |
|-----------|------|-----|------|
| **Motor** | 1000-1400KV outrunner, 150-250W | 1 | $15-30 |
| **ESC** | 30-40A, BEC | 1 | $12-20 |
| **Propeller** | 8×6 to 10×6 | 2-3 | $3-6 ea |
| **Servos** | 9g micro servos | 4-5 | $3-5 ea |
| **Flight Controller** | Pixhawk Mini or Matek F405-Wing | 1 | $60-100 |
| **GPS** | UBLOX M8N + compass | 1 | $20-35 |
| **Battery** | 3S 2200mAh-3300mAh | 2 | $25-40 ea |
| **Receiver** | SBUS compatible | 1 | $15-30 |
| **Telemetry** | 915/433MHz radio | 1 | $20-40 |

### Additional Hardware
- Control horns, pushrods, linkages (usually in kit)
- Velcro straps, foam tape, CA glue
- Wire (20-22 AWG for servos, 14-16 AWG for power)
- XT60 connector, heat shrink
- Covering/paint (optional, for appearance)

## Airframe Assembly

### Step 1: Build Foam Airframe

**If Using Kit**: Follow manufacturer instructions carefully

**If Scratch Building (Flite Test)**:
1. Download plans from Flite Test website (free)
2. Transfer plans to foam board (carbon paper or print/glue method)
3. Cut with sharp hobby knife
4. Score fold lines (careful not to cut through)
5. Glue parts with hot glue or foam-safe CA

**Key Components**:
- Fuselage (main body)
- Wings (2 halves + center section)
- Horizontal stabilizer (tail plane)
- Vertical stabilizer (fin/rudder)
- Control surfaces (ailerons, elevator, rudder)

### Step 2: Control Surface Preparation

**Hinging**:
- Use tape hinge method (packing tape top & bottom)
- OR bevel edge, hinge with thin CA glue
- Test: Control surfaces should move freely, no binding

**Control Horns**:
- Install on elevator, rudder, ailerons
- Use CA glue or screws (comes with kit usually)
- Position where pushrod angle will be optimal

**Servo Installation**:
- Cut servo wells in wing/fuselage
- Secure servos with screws or hot glue
- Route servo wires to receiver location

### Step 3: Power System Installation

**Motor Mount**:
- Firewall (front of fuselage) must be reinforced
- Use plywood or carbon fiber plate
- Mount motor with 4 screws, check alignment

**Motor Angle**:
- 0-3° down thrust (helps level flight)
- 0-2° right thrust (counters prop torque)
- Adjust with shims if needed

**ESC Mounting**:
- Inside fuselage, airflow for cooling
- Wire to motor (any order initially, we'll reverse if needed)
- Battery connector accessible (usually rear of fuselage for CG)

**Propeller**:
- Install AFTER all testing complete
- Match prop size to motor KV (check manufacturer recommendation)

## Electronics Integration

### Step 4: Flight Controller Installation

**Location**: Center of wing or forward fuselage, near CG

**Mounting**:
- Pixhawk: Use vibration dampers (included foam pads)
- Matek: Moderate damping, double-sided foam tape
- Arrow/Forward marking must point nose direction

**Wiring**:
- Servos: Connect to servo rail or individual outputs
  - Channel 1: Aileron (or elevon mix)
  - Channel 2: Elevator (or elevon mix)
  - Channel 3: Throttle (to ESC signal wire)
  - Channel 4: Rudder
- ESC: Connect to throttle output
- Battery: Connect to power input (through power module if Pixhawk)

### Step 5: GPS & Sensors

**GPS Mount**:
- Top of fuselage or wing, clear view of sky
- Elevated if possible (foam block or mast)
- Arrow points forward
- Away from motor/ESC (electrical noise)

**Compass Alignment**:
- Critical for autonomous flight
- Note orientation if GPS mounted at angle
- Configure in software

**Airspeed Sensor** (Optional but Recommended):
- Pitot tube on nose or wing leading edge
- Measures airspeed (critical for auto-land, stall prevention)
- Connect to I2C port on FC

### Step 6: Receiver & Telemetry

**Receiver**:
- Mount in fuselage with foam (vibration isolation)
- Antennas external (exit fuselage, no metal blocking)
- Connect to FC UART (SBUS) or PWM channels

**Telemetry Radio**:
- Mount with antenna external
- Connect to TELEM port on FC
- Allows mission planning, real-time monitoring

### Step 7: Center of Gravity (CG)

**Critical for Fixed-Wing**: CG too far forward = nose-heavy, difficult to flare. CG too far back = tail-heavy, unstable, dangerous.

**CG Location**: Usually 25-30% back from leading edge of wing (check plans)

**Balancing**:
1. Support plane at CG point (fingers under wing)
2. Plane should balance level or slightly nose-down
3. Adjust battery position forward/back to achieve CG
4. Add weight to nose if needed (washers, fishing weights)

**CG Test**:
- Before first flight, verify CG with full flight battery
- Re-check after any modifications

## Software Configuration (ArduPilot Plane)

### Step 8: Firmware & Initial Setup

**Install ArduPilot Plane**:
1. Connect FC via USB
2. Mission Planner or QGroundControl
3. Install Firmware → Select "Plane"

**Frame Type**:
- Select airframe type (normal plane, flying wing, etc.)

**Servo Configuration**:
- **Function Assignment**: Assign servo outputs
  - Servo 1: Aileron
  - Servo 2: Elevator
  - Servo 3: Throttle
  - Servo 4: Rudder
- **Servo Reversal**: Test each servo, reverse if needed
- **Servo Limits**: Set min/max to prevent binding

**Elevon Mixing** (Flying Wings):
- Enable elevon mixing in parameters
- Combine aileron + elevator into left/right elevons

### Step 9: Calibrations

**Accelerometer**: Level plane on table, run calibration (6 orientations)
**Compass**: Outdoor calibration, rotate in all axes
**Radio**: Calibrate transmitter (move all sticks to extremes)
**ESC**: May need throttle calibration (full throttle arm procedure)

### Step 10: Critical Plane Parameters

**Airspeed (if sensor installed)**:
- `ARSPD_TYPE`: Set to sensor type (MS4525 common)
- `ARSPD_AUTOCAL`: Enable for automatic calibration
- `ARSPD_FBW_MIN`: Minimum airspeed (m/s), above stall speed
- `ARSPD_FBW_MAX`: Maximum airspeed (m/s), safe cruise speed

**Cruise Settings**:
- `TRIM_ARSPD_CM`: Cruise airspeed (cm/s), typical 12-15 m/s
- `TRIM_THROTTLE`: Cruise throttle %, usually 50-70%

**Stall Prevention**:
- `STALL_PREVENTION`: Enable (highly recommended)
- Prevents stalling in autonomous modes

**RTL & Landing**:
- `RTL_ALTITUDE`: Return altitude (m), safe clearance
- `LAND_FLARE_ALT`: Altitude to flare for landing (m)
- `LAND_FLARE_SEC`: Seconds of flare before touchdown

### Step 11: Flight Modes

**Recommended Mode Setup**:
- **Manual**: Direct control, no stabilization (advanced only)
- **Stabilize (FBWA)**: Stabilized, easiest for learning
- **Cruise (FBWB)**: Maintains altitude and airspeed
- **Auto**: Autonomous waypoint missions
- **RTL**: Return to launch, auto-land
- **Loiter**: Circle at current position

**For Training**: Use Stabilize (FBWA) almost exclusively at first

## Pre-Flight Testing

### Step 12: Control Surface Checks (Props OFF)

**Servo Test**:
1. Power on transmitter, then plane
2. Move sticks, verify correct control surface response:
   - Roll right → right aileron up, left down
   - Pitch forward → elevator down
   - Rudder right → rudder right
3. Check travel (should reach full deflection without binding)

**Reverse if Needed**:
- Use transmitter channel reverse, OR
- Use ArduPilot servo reverse parameter

### Step 13: Motor Test (Props OFF!)

1. Arm plane (throttle to zero, arm switch)
2. Slowly increase throttle
3. Motor should spin in correct direction (check prop airflow direction)
4. If wrong, swap any TWO motor wires

### Step 14: Ground Roll Test (Props ON, Ready to Fly)

**Purpose**: Verify control surfaces respond correctly at speed

1. Open area (grass field)
2. Hand-hold plane facing into wind
3. Apply 1/2 throttle
4. Test controls (roll, pitch, yaw) - should respond correctly
5. Power off

**This test catches servo reversals before flight damage!**

## First Flight

### Step 15: Hand Launch Technique

**Traditional Method** (Recommended for first flights):
1. Hold plane by fuselage, thumb on back, fingers underneath
2. Face into wind
3. Full throttle, 2-second delay (build RPM)
4. Throw firmly forward and slightly upward (like football spiral)
5. Release controls briefly (let plane stabilize)
6. Gentle corrections as needed

**DO NOT**:
- Throw straight up (will stall)
- Throw while pulling back on stick (instant stall)
- Launch downwind or in strong gusts

### Step 16: First Flight Pattern

**Takeoff**:
1. Hand launch as above
2. Immediately check for correct flight attitude
3. Climb to safe altitude (50-100m) before attempting maneuvers

**Trim Adjustments**:
- Plane should fly relatively straight with centered sticks
- Use transmitter trim to adjust (or trims in ArduPilot)
- Note: Wind will affect trim

**Basic Maneuvers**:
1. **Straight & Level**: Practice maintaining altitude and heading
2. **Gentle Turns**: Bank 20-30°, coordinate with slight up-elevator
3. **Figure-8s**: Practice constant turns in both directions
4. **Altitude Changes**: Climb and descend smoothly

**Landing**:
1. Reduce throttle (50-25%)
2. Descend gradually into wind
3. Line up with landing area (grass field)
4. Reduce throttle more as approaching ground
5. Gentle up-elevator to flare (nose up, slow descent)
6. Touch down on wheels or belly (depending on design)
7. Cut throttle immediately

**If Problems**:
- **Stall Warning**: Nose points up, airspeed drops → Full throttle, lower nose
- **Spiral**: Level wings immediately, then pull out of dive
- **Loss of Orientation**: Climb to safe altitude, observe from side to reorient

## Autonomous Operations

### Step 17: First GPS Flight

**After Manual Flight Proficiency**:
1. Test **Loiter** mode: Fly to safe altitude, switch to Loiter (should circle)
2. Test **RTL**: Fly away 100m, switch to RTL (should return and circle home)
3. Practice **Auto-Land**: Use RTL to auto-land (monitor closely, ready to override)

### Step 18: Waypoint Missions

**Mission Planning**:
1. Mission Planner → Flight Plan
2. Click map to add waypoints
3. Set altitude (100m+ for safety)
4. Add takeoff and land commands
5. Upload to plane

**Mission Flight**:
1. Manual takeoff and climb
2. Switch to **AUTO** mode (mission begins)
3. Monitor progress, ready to revert to manual
4. Plane flies waypoints, lands automatically (if programmed)

**Educational Missions**:
- Survey patterns (parallel lines, grid)
- Perimeter flights (geofence testing)
- Search patterns (expanding square)
- High-altitude endurance tests

## Educational Activities

### Physics & Math Integration
1. **Lift & Drag**: Measure flight characteristics, calculate coefficients
2. **Endurance**: Plot flight time vs battery capacity, weight
3. **Range**: Calculate max range based on cruise speed and battery
4. **Wind Triangle**: Navigation in wind, ground speed vs airspeed

### Engineering Projects
5. **Wing Design**: Test different wing shapes (flat vs airfoil)
6. **CG Effects**: Document handling changes with CG position
7. **Payload Integration**: Add camera, GPS logger, sensors
8. **Efficiency Optimization**: Best cruise speed, prop selection

### Autonomous Applications
9. **Aerial Photography**: GPS-planned mission, camera trigger waypoints
10. **Mapping**: Survey grid pattern, post-process images (photogrammetry)
11. **Long-Range**: Maximize range/endurance missions
12. **Search & Rescue Sim**: Autonomous search patterns

## Maintenance & Troubleshooting

### Post-Flight
- Inspect airframe (cracks, loose parts)
- Check motor and ESC temperature
- Verify control surfaces still secure
- Charge batteries

### Common Issues
**Plane won't climb**: CG too far forward, motor underpowered, or too heavy
**Unstable, wobbles**: CG too far back (dangerous!) or control surfaces loose
**Stalls easily**: Airspeed too low, CG too far back, or wing damage
**Turns one direction**: Trim needed, or motor angled incorrectly
**Short flight times**: Battery too small, inefficient flight, or wind

### Crash Repair (Foam)
- Hot glue for foam repairs (quick, easy)
- Reinforce breaks with packing tape
- Replace damaged control surfaces
- Check electronics for damage before next flight

## Safety & Legal

### Fixed-Wing Specific Safety
- **Larger Operating Area**: Need 2-3× space vs multirotors
- **Landing Hazards**: Plane can't stop mid-air, plan landing zone carefully
- **Higher Speeds**: 30-60 mph cruise = more dangerous than slow multirotor
- **Propeller**: Spinning prop very dangerous, never reach toward running motor

### Legal (US)
- **Registration**: Required if >250g
- **Part 107**: Required for commercial/research use
- **Airspace**: Often same altitude restrictions as multirotors
- **Pilot Skill**: Ensure pilot competent before GPS flights

See: [Safety & Compliance](../../safety-compliance/)

## Resources

### Build Plans & Kits
- **Flite Test**: Free plans, beginner-friendly foam builds
- **Volantex**: RTF/ARF affordable trainers
- **Sonicmodell**: High-quality EPO trainers

### Software & Guides
- [ArduPilot Plane Documentation](https://ardupilot.org/plane/)
- [Fixed-Wing Setup Guide (Mission Planner)](https://ardupilot.org/plane/docs/first-flight-landing-page.html)

### Hardware Files
- [Fixed-Wing BOM](../../../hardware/uav-designs/fixed-wing-trainer/bom.csv)
- [Assembly Guide](../../../hardware/uav-designs/fixed-wing-trainer/assembly-guide.pdf)

### Configuration Files
- [ArduPlane Parameter File](../../../code/flight-controllers/ardupilot-missions/fixed-wing-params.param)

---

**Back to**: [UAV Build Guides →](../index.md) | [UAV Systems →](../index.md)
