# Preventive Maintenance

Regular inspection and maintenance procedures to prevent problems before they occur. Establish maintenance schedules, inspection checklists, and record-keeping systems.

## Maintenance Philosophy

**Prevention vs Reaction:**
- 5 minutes of prevention saves hours of repair
- Scheduled maintenance prevents unexpected failures
- Regular inspection catches problems early
- Documentation tracks vehicle history

**Educational Benefits:**
- Builds systematic thinking
- Develops inspection skills
- Reinforces component knowledge
- Prevents frustrating failures

## Pre-Flight Inspection

### Every Flight Checklist

**Complete before every flight - no exceptions:**

#### Visual Inspection (2 minutes)
```
[ ] Frame: No cracks, breaks, or loose parts
[ ] Props: Correct installation, no damage, secure
[ ] Motors: Spin freely, no grinding, bells secure
[ ] Wiring: No exposed conductors, secure connections
[ ] Battery: No swelling, damage, or excessive heat
[ ] Antennas: Present, undamaged, properly oriented
```

#### Systems Check (3 minutes)
```
[ ] Power On: Normal startup sequence, LEDs correct
[ ] RC Link: Transmitter connected, RSSI good
[ ] GPS: Lock achieved, adequate satellites
[ ] Sensors: IMU/compass/baro initialized
[ ] Camera/VTX: Video signal clear (if FPV)
[ ] Mode Switches: All modes accessible
[ ] Arming: Arms successfully, no pre-arm errors
```

#### Control Check (2 minutes)
```
[ ] Roll: Right stick right = right tilt
[ ] Pitch: Right stick forward = forward tilt
[ ] Yaw: Left stick right = clockwise rotation
[ ] Throttle: Responds smoothly, full range
[ ] Trims: Centered, no excessive trim needed
[ ] Failsafe: Tested and confirms to RTL/land
```

#### Final Checks (1 minute)
```
[ ] Battery: Voltage sufficient for planned flight
[ ] Propellers: Correct rotation direction
[ ] Airspace: Clear, permission obtained if needed
[ ] Observers: Positioned, briefed on procedures
[ ] Emergency Plan: Landing zones identified
```

!!! tip "Make it Mandatory"
    Require students to complete checklist every time. Use printed forms initially, then transition to habit.

## Post-Flight Inspection

### After Each Flight Session (5 minutes)

**Immediate Post-Flight:**
```
[ ] Disarm and disconnect battery
[ ] Check for excessive heat (motors, ESCs, battery)
[ ] Look for new damage
[ ] Wipe down (remove dirt, grass, debris)
[ ] Check for loose screws
```

**Detailed Check:**
```
[ ] Props: Nicks, cracks, balance issues
[ ] Motors: Bearing play, bell wobble, wire wear
[ ] Frame: New cracks, stress marks
[ ] Solder Joints: Cracks, cold joints
[ ] Connectors: Wear, melting, fit
[ ] Battery: Voltage, temperature, condition
```

**Documentation:**
```
[ ] Flight time logged
[ ] Issues noted
[ ] Next maintenance needed
[ ] Performance observations
```

## Weekly Detailed Inspection

### For Actively Flown Vehicles (30 minutes)

#### Mechanical Inspection

**Frame:**
- Inspect all joints and connection points
- Look for cracks in carbon (white stress marks)
- Check for loose standoffs
- Verify arm alignment

**Motors:**
```
Test:
1. Spin by hand - should be smooth, no grinding
2. Check for play - minimal end-to-end movement
3. Inspect bell - should be secure, no wobble
4. Examine wires - no fraying at solder joints

Replace if:
- Grinding or rough spinning
- Excessive play
- Bell loose or damaged
- Wires damaged
```

**Props:**
```
Inspect:
- Cracks, especially at hub
- Nicks on leading edge
- Warping or bending
- Balance (if possible)

Replace if:
- Any cracks
- Significant nicks
- Bent or warped
- After ~30-50 flights even if look OK
```

#### Electrical Inspection

**Battery:**
```
Check:
- Voltage of each cell (should be balanced)
- Physical condition (no swelling, damage)
- Connector condition (no melting, wear)
- Internal resistance if tester available

Retire if:
- Cell imbalance >0.1V
- Any swelling
- Capacity dropped >20%
- IR increased significantly
```

**Wiring and Connections:**
```
Inspect:
- All solder joints for cracks
- Wires for chafing or cuts
- Connectors for melting or damage
- Heat shrink for integrity

Repair/Replace:
- Reflow cracked joints
- Re-solder corroded connections
- Add strain relief where needed
- Replace damaged connectors
```

**ESCs:**
```
Check:
- No burn marks or discoloration
- Capacitor condition (if visible)
- Wires secure
- Not excessively hot after flights
```

