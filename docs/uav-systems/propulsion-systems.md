# UAV Propulsion Systems

Understanding propulsion systems is critical for building efficient, safe, and mission-appropriate UAVs. This guide covers motors, propellers, ESCs, and power systems for educational platforms.

## System Overview

The propulsion system consists of four interconnected components:

1. **Battery** → Provides electrical energy
2. **ESC (Electronic Speed Controller)** → Converts DC to 3-phase AC, controls motor speed
3. **Motor** → Converts electrical energy to mechanical rotation
4. **Propeller** → Converts rotation to thrust

## Brushless Motors

### Motor Specifications

#### KV Rating
**Definition**: RPM per volt (unloaded)

- **Low KV (1000-1500)**: High torque, large props, longer flight times
- **Medium KV (1500-2300)**: Balanced, general purpose, educational builds
- **High KV (2300-4000+)**: High speed, small props, racing/acrobatics

**Selection Guide**:
```
Large Props (9"+)    → Low KV (1000-1500)
Medium Props (6-8")  → Medium KV (1500-2300)
Small Props (3-5")   → High KV (2300-3500)
Micro Props (2-3")   → Very High KV (3500-8000+)
```

#### Motor Size
Expressed as AABB format: AA = stator diameter, BB = stator height (mm)

**Common Educational Sizes**:
- **0702-0802**: Micro quads (<100mm), indoor use
- **1104-1306**: Small quads (120-180mm), beginner outdoor
- **1806-2206**: Medium quads (200-280mm), educational/racing
- **2207-2306**: Standard racing (250mm), high performance
- **2212-2216**: Larger platforms (350-500mm), payload capable

#### Current Draw
- **Max Current**: Peak amperage motor can handle (brief duration)
- **Continuous Current**: Sustained current rating (important for flight time calculations)

**Example**: 2207 2400KV motor
- Typical draw: 25-30A continuous, 40A peak
- Pair with 35-40A ESC for safety margin

### Motor Selection by Platform

| Platform Type | Motor Size | KV Range | Example Models |
|--------------|------------|----------|----------------|
| Micro Quad (<100g) | 0702-0802 | 15000-20000 | Happymodel 0802 19000KV |
| Small Quad (100-200g) | 1104-1306 | 2800-4000 | EMAX 1106 4500KV |
| Educational Quad (250-500g) | 1806-2207 | 2000-2600 | EMAX RS2205 2300KV |
| Standard Quad (500g-1kg) | 2207-2306 | 1600-2400 | EMAX Eco II 2207 1700KV |
| Payload Quad (1-2kg) | 2212-2216 | 800-1200 | DYS D2212 1000KV |

### Motor Configuration

#### Rotation Direction
Motors must alternate rotation for stable flight:

**X-Configuration (Front-Forward)**:
```
  CW (2)    CCW (1)
      \      /
       [FC]
      /      \
 CCW (3)    CW (4)
```

#### Motor Wire Order
**Changing rotation**: Swap any TWO motor wires
- Standard: Black, Red, White → CCW
- Reversed: Red, Black, White → CW

!!! warning "Motor Direction"
    Always verify motor direction with props OFF before first flight. Use BLHeli Configurator or flight controller motor test.

## Propellers

### Propeller Specifications

#### Size Format: AABB or AABBCC
- **AA**: Diameter in inches
- **BB**: Pitch in inches (theoretical travel per revolution)
- **CC**: Number of blades (if present)

**Examples**:
- **5045**: 5-inch diameter, 4.5-inch pitch
- **6045x3**: 6-inch diameter, 4.5-inch pitch, tri-blade

