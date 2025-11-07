---
title: Battery Safety - LiPo and Lithium Batteries
description: Critical safety information for handling, charging, storing, and disposing of lithium polymer batteries
---

# Battery Safety

!!! danger "CRITICAL SAFETY INFORMATION"
    **Lithium Polymer (LiPo) batteries can catch fire or explode if mishandled.** This page contains essential information that could prevent serious injury, property damage, or death. Read completely before using any LiPo battery.

## Why Battery Safety Matters

LiPo batteries are used in most unmanned vehicles because they provide:
- High energy density (lots of power, small size)
- High discharge rates (powerful motors)
- Lightweight design

**However, they also present serious fire risks:**
- Store tremendous energy in small package
- Can ignite if punctured, overcharged, or damaged
- Fires are intense, difficult to extinguish
- Toxic fumes when burning
- Can reignite after appearing extinguished

**Real incidents:**
- House fires from charging LiPos
- Vehicle fires from storing LiPos
- Severe burns from battery explosions
- Property damage exceeding $100,000+

**Following safety procedures is non-negotiable.**

## Understanding LiPo Batteries

### Basic Structure

**Components:**
- **Cells:** Individual 3.7V nominal units, connected in series (S) or parallel (P)
- **Pouch:** Flexible aluminum-laminated wrapper
- **Balance connector:** Monitors individual cell voltages
- **Main connector:** High-current discharge (XT60, Deans, etc.)

**Common Configurations:**
- **1S:** 3.7V nominal (4.2V max) - micro drones
- **2S:** 7.4V nominal (8.4V max) - small drones
- **3S:** 11.1V nominal (12.6V max) - common for 5" quads
- **4S:** 14.8V nominal (16.8V max) - higher performance
- **6S:** 22.2V nominal (25.2V max) - racing, large platforms

### Key Specifications

**Capacity (mAh):** How much energy stored
- 1000mAh = 1Ah (amp-hour)
- Higher capacity = longer flight time, heavier battery

**C-Rating:** How fast battery can safely discharge
- Formula: Max current = Capacity (Ah) × C-Rating
- Example: 1500mAh (1.5Ah) × 50C = 75A max discharge
- Always choose C-rating above your actual draw

**Voltage Ranges (per cell):**
- **Charged (storage):** 3.8V-3.85V (for storage)
- **Fully charged:** 4.2V (for immediate use)
- **Nominal:** 3.7V (average during use)
- **Warning:** 3.5V (land immediately)
- **Cutoff:** 3.0V (absolute minimum, damage occurs)
- **Dangerous:** Below 3.0V (permanent damage, fire risk)

## Hazard Recognition

### Signs of Damaged Battery - DO NOT USE

🔴 **CRITICAL - Dispose Immediately:**
- **Swelling/puffing** (bulging pouch)
- **Puncture or tear** in outer wrapper
- **Leaking** electrolyte
- **Deformed** shape
- **Burnt smell** or discoloration
- **Cells at very different voltages** (>0.1V difference)

🟡 **WARNING - Inspect Carefully:**
- Wrappers coming loose
- Connectors damaged
- Excessive heat during charge/discharge
- Rapid voltage drop under load
- Longer than normal charge times

!!! danger "Swollen Battery = Immediate Disposal"
    A puffed/swollen battery is a battery in the process of failing. The buildup of gas inside indicates chemical breakdown. **Do not charge, do not use, dispose of immediately following safe disposal procedures.**

## Charging Safety

### Critical Charging Rules

1. **NEVER leave charging unattended**
   - Stay in the same room
   - Check every 5-10 minutes
   - Set timer as reminder

2. **ALWAYS use LiPo-specific charger**
   - Must have balance charging capability
   - Must have LiPo mode (not NiCad/NiMH)
   - Quality brands: ISDT, SkyRC, Hitec, Venom

3. **ALWAYS charge in LiPo safe bag or container**
   - Fire-resistant LiPo bag minimum
   - Better: metal ammo can with vent hole
   - Best: concrete floor, away from flammables

4. **ALWAYS verify settings before charging**
   - Correct cell count (2S, 3S, 4S, etc.)
   - Correct capacity
   - Correct charge rate (1C typical, max per manufacturer)
   - Balance charge mode selected

5. **NEVER charge damaged batteries**
   - Inspect before every charge
   - If swollen, punctured, or damaged → dispose

