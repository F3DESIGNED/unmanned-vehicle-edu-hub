# Micro Quadcopter Build Guide (<250g)

Build a sub-250g quadcopter perfect for indoor flight, classroom demonstrations, and learning basic flight principles without FAA registration requirements.

## Project Overview

**Skill Level**: Beginner
**Build Time**: 3-5 hours
**Flight Time**: 5-8 minutes
**Cost**: $100-180
**Best For**: Indoor flight, classroom use, learning basics

### Why Build This Platform?

- **FAA Exempt**: <250g = no registration required (US)
- **Safe**: Low mass, protected props, minimal damage potential
- **Indoor Capable**: Fly in gym, classroom (with permission)
- **Affordable**: Budget-friendly for classroom sets
- **Learning Platform**: Teaches fundamentals without overwhelming complexity

## Bill of Materials (BOM)

### Core Components

| Component | Specification | Quantity | Est. Cost | Notes |
|-----------|---------------|----------|-----------|-------|
| **Frame** | 100-120mm carbon fiber or plastic | 1 | $10-20 | Whoop-style or micro X-frame |
| **Motors** | 0802 15000-20000KV brushless | 4 | $24-32 | Check frame compatibility |
| **ESCs** | 6A or 4-in-1 (12-16A) | 4 or 1 | $20-35 | AIO (All-In-One) easier |
| **Flight Controller** | F4 or F7 (AIO with receiver) | 1 | $25-45 | Betaflight compatible |
| **Props** | 40mm or 2" tri-blade (ducted guards) | 2 sets | $6-10 | Spares essential |
| **Battery** | 1S 300-450mAh or 2S 300mAh LiPo | 2-3 | $15-25 | More batteries = more flight time |
| **Camera** | AIO camera/VTX (optional FPV) | 1 | $20-30 | Optional but recommended |
| **Receiver** | Built-in or external | 1 | $0-20 | Check FC compatibility |

**Total Core**: ~$120-210 (with FPV), ~$100-150 (no FPV)

### Tools Required

- Soldering iron (temperature controlled, ~350°C)
- Solder (60/40 or lead-free)
- Wire strippers
- Flush cutters
- Hex drivers (1.5mm, 2.0mm common)
- Multimeter (helpful for troubleshooting)
- Helping hands or PCB holder

### Consumables

- Heat shrink tubing
- Zip ties (small)
- Double-sided foam tape
- Threadlocker (blue, optional)
- Electrical tape

## Frame Assembly

### Step 1: Prepare Frame Parts

**Included in frame kit**:
- Bottom plate
- Top plate
- 4× motor mounts (or integrated into arms)
- Hardware (screws, standoffs)
- Prop guards (if whoop-style)

**Preparation**:
1. Lay out all parts, verify nothing missing
2. Check for damage or defects
3. Identify front orientation (usually marked or obvious)

### Step 2: Motor Installation

**Motor mounting**:
1. Place motor on mount, align screw holes
2. Apply tiny drop of threadlocker to screws (optional but recommended)
3. Tighten screws in X-pattern (prevents warping)
4. Don't over-tighten (carbon fiber or plastic can crack)

**Wire management**:
- Route wires toward center of frame
- Leave some slack (frame flexes in crashes)
- Don't let wires rub on sharp edges

**Motor direction** (verify later):
```
    Motor 1 (CCW)      Motor 2 (CW)
         \                  /
          \                /
            [Flight Controller]
          /                \
         /                  \
    Motor 4 (CW)       Motor 3 (CCW)
```

### Step 3: Bottom Plate Assembly

1. Secure motors to bottom plate (if not already attached via arms)
2. Install standoffs for FC mounting
3. Ensure all screws fully tightened

**Pro Tip**: Use electrical tape on underside of FC to prevent shorts on carbon fiber frames.

## Electronics Installation

### Step 4: ESC Wiring

#### Option A: 4-in-1 ESC (Recommended)

**Advantages**: Cleaner build, lighter, easier

**Installation**:
1. Solder battery lead (red/black) to BAT+/BAT- pads
2. Solder motor wires to ESC pads (note order: M1, M2, M3, M4)
   - Each motor has 3 wires, order doesn't matter initially (we'll fix direction later)
3. Mount ESC under FC using standoffs or stack

#### Option B: Individual ESCs

**Installation**:
1. Solder motor wires to each ESC (3 wires, any order)
2. Solder ESC signal wire to FC
3. Solder power (red) and ground (black) to PDB or battery lead
4. Secure ESCs to arms with heat shrink or zip ties

### Step 5: Flight Controller Installation

**FC Orientation**:
- Arrow or text indicates "FRONT"
- Ensure front faces forward on frame
- If misaligned, adjust in Betaflight configuration

**Mounting**:
1. Apply double-sided foam or soft mounts (vibration damping)
2. Route motor signal wires to FC
3. Connect battery leads to FC (if FC has power input)
4. DO NOT connect battery yet

**Soldering Connections**:
- Motor signal pads: M1, M2, M3, M4
- Battery pads: VBAT (+), GND (-)
- Receiver (if external): RX, TX, VCC, GND