#### Pitch Explained
- **Low Pitch (3-4")**: High RPM, better control, efficient, longer flight time
- **Medium Pitch (4-5")**: Balanced performance, most common
- **High Pitch (5-6"+)**: High speed, faster response, shorter flight time

#### Blade Count
- **2-Blade**: Most efficient, longest flight time, smooth
- **3-Blade**: Increased thrust, better control, slightly less efficient
- **4-Blade**: Maximum thrust, responsive, shortest flight time

### Propeller Selection Guide

| Platform Weight | Motor KV | Propeller Size | Best For |
|----------------|----------|----------------|----------|
| <100g | 15000-20000 | 1.5-2.5" tri-blade | Indoor micro quads |
| 100-250g | 3500-5000 | 3-4" tri-blade | Small quads, learning |
| 250-500g | 2000-2600 | 5-6" bi/tri-blade | Educational, racing, FPV |
| 500g-1kg | 1600-2000 | 7-8" bi-blade | Camera platforms, longer flight |
| 1-2kg | 1000-1500 | 9-11" bi-blade | Payload missions, research |

### Propeller Materials

**Plastic (Polycarbonate)**:
- Low cost, safe to handle
- Break easily (safety feature)
- Slightly less efficient
- **Best For**: Learning, indoor, frequent crashes

**Carbon Fiber/Reinforced**:
- Very durable, more expensive
- High efficiency
- Dangerous if damaged (sharp fragments)
- **Best For**: Competition, performance, advanced use

**Plastic with Reinforced Hub**:
- Good durability, moderate cost
- Balance of safety and performance
- **Best For**: Educational platforms

### Propeller Safety

!!! danger "Critical Safety"
    - NEVER test motors with propellers attached indoors
    - Always remove props when testing/configuring
    - Wear safety glasses when props are spinning
    - Keep body parts and loose items away from props
    - Use prop guards for classroom demonstrations
    - Inspect props before each flight for cracks/damage

## Electronic Speed Controllers (ESCs)

### ESC Functions
1. Convert battery DC voltage to 3-phase AC for motor
2. Control motor speed via PWM signal from flight controller
3. Often provide 5V BEC power for flight controller and receiver

### ESC Specifications

#### Current Rating
**Rule**: ESC current rating should be 20-30% higher than motor max continuous draw

**Example Calculation**:
- Motor: 25A continuous, 35A peak
- ESC Selection: 30A or 35A rated ESC

#### Firmware Options
- **BLHeli_S**: Standard, widely compatible, 8-bit
- **BLHeli_32**: Advanced features, 32-bit, better performance
- **SimonK**: Older, open-source, less common now

#### Special Features
- **Active Braking**: Quickly stops motor rotation
- **Regenerative Braking**: Recovers energy during prop deceleration
- **Current Sensing**: Provides current telemetry
- **Dshot Protocol**: Digital signal, faster and more reliable than PWM

### ESC Configurations

#### Individual ESCs (4-in-1 separated)
**Advantages**:
- Replace single ESC if one fails
- Easier to troubleshoot
- Flexible mounting

**Disadvantages**:
- More wiring complexity
- Slightly heavier
- More mounting space required

**Best For**: Beginner builds, educational platforms where repair is important

#### 4-in-1 ESC
All four ESCs on single board, integrated with PDB.

**Advantages**:
- Clean build, less wiring
- Lighter overall weight
- Integrated power distribution
- Compact mounting

**Disadvantages**:
- Single point of failure
- Must replace entire unit if one ESC fails
- More expensive

**Best For**: Racing, competition builds, advanced platforms

### ESC Protocols

Signal protocols between flight controller and ESC:

| Protocol | Speed | Reliability | Notes |
|----------|-------|-------------|-------|
| **Standard PWM** | 50-400Hz | Good | Legacy, universal compatibility |
| **Oneshot125** | 1-2kHz | Good | Faster response than PWM |
| **Multishot** | 2-4kHz | Good | Very fast, requires capable FC |
| **Dshot300/600** | Digital | Excellent | No calibration, telemetry capable |

**Recommendation**: Use Dshot600 for modern builds (2019+ hardware)

## Power Systems

### Battery Selection

#### Battery Chemistry
**LiPo (Lithium Polymer)**: Standard for UAVs
- High energy density
- High discharge rates
- Requires careful handling and charging
- **Most Common**: 3S (11.1V), 4S (14.8V), 6S (22.2V)

**LiHV (Lithium High Voltage)**:
- 4.35V per cell vs 4.2V for standard LiPo
- Slightly more capacity
- Requires compatible charger
- Less common in education

#### Battery Specifications

**Capacity (mAh)**: Total energy storage
- **500-850mAh**: Micro quads, 3-5 min flight
- **1000-1500mAh**: Small-medium quads, 5-10 min flight
- **1500-2200mAh**: Educational/racing quads, 8-15 min flight
- **2200-5000mAh**: Larger platforms, 15-30 min flight

**C-Rating**: Discharge rate capability
- Formula: Max Amps = Capacity (Ah) × C-Rating
- Example: 1500mAh, 75C = 1.5A × 75 = 112.5A max burst

**Recommended C-Ratings**:
- Slow flight/camera work: 25-50C
- Educational platforms: 45-65C
- Racing/acrobatics: 75-100C+

#### Cell Count Selection

| Cell Count | Voltage | Best For | Pros | Cons |
|-----------|---------|----------|------|------|
| **2S (7.4V)** | 7.4V | Micro indoor quads | Very safe, long flight time | Low power, limited wind capability |
| **3S (11.1V)** | 11.1V | Small-medium education | Good balance, widely available | Limited performance for advanced |
| **4S (14.8V)** | 14.8V | Standard racing/FPV | Excellent performance | Higher cost, shorter flight time |
| **6S (22.2V)** | 22.2V | High performance racing | Maximum power | Expensive, very short flight time |

**Educational Recommendation**: 3S for beginners, 4S for intermediate/advanced

### Power Distribution

#### Power Distribution Board (PDB)
Distributes battery power to ESCs and accessories.

**Features**:
- Multiple ESC pads (4-8+)
- Filtered 5V/12V BEC outputs
- Current/voltage sensing
- Integrated LED pads

**Selection**: Match current rating to total system draw + 30% margin

#### Wiring Gauge
Proper wire gauge prevents voltage sag and overheating:

| Current Draw | Wire Gauge (AWG) | Typical Use |
|--------------|------------------|-------------|
| 0-5A | 24-26 AWG | Signal wires, small accessories |
| 5-15A | 20-22 AWG | Small motor leads, sensor power |
| 15-30A | 16-18 AWG | Medium motor leads, ESC to motor |
| 30-60A | 12-14 AWG | Battery to PDB, high-current ESCs |
| 60-100A+ | 10-12 AWG | Large battery leads, multiple motors |

### Connectors

**Common Types**:
- **XT30**: 30A continuous, micro-small quads
- **XT60**: 60A continuous, most common for educational platforms
- **XT90**: 90A continuous, larger platforms
- **Deans**: 40-60A, older standard
- **EC3/EC5**: 30A/120A, less common

**Educational Recommendation**: Standardize on XT60 for 3S-4S platforms

## System Calculations

### Flight Time Estimation

**Basic Formula**:
```
Flight Time (minutes) = (Battery Capacity in mAh / Average Current Draw in mA) × 60 × Efficiency Factor

Efficiency Factor: 0.7-0.8 for multirotors
```

**Example**:
- Battery: 1500mAh 3S
- Average draw: 20A (20,000mA)
- Efficiency: 0.75

Flight Time = (1500 / 20000) × 60 × 0.75 = 3.375 minutes of full-throttle flight

Cruising flight (50-60% throttle) typically 2x this estimate = 6-8 minutes

### Thrust-to-Weight Ratio

**Formula**:
```
T/W Ratio = Total Thrust (all motors) / Total Weight (grams)
```

**Targets**:
- **2:1**: Minimum for stable flight
- **3:1**: Good general purpose, smooth camera work
- **4:1**: Excellent performance, educational platforms
- **5:1+**: Racing, acrobatics, very responsive

**Example Calculation**:
- 4× motors, 500g thrust each = 2000g total thrust
- Total weight: 500g
- T/W = 2000/500 = 4:1 (excellent)

### Power System Matching

Use eCalc or similar calculators to match components:
1. Enter frame weight estimate
2. Select motors
3. Select propellers
4. Calculator provides:
   - Expected thrust
   - Current draw
   - Flight time estimate
   - Efficiency metrics

**Online Calculator**: [eCalc.ch](https://www.ecalc.ch) (highly recommended)

## Troubleshooting

### Motor Not Spinning
1. Check ESC connections (signal, power, ground)
2. Verify motor direction in flight controller
3. Test ESC with known-good motor
4. Check for shorted motor windings (3× resistance checks should be equal)

### Motor Overheating
1. Propeller too large/high pitch for motor KV
2. ESC current limit too low
3. Motor damage (bad bearings)
4. Over-aggressive flying (constant full throttle)

### Vibrations
1. Balance propellers (propeller balancer tool)
2. Check for damaged propellers
3. Verify motor mounting is secure
4. Check for bent motor shafts
5. Replace worn motor bearings

### Short Flight Times
1. Battery degraded (check voltage sag under load)
2. Props too large/high pitch (excessive current draw)
3. Over-aggressive flying style
4. System weight too high for battery capacity
5. Battery not fully charged

## Educational Activities

### Lab Experiments

1. **KV vs Propeller Size Study**: Test same motor with different props, measure thrust and current
2. **Efficiency Comparison**: Compare flight times with 2-blade vs 3-blade props
3. **Thrust Stand Building**: Build Arduino-based thrust stand, characterize motors
4. **Battery Discharge Analysis**: Log voltage/current during flight, analyze discharge curves
5. **Motor Temperature Monitoring**: Infrared thermometer, correlate temperature with load

### Calculations Worksheet
Create student worksheets for:
- Calculating flight time from battery specs
- Determining appropriate ESC current rating
- Computing thrust-to-weight ratios
- Estimating total system power draw

## Safety & Maintenance

### Pre-Flight Checks
- [ ] All props securely attached, correct rotation
- [ ] Props undamaged (no cracks, chips, or bends)
- [ ] Motors spin freely by hand, no grinding
- [ ] ESCs securely mounted, no exposed solder joints
- [ ] Battery voltage correct (check cell balance)
- [ ] Connectors secure, no arcing damage visible

### Maintenance Schedule
- **After Each Flight**: Visual inspection of props and motors
- **Every 5 Flights**: Check motor screws, clean debris from motors
- **Every 10 Flights**: Inspect motor bearings, check for play
- **Every 25 Flights**: Clean motors with compressed air or contact cleaner

### Battery Safety
See [Battery Safety Guide](../safety-compliance/battery-safety.md) for complete information:
- Never leave charging batteries unattended
- Use LiPo-safe charging bags
- Store at 3.8V per cell for longevity
- Dispose of damaged/puffed batteries properly

## Component Recommendations

### Budget Educational Platform (3S, 250mm)
- **Motors**: EMAX RS2205 2300KV (4×) - ~$60
- **ESCs**: 30A BLHeli_S (4×) or 35A 4-in-1 - ~$40-60
- **Props**: 5045 Tri-blade (3-5 sets) - ~$15
- **Battery**: 1500mAh 3S 45C (2-3×) - ~$40-60
- **Total Propulsion**: ~$155-195

### Advanced Educational Platform (4S, 220mm)
- **Motors**: EMAX Eco II 2207 1700KV (4×) - ~$80
- **ESCs**: 45A 4-in-1 BLHeli_32 - ~$50
- **Props**: 5" Bi-blade (5 sets) - ~$25
- **Battery**: 1300mAh 4S 75C (3×) - ~$75
- **Total Propulsion**: ~$230

## Resources

### Vendors
- **GetFPV**, **RaceDayQuads**: Quality racing/educational components
- **HobbyKing**: Budget-friendly options, slower shipping
- **Amazon**: Quick shipping, higher prices, variable quality

### Tools
- **eCalc**: Propulsion system calculator
- **BLHeliSuite**: ESC configuration and firmware updates
- **ecalc.ch**: Motor thrust and efficiency database

### Further Reading
- **Oscar Liang Blog**: Comprehensive motor and propeller guides
- **Joshua Bardwell YouTube**: Detailed component explanations
- **RCGroups Forums**: Community troubleshooting and recommendations

---

**Next**: [Flight Controllers →](flight-controllers/) | [Back to UAV Overview →](index.md)