### Recommended Charging Procedure

**Setup:**
1. Clear area of flammable materials
2. Place battery in LiPo safe bag
3. Place on non-flammable surface (concrete, metal, ceramic tile)
4. Have fire extinguisher accessible (5-10 feet away)
5. Ensure good ventilation

**Configuration:**
1. Connect balance lead to charger
2. Connect main lead to charger
3. Verify cell count on charger display matches battery
4. Set charge current: **1C is safe** (1500mAh battery = 1.5A charge rate)
   - Faster charging (2C) increases stress and heat
   - Slower charging (0.5C) is safest
5. Select "LiPo Balance Charge" mode
6. Double-check all settings
7. Start charge

**Monitoring:**
1. Watch first 2-3 minutes for any issues
2. Check every 5-10 minutes
3. Battery should be slightly warm, **NOT hot**
4. Listen for hissing, popping, or unusual sounds
5. Smell for unusual odors

**Completion:**
1. Charger will beep/indicate completion
2. Verify battery is 4.2V per cell (or storage voltage if storage charging)
3. Let battery cool before use (5-10 minutes)
4. Disconnect from charger
5. Label battery with charge date (optional but recommended)

### Charge Rate Guidelines

| Battery Condition | Recommended Charge Rate | Notes |
|-------------------|------------------------|-------|
| **New battery** | 1C | Conservative, safe |
| **Regular use** | 1C | Standard charging |
| **Fast charge (needed quickly)** | 2C | Higher stress, reduces battery life |
| **Long-term storage prep** | 0.5C to storage voltage | Safest for battery |
| **Old battery (50+ cycles)** | 0.5-1C | Lower rate extends life |
| **Any swelling** | **DO NOT CHARGE** | Dispose immediately |

## Storage Safety

### Short-Term Storage (Less than 48 hours)

**For immediate reuse:**
- Keep at full charge (4.2V/cell) is acceptable
- Store in LiPo bag
- Room temperature
- Away from flammables

### Long-Term Storage (More than 3 days)

!!! warning "Storage Voltage is Critical"
    **ALWAYS store LiPos at storage voltage (3.8V-3.85V per cell)** for periods longer than 3 days. Storing at full charge (4.2V) stresses the battery and significantly reduces lifespan. Storing too low risks over-discharge.

**Proper long-term storage:**
1. **Charge/discharge to storage voltage**
   - Use charger's "Storage" mode
   - Brings battery to 3.8V per cell
2. **Place in LiPo safe bag or metal container**
3. **Store in cool, dry location**
   - Ideal: 40-80°F (4-27°C)
   - Avoid: hot cars, attics, direct sunlight
   - Never: freezing temperatures
4. **Keep away from flammables**
   - Not in bedroom, living room
   - Garage or shed (with fire extinguisher) is better
5. **Check every 30-60 days**
   - Voltage should remain stable
   - Any swelling = dispose immediately

### Storage Locations

✅ **GOOD:**
- Garage on concrete floor
- Workshop with fire extinguisher
- Metal cabinet
- Fireproof safe (if not sealed airtight)

⚠️ **ACCEPTABLE (with precautions):**
- Basement (if dry, not near furnace)
- Shed (temperature controlled)

❌ **NEVER:**
- Bedroom or living spaces
- Near flammable liquids (gasoline, paint)
- In hot car or trunk
- Direct sunlight
- Near heat sources (furnace, water heater)
- Airtight containers (pressure buildup risk)

### Storage Containers

**LiPo Safe Bags:**
- **Pros:** Cheap ($10-20), portable, some fire resistance
- **Cons:** Not fully fireproof, won't contain major fire
- **Use:** Charging and short-term storage

**Metal Ammo Cans:**
- **Pros:** Strong, contains fire better, vents available
- **Cons:** Must add vent hole (pressure release)
- **Use:** Long-term storage, charging location
- **Important:** Drill 1/4" hole in lid for venting

**Bat-Safe or Similar:**
- **Pros:** Designed for LiPo fires, excellent containment
- **Cons:** Expensive ($60-150)
- **Use:** Maximum safety for charging/storage

**Ceramic Pots/Concrete Blocks:**
- **Pros:** Non-flammable, cheap
- **Cons:** Not portable, no lid
- **Use:** Charging location

## Transportation Safety

### Vehicle Transport