**Wiring tips**:
- Tin pads before soldering
- Use flux for better solder flow
- Inspect for cold solder joints (shiny, firm = good)
- Check for shorts with multimeter

### Step 6: Camera & VTX (If FPV)

**AIO Camera/VTX** (simplest option):
1. Solder power (5V or VBAT, check specs)
2. Solder ground
3. Mount camera facing forward (slight upward tilt, 15-25°)
4. Secure with foam tape or camera mount

**Camera angle**:
- 0° = Hovering, easy to see
- 15-25° = Cruising, better for forward flight
- Adjust based on flight style

### Step 7: Receiver

**Built-in Receiver** (ELRS, Frsky, etc.):
- Already on FC, just bind to transmitter later

**External Receiver**:
1. Solder RX to FC TX pad (yes, reversed!)
2. Solder TX to FC RX pad
3. Solder VCC and GND
4. Mount receiver with double-sided tape
5. Position antenna away from carbon fiber (blocks signal)

## Final Assembly

### Step 8: Top Plate & Protection

1. Route all wires cleanly (avoid prop area)
2. Secure camera at front
3. Attach top plate over FC/ESC stack
4. Ensure no wires pinched
5. All screws tight but not stripped

### Step 9: Prop Guards (If Applicable)

**Whoop-style frames**:
- Ducted guards protect props and people
- Essential for indoor flight
- Snap or screw into place

**Open frames**:
- Consider adding guard rings (3D printed or purchased)
- Especially important for classrooms

### Step 10: Battery Mounting

**Micro builds**: Usually use battery pad with velcro strap

1. Adhere velcro to bottom (battery strap location)
2. Ensure battery doesn't obstruct props
3. Center battery for balanced CG
4. Test fit before first flight

## Software Configuration

### Step 11: Betaflight Setup

**Connect FC to Computer**:
1. USB cable to FC
2. Open Betaflight Configurator
3. Connect (select COM port)

**Flash Firmware** (if needed):
1. Firmware Flasher tab
2. Select target (FC model)
3. Flash latest Betaflight version

**Configuration Wizard**:
1. Select board orientation
2. Select receiver type
3. Configure ESC protocol (DShot600 recommended)
4. Set motor direction

### Step 12: Receiver Setup

**Bind Receiver**:
1. Put transmitter in bind mode
2. Power FC in bind mode (button or CLI command)
3. Wait for bind confirmation

**Channel Mapping**:
1. Receiver tab in Betaflight
2. Move sticks, verify channels respond
3. Typical: AETR1234

### Step 13: Motor Configuration

!!! danger "Remove Props for Motor Testing"

**Motor Order & Direction**:
1. Motors tab → Enable test mode
2. Spin each motor individually (low throttle)
3. Verify motor number matches quad position
4. Verify spin direction (CCW or CW per diagram)

**Fix Wrong Direction**:
- Enable "Motor direction is reversed" in Betaflight (DShot only)
- OR swap any TWO motor wires

### Step 14: Modes & Failsafe

**Flight Modes**:
- **Angle Mode**: Always on for beginners (self-leveling)
- **ARM**: Assign to switch (typically AUX1)
- **Air Mode**: Optional (for experienced pilots)

**Failsafe**:
1. Set throttle to low
2. Save failsafe settings
3. Test: Arm quad (props off), turn off radio, verify motors stop

### Step 15: PID Tuning

**For Beginners**: Use defaults or "Tune" preset

**If needed**:
- Start with "Race" or "Freestyle" preset
- Test fly, adjust if oscillations occur
- Reduce Master Multiplier if too twitchy

## Pre-Flight Checks

### Step 16: Ground Testing

**Battery Connection**:
1. Props still OFF
2. Connect battery (listen for boot sounds/music)
3. Check voltage on OSD or configurator

**Motor Test**:
1. Arm quad (motors should spin slowly)
2. Increase throttle slightly
3. All motors should spin smoothly
4. Disarm

**Range Check**:
1. Walk away with transmitter
2. Check control at 30 feet (typical indoor range)

### Step 17: First Flight Preparation

**Propeller Installation**:
1. Match prop direction to motor rotation
2. CW props: Right-hand thread (normal)
3. CCW props: Left-hand thread (reverse) OR specific CCW prop

**Prop identification**:
- Props labeled CW or CCW
- Or: Blade leading edge slants down in direction of rotation

**Installation**:
- Tighten securely (will vibrate loose otherwise)
- Don't over-tighten (plastic can strip)

**Safety Checklist**:
- [ ] Props correct direction
- [ ] All screws tight
- [ ] Battery secure
- [ ] Transmitter on, bound
- [ ] Clear flight area
- [ ] Eye protection (optional but recommended)

## Flying Your Micro Quad

### First Flight (Indoor)

**Location**: Open room, no obstacles (gym ideal)