#### Software Check

**Firmware:**
- Current version documented
- Check for critical updates
- Review changelog
- Update if significant fixes

**Configuration:**
- Backup current parameters
- Verify critical settings unchanged
- Check for parameter drift (rare)
- Test all modes

#### Functional Testing

**Bench Test:**
```
Props OFF:
[ ] All motors spin in motor test
[ ] Correct direction
[ ] Similar sound/feel
[ ] No unusual vibration
[ ] ESCs initialize properly
```

**Sensor Verification:**
```
[ ] GPS acquires lock
[ ] Compass heading accurate
[ ] IMU level indication correct
[ ] Barometer reading reasonable
[ ] Voltage sensing accurate
```

## Monthly Maintenance

### Comprehensive Inspection (1-2 hours)

#### Deep Cleaning
- Remove all dust and debris
- Clean motors (compressed air, carefully)
- Clean flight controller and ESCs
- Inspect for corrosion
- Re-apply conformal coating if needed

#### Precision Checks

**Motor Bearings:**
```
Test:
1. Remove props
2. Hold motor, spin bell
3. Feel for roughness or binding
4. Listen for grinding

Consider Replacing:
- After 100+ flight hours
- If rough or noisy
- If excessive play develops
- Preventively for critical missions
```

**Frame Integrity:**
```
Stress Test:
1. Gentle flex test on arms
2. Check center plate for cracks
3. Verify no delamination
4. Look for hidden cracks

Racing/Hard Use:
- Replace arms after heavy crashes
- Check critical stress points
- Don't wait for failure
```

**Electronic Components:**
```
Visual Inspection:
- Capacitors: No bulging, leaking
- Connectors: No corrosion
- PCBs: No cracks or burns
- ICs: No damage or overheating signs
```

#### Calibration Verification

**IMU:**
- Recalibrate if drift noticed
- Verify level indication
- Check in configurator

**Compass:**
- Test for interference
- Recalibrate if variance high
- Verify heading accuracy

**ESCs:**
- Check for timing drift
- Verify protocol settings
- Update firmware if available

**RC System:**
- Check transmitter trims
- Verify failsafe
- Test range (30m+ walk test)
- Replace transmitter battery if weak

## Seasonal / Annual Maintenance

### Deep Overhaul (3-4 hours)

**Complete Disassembly (if needed):**
- Document configuration
- Photograph wiring
- Label all connections
- Systematic disassembly

**Component-Level Inspection:**
- Test each component individually
- Replace wear items prophylactically
- Upgrade firmware/software
- Clean all electronic components

**Reassembly:**
- Fresh solder on critical joints
- New heatshrink where needed
- Improved cable routing if possible
- Update documentation

**Testing:**
- Complete bench test
- Hover test flight
- Full function check
- Log analysis

## Component Lifecycle Tracking

### Replacement Schedules

| Component | Replace After | Or When |
|-----------|---------------|---------|
| Props | 30-50 flights | Any damage, imbalance |
| Battery | 200-300 cycles | Swelling, low capacity |
| Motors | 200+ hours | Rough bearings, damage |
| Motor Bearings | 100-150 hours | Grinding, play |
| ESCs | As needed | Failure, burning, glitching |
| Frame Arms | After hard crash | Any cracks |
| Camera | As needed | Image quality degrades |
| VTX | As needed | Failure, poor video |

### Tracking System

**Maintenance Log Template:**

```markdown
# Vehicle Maintenance Log

## Vehicle Information
- **ID:** Vehicle Name/Number
- **Type:** Quadcopter/Rover/etc.
- **Frame:** Model
- **Build Date:**

## Component Inventory
| Component | Brand/Model | Serial | Install Date | Flight Hours |
|-----------|-------------|--------|--------------|--------------|
| FC | | | | |
| ESC | | | | |
| Motors | | | | |
| Battery 1 | | | | Cycles: |
| Battery 2 | | | | Cycles: |

## Flight Time Log
| Date | Duration | Conditions | Issues | Total Hours |
|------|----------|------------|--------|-------------|
| | | | | |

## Maintenance Record
| Date | Type | Work Performed | Parts Replaced | Technician |
|------|------|----------------|----------------|------------|
| | Pre-flight | | | |
| | Weekly | | | |
| | Monthly | | | |

## Incident Log
| Date | Type | Description | Damage | Resolution |
|------|------|-------------|--------|------------|
| | | | | |
```

**Digital Tracking:**
- Spreadsheet or database
- Track per vehicle and per component
- Alert when service due
- Historical analysis

## Tools and Supplies

### Essential Maintenance Tools

**Inspection:**
- Multimeter
- Magnifying glass or loupe
- LED flashlight
- Camera for documentation