**Rules:**
1. Batteries at storage voltage if possible
2. In LiPo safe bag minimum
3. Not in direct sunlight
4. Not in hot trunk
5. Secured so won't roll around
6. Never transport damaged batteries

**Flying with LiPos (Aircraft):**
- **Carry-on ONLY** - never checked baggage
- Must be in LiPo bag
- Airlines limit size/quantity
- Check specific airline policies
- International flight rules vary

## Usage Safety

### Before Each Use

- [ ] **Visual inspection** - no swelling, damage, loose wires
- [ ] **Voltage check** - all cells balanced and charged
- [ ] **Temperature check** - room temperature, not cold or hot
- [ ] **Connection check** - connectors secure and clean
- [ ] **Capacity check** - appropriate for your needs

### During Use

- [ ] **Monitor voltage** - land/stop before 3.0V per cell (3.5V safer)
- [ ] **Monitor temperature** - battery shouldn't exceed 140°F (60°C)
- [ ] **Use battery alarm** or telemetry warnings
- [ ] **Land with reserve** - 20% capacity recommended

### After Use

- [ ] **Check temperature** - should cool to room temp in 10-15 min
- [ ] **Check for swelling** - feel for puffiness
- [ ] **Check voltage** - note resting voltage after cooldown
- [ ] **Storage charge** if not using within 2-3 days

## Emergency Response

### Fire Procedure

!!! danger "LiPo Fire - DO NOT USE WATER"
    Water on a lithium fire can cause violent reactions. Use appropriate extinguishers only.

**If battery catches fire:**

1. **Alert everyone** - Shout "FIRE!" loudly
2. **Evacuate people** - Get everyone 20+ feet away
3. **If SMALL and SAFE:**
   - Use ABC or Class D fire extinguisher
   - Smother with sand (dry sandbox helpful)
   - Metal lid to contain
4. **If LARGE or SPREADING:**
   - Evacuate building
   - **Call 911 immediately**
   - Close doors behind you
5. **If outdoors and safe:**
   - Move away and let burn out (takes 5-20 minutes)
   - Keep people/animals away
6. **NEVER:**
   - Use water (can intensify fire)
   - Touch burning battery
   - Breathe fumes (toxic)
   - Try to move large battery fire

**After fire is out:**
- Ventilate area (open windows)
- Battery may reignite - monitor for 1+ hour
- Dispose of remains safely (see disposal section)
- Report significant incidents

### Thermal Runaway Signs

**If battery is entering thermal runaway:**
- Rapid heating
- Hissing/popping sounds
- Smoke
- Bulging/swelling
- Strong chemical smell

**Action:**
1. Disconnect from charger/device immediately (if safe)
2. Move to outdoor area (if safe)
3. Place in metal container or open area
4. Move away (30+ feet)
5. Monitor from safe distance
6. Prepare to call 911

## Disposal

### When to Dispose

- Any swelling/puffing
- Physical damage (puncture, torn wrapper)
- Excessive capacity loss (>20% reduction)
- Cells won't balance
- After 200-300 cycles (depending on use)
- Failed voltage test

### Safe Disposal Procedure

!!! warning "Never Trash a LiPo with Charge"
    A charged LiPo in trash can cause garbage truck or landfill fires. **Discharge completely before disposal.**

**Steps:**

1. **Discharge battery completely**
   - Use discharge function on charger (safest)
   - OR use device until dead
   - OR salt water bath (see below)

2. **Salt water discharge method:**
   - Mix solution: 1/2 cup salt per gallon of water
   - Use plastic bucket
   - Submerge battery completely (attach weight if needed)
   - Keep outdoors, away from flammables
   - Leave for 2-7 days (larger batteries = longer)
   - Check voltage: all cells at 0.0V = safe

3. **Physical preparation:**
   - Cut wires with insulated wire cutters (one at a time)
   - Wrap ends in electrical tape
   - Place in plastic bag