**Procedure**:
1. Place quad on level surface
2. Power on transmitter
3. Connect battery to quad
4. Wait 5 seconds (FC initialization)
5. ARM quad (motor beep, props spin slowly)
6. Slowly increase throttle
7. Lift off to knee height
8. Hover, small corrections
9. Lower throttle gently, land
10. DISARM immediately after landing

**If Problems**:
- Flips immediately: Motor order or direction wrong
- Drifts strongly: Accelerometer calibration needed
- Won't arm: Check pre-arm conditions in Betaflight

### Flight Exercises (Progression)

1. **Hover Practice**: Maintain knee height for 30 seconds
2. **Basic Translation**: Forward, back, left, right (low altitude)
3. **Circles**: Fly slow circles around yourself
4. **Figure-8s**: Smooth figure-8 pattern
5. **Controlled Landing**: Land on target (piece of paper)

### Indoor Flying Tips

- Start low and slow
- Use Angle mode (self-leveling)
- Lower rates if too sensitive
- Keep away from walls initially
- Have spotter help with orientation

## Troubleshooting

### Build Issues

**Motors won't spin**:
- Check ESC connections (solder joints)
- Verify motor wires not shorted
- Test ESCs individually with multimeter

**Immediate crash on takeoff**:
- Motor order wrong: Verify in Betaflight motor test
- Motor direction wrong: Fix one or more motor directions
- Props wrong direction: Check prop installation

**Drifts to one side**:
- Recalibrate accelerometer (level surface)
- Check frame for bends/damage
- Verify motors all similar thrust (test individually)

### Flight Issues

**Short flight time (<3 minutes)**:
- Battery degraded: Check voltage under load
- Flying too aggressively: Smooth inputs extend flight
- Battery too small: Consider larger capacity

**FPV video static/interference**:
- Camera wires near motor wires (separate them)
- Bad antenna or damaged coax
- VTX channel conflict with nearby pilots

**Gets hot quickly**:
- Props too large for motors (check specs)
- Battery voltage too high for motors
- Motor bearings damaged

## Maintenance

### After Each Flight

- Visual inspection (cracks, loose screws)
- Check props for damage
- Wipe off any debris

### Every 5-10 Flights

- Tighten all screws (vibration loosens them)
- Check motor bearings (spin by hand, should be smooth)
- Inspect solder joints for cracks
- Clean motors if dusty/dirty

### Battery Care

- Don't over-discharge (<3.0V per cell)
- Store at 3.8V per cell (storage charge)
- Inspect for puffing before each flight
- Dispose properly if damaged (battery recycling)

## Educational Extensions

### STEM Integration

**Physics**:
- Calculate thrust-to-weight ratio
- Measure actual vs theoretical flight time
- Investigate angle of attack vs lift

**Math**:
- Battery capacity calculations
- Cost-benefit analysis of component choices
- Geometry of flight paths

**Engineering Design**:
- Optimize weight vs durability
- Design custom frame or parts (3D printing)
- Iterative testing and improvement

### Competitions

- **Precision Landing**: Land on target, closest wins
- **Flight Time Challenge**: Longest single flight
- **Obstacle Course**: Timed runs through hoops/gates
- **Build Quality**: Judged competition (craftsmanship, cable management)

## Safety Guidelines

**During Build**:
- Wear safety glasses when soldering
- Ventilate area (solder fumes)
- Unplug soldering iron when not in use
- Keep water/drinks away from electronics

**During Flight**:
- Eye protection recommended for pilot
- Clear area of bystanders (10-foot radius minimum)
- Never fly toward people
- Props OFF for all testing except flight
- Know how to disarm quickly (practice!)

**Battery Safety**:
- Never leave charging unattended
- Use LiPo bags or ammo cans for charging
- Don't charge damaged batteries
- See [Battery Safety Guide](../../safety-compliance/battery-safety.md)

## Resources

### Hardware Files
- [Micro Quad BOM (CSV)](../../../hardware/uav-designs/micro-quad-250/bom.csv)
- [Wiring Diagrams](../../../hardware/uav-designs/micro-quad-250/wiring-diagram.png)
- [3D Printable Parts](../../../hardware/uav-designs/micro-quad-250/CAD/)

### Configuration Files
- [Betaflight Configuration Dump](../../../code/flight-controllers/betaflight-configs/micro-quad.txt)

### Video Guides
- **YouTube**: Search "micro quad build" for visual guides
- **Joshua Bardwell**: Detailed micro builds
- **UAV Futures**: Budget micro quad builds

### Parts Sources
- **GetFPV**, **RaceDayQuads**: Quality components, fast shipping
- **Banggood**, **AliExpress**: Budget options, slower shipping
- **Amazon**: Quick shipping, moderate prices

## Next Steps

**After Mastering Micro Quad**:
1. Build larger [Educational Quadcopter](educational-quadcopter-build.md) (250-500g)
2. Add FPV goggles for immersive flight
3. Try [Betaflight](../flight-controllers/betaflight.md) advanced tuning
4. Experiment with different props/batteries
5. Design custom 3D printed parts

---

**Back to**: [UAV Build Guides →](../index.md) | [UAV Systems →](../index.md)