**Maintenance:**
- Hex driver set (1.5mm, 2.0mm, 2.5mm, 3.0mm)
- Screwdriver set (Phillips and flathead)
- Tweezers (ESD-safe)
- Wire cutters
- Wire strippers

**Cleaning:**
- Compressed air
- Isopropyl alcohol (90%+)
- Soft brushes
- Lint-free cloths
- Cotton swabs

**Repair:**
- Soldering iron and solder
- Heat shrink tubing
- Spare wire (16-20 AWG)
- Threadlocker (blue, removable)
- Zip ties
- Electrical tape

### Spare Parts Inventory

**Critical Spares:**
```
For Educational Program:
- Props: 20+ sets
- Motors: 2-4 spare
- ESCs: 2 spare or 1 spare 4-in-1
- Battery: 20% spare capacity
- Frame arms: 4+ spare
```

**Consumables:**
```
Keep on Hand:
- Solder
- Heat shrink (various sizes)
- Wire (various gauges)
- Threadlocker
- Zip ties
- XT60/XT30 connectors
- Screws (M3, various lengths)
- Standoffs
```

## Educational Integration

### Student Maintenance Program

**Benefits:**
- Ownership and responsibility
- Practical skills development
- System understanding
- Career skills (inspection, documentation)

**Structure:**
1. **Assign Vehicle** - Student or team responsible
2. **Training** - How to inspect properly
3. **Schedule** - Regular maintenance slots
4. **Documentation** - Require logging
5. **Oversight** - Teacher verification

### Maintenance Curriculum

**Lesson Plans:**

**Week 1: Introduction to Maintenance**
- Why maintenance matters
- Types of maintenance
- Inspection techniques
- Documentation

**Week 2: Pre-Flight Inspections**
- Checklist development
- Systematic approach
- Common issues
- Practice inspections

**Week 3: Component Inspection**
- Motors and props
- Electronics
- Structure
- Batteries

**Week 4: Troubleshooting**
- Diagnostic approach
- Testing procedures
- When to replace vs repair
- Parts sourcing

**Week 5: Preventive Maintenance**
- Scheduled maintenance
- Lifecycle tracking
- Inventory management
- Cost analysis

### Assessment

**Rubric:**

| Skill | Novice | Proficient | Expert |
|-------|--------|-----------|--------|
| Inspection Completeness | Misses obvious issues | Finds most problems | Catches subtle issues |
| Documentation | Incomplete or missing | Adequate records | Comprehensive logs |
| Diagnosis | Guesses randomly | Systematic approach | Accurate root cause |
| Repair | Needs constant help | Works independently | Teaches others |

## Safety in Maintenance

### Electrical Safety

```
ALWAYS:
- Disconnect battery before working
- Check battery is removed
- Double-check polarity
- Use smoke stopper on first power-up

NEVER:
- Connect USB and battery simultaneously (unless FC approved)
- Work on powered system
- Touch spinning props
- Short circuit battery
```

### Chemical Safety

```
Batteries:
- Handle with care
- No puncturing
- Dispose properly
- Watch for swelling

Solvents:
- Good ventilation
- No flames
- Proper disposal
- Skin protection if needed

Solder:
- Ventilation required
- Wash hands after
- No lead solder contact with food
```

### Tool Safety

```
Soldering Iron:
- 300-400°C surface
- Proper stand
- Cool before storing
- Supervise students

Compressed Air:
- Eye protection
- Don't aim at people
- Use proper pressure
- Careful around electronics

Cutting Tools:
- Always cut away from body
- Sharp tools safer than dull
- Proper storage
- Supervise use
```

## Cost Management

### Budgeting for Maintenance

**Annual Per-Vehicle Estimate:**
```
Consumables: $50-100
Props: $50
Replacement parts: $100-200
Batteries: $100-150 (rotating)
Total: $300-450/vehicle/year active use
```

**Reducing Costs:**
- Group purchases (bulk pricing)
- Preventive maintenance (avoid failures)
- Student repairs (learning + cost savings)
- Proper handling (reduce damage)
- Good documentation (avoid redundant replacement)

### Grant and Funding

**Maintenance in Grant Proposals:**
- Include ongoing costs, not just initial
- Typical: 20-30% of build cost annually
- Consumables and replacement parts
- Testing and calibration equipment

## Next Steps

- [Hardware Issues](hardware-issues.md) - When maintenance finds problems
- [Safety Procedures](../safety-compliance/safety-procedures.md) - Safe operation
- [Build Guides](../uav-systems/build-guides/educational-quadcopter-build.md) - Initial construction
- [Safety Incident Response](safety-incident-response.md) - After accidents

## Resources

- Component manufacturer maintenance guides
- Community maintenance best practices
- Inspection checklists (downloadable templates)
- Maintenance scheduling software
- Parts suppliers and bulk ordering