4. **Disposal:**
   - Take to battery recycling center
   - Call2Recycle locations ([call2recycle.org](https://www.call2recycle.org))
   - Some hobby shops accept for recycling
   - Electronics stores (Best Buy, etc.) may accept

**Never:**
- Throw in regular trash (unless fully discharged and checked with recycling program)
- Burn batteries
- Puncture intentionally (fire risk)

## Battery Maintenance

### Extending Battery Life

**Do:**
- ✅ Store at storage voltage
- ✅ Balance charge every time
- ✅ Land with 20% remaining
- ✅ Keep cool during use and storage
- ✅ Charge at 1C or less
- ✅ Use quality charger
- ✅ Inspect before each use
- ✅ Track cycles (write on battery)

**Don't:**
- ❌ Drain below 3.0V per cell
- ❌ Overcharge (above 4.2V per cell)
- ❌ Store at full charge long-term
- ❌ Store in hot environments
- ❌ Fast charge unnecessarily (2C+)
- ❌ Use damaged batteries
- ❌ Over-discharge repeatedly

### Battery Log (Recommended)

Track on battery with permanent marker:
- Purchase date
- Cycle count (tally marks)
- Any incidents (crash, over-discharge)
- Capacity test results

**Example:**
```
Purchased: 11/2025
Cycles: |||| |||| ||| (13)
Notes: OK
```

## Educational Settings

### Additional Safety for Schools

**Required:**
- [ ] Designated charging area (fire-safe)
- [ ] Adult supervision of all charging
- [ ] Fire extinguisher (ABC or Class D) within 10 feet
- [ ] Written procedures posted
- [ ] Student training documented
- [ ] Battery inventory system
- [ ] Regular inspections (monthly minimum)
- [ ] Disposal plan for damaged batteries

**Recommended:**
- Bat-Safe or metal ammo cans for charging
- Smoke detector in charging area
- Emergency contact procedures posted
- Insurance notification (some policies exclude LiPos)
- Parent/guardian LiPo safety acknowledgment for students

## Product Recommendations

### Chargers (Budget to Professional)

**Entry ($30-60):**
- Venom Pro Duo
- HTRC LiPo charger

**Mid-Range ($60-120):**
- ISDT Q6/Q8
- SkyRC B6AC V2

**Professional ($120-300):**
- ISDT P20/P30
- Hitec X4 Advanced
- SkyRC Q200

**Features to look for:**
- Balance charging
- Storage mode
- Multiple chemistries (LiPo, Li-ion, LiHV)
- Safety features (auto-shutoff)
- Temperature monitoring (if available)

### Safety Equipment

**Essential:**
- LiPo safe bag: $10-20 (multiple needed)
- Fire extinguisher (ABC): $20-50
- Voltage checker: $5-15

**Recommended:**
- Metal ammo can: $20-40
- Bat-Safe: $60-150
- Temperature gun: $15-30
- Battery capacity tester: $20-50

## Quick Reference Checklist

### Every Charge
- [ ] Battery inspected (no swelling/damage)
- [ ] LiPo safe bag or container
- [ ] Correct charger settings (cell count, capacity, LiPo mode)
- [ ] Balance leads connected
- [ ] Area clear of flammables
- [ ] Fire extinguisher accessible
- [ ] Will monitor entire charge time

### Every Flight/Use
- [ ] Battery inspected
- [ ] Voltage checked
- [ ] Temperature normal
- [ ] Connections secure

### Every 30 Days (Storage)
- [ ] Voltage checked (should be 3.8V/cell ±0.1V)
- [ ] Visual inspection
- [ ] Any issues = immediate disposal

## Resources

### Official Safety Info
- [FAA Battery Safety](https://www.faa.gov/hazmat/safecargo/lithium_batteries)
- [CPSC LiPo Safety](https://www.cpsc.gov/safety-education/safety-guides/toys/battery-safety)

### Community Resources
- [RC Groups - LiPo Safety Discussions](https://www.rcgroups.com)
- [Oscar Liang - LiPo Guide](https://oscarliang.com/lipo-battery-guide)
- [Painless360 - LiPo Videos](https://www.youtube.com/user/Painless360)

### Recycling
- [Call2Recycle Locator](https://www.call2recycle.org/locator/)

## Summary

**LiPo batteries are safe when handled properly but dangerous when mishandled.**

**Keys to safety:**
1. Never leave charging unattended
2. Always use LiPo safe bag/container
3. Inspect before every use
4. Dispose of damaged batteries immediately
5. Store at storage voltage
6. Have fire safety equipment ready

**When in doubt, ask for help or dispose of the battery.**

---

**Last Updated:** November 2025
**Related Topics:** [Safety Procedures](safety-procedures.md) | [Getting Started](../getting-started/index.md) | [Glossary](../glossary/index.md)
