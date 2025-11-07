---
title: Safety Procedures
description: Essential operational safety procedures for all unmanned vehicle platforms
---

# Safety Procedures

!!! info "Universal Application"
    These safety procedures apply to **all** unmanned vehicle platforms: aerial (UAVs), ground (UGVs), and marine (USVs). Platform-specific additions are noted where applicable.

## Safety Culture

**Safety is everyone's responsibility.** Whether you're operating alone or in a group, maintaining a safety-first mindset prevents accidents and builds professional habits.

### Core Principles

1. **Preparation over reaction** - Plan for emergencies before they happen
2. **No shortcuts** - Every checklist item matters
3. **Speak up** - Report unsafe practices without hesitation
4. **Continuous learning** - Learn from every incident and near-miss
5. **Respect limits** - Know your skill level and equipment capabilities

## Personal Protective Equipment (PPE)

### Required for All Operations

| PPE Item | Purpose | When Required |
|----------|---------|---------------|
| **Safety glasses** | Eye protection from debris, propellers | Building, testing, operating near platform |
| **Closed-toe shoes** | Foot protection | All field operations |
| **Long pants** | Leg protection | Field operations with large platforms |

### Recommended

| PPE Item | Purpose | When Useful |
|----------|---------|-------------|
| **Gloves** | Hand protection | Handling hot motors, sharp edges |
| **Ear protection** | Hearing protection | Large drones, gas engines |
| **High-vis vest** | Visibility | Outdoor operations, near roads |
| **Sun protection** | UV protection | Extended outdoor operations |
| **First aid kit** | Emergency response | All field operations |

### Building/Workshop PPE

| PPE Item | Purpose | When Required |
|----------|---------|---------------|
| **Safety glasses** | Solder splatter, component projection | Soldering, cutting |
| **Heat-resistant mat** | Protect work surface | Soldering |
| **Ventilation** | Fume extraction | Soldering |
| **Gloves (optional)** | Burn protection | Handling hot components |

## Pre-Operation Checklist

### Universal Pre-Flight/Pre-Drive Check

Complete **every time before** operation:

#### Platform Inspection
- [ ] **Frame/structure** - No cracks, damage, or loose parts
- [ ] **Propellers/wheels** - Secure, undamaged, spin freely
- [ ] **Motors** - Secure mounting, clean, no debris
- [ ] **Wiring** - No frayed wires, secure connections
- [ ] **Battery** - No swelling, proper voltage, secure mounting
- [ ] **Electronics** - Secure mounting, no visible damage
- [ ] **Payload** - Secure, within weight limits

#### Battery Check
- [ ] **Voltage** - Fully charged (4.2V/cell for LiPo) or appropriate for mission
- [ ] **Balance** - All cells within 0.03V of each other
- [ ] **Temperature** - Room temperature (not cold or hot)
- [ ] **Physical** - No swelling, punctures, or damage
- [ ] **Connections** - Secure, no damage to connectors
- [ ] **Charge date** - Recharged if more than 1 week old

#### Control System Check
- [ ] **Radio link** - Transmitter and receiver communicating
- [ ] **Range test** - Performed if required
- [ ] **Control surface/motor check** - All respond correctly
- [ ] **Failsafe test** - Verified (turn off transmitter, verify failsafe activates)
- [ ] **GPS lock** - Minimum 6 satellites (if GPS-equipped)
- [ ] **Compass calibration** - Recent (within 30 days) and accurate
- [ ] **Sensors** - All showing valid readings

#### Environment Assessment
- [ ] **Weather** - Acceptable for platform capabilities
- [ ] **Airspace** - Legal to operate (aerial platforms)
- [ ] **Operating area** - Clear of obstacles, people, animals
- [ ] **Lighting** - Sufficient visibility
- [ ] **Emergency plan** - Reviewed and communicated

#### Documentation & Communication
- [ ] **Flight/operation plan** - Defined and understood
- [ ] **Spotter** - Assigned (if required)
- [ ] **Emergency contacts** - Phone accessible
- [ ] **Regulatory compliance** - TRUST/Part 107, registration verified
- [ ] **Permissions** - Property owner approval obtained

### Platform-Specific Additions

#### Aerial (UAV) Specific
- [ ] **Propeller tightness** - Hand-tighten, verify secure
- [ ] **Center of gravity** - Balanced correctly
- [ ] **Takeoff area** - Level, clear, appropriate size
- [ ] **Wind conditions** - Within platform limits
- [ ] **Return-to-home** - Set and tested

#### Ground (UGV) Specific
- [ ] **Tire/track condition** - Proper inflation, no damage
- [ ] **Steering** - Full range of motion, no binding
- [ ] **Terrain assessment** - Appropriate for platform
- [ ] **Boundary** - Geofence set (if autonomous)

#### Marine (USV) Specific
- [ ] **Waterproofing** - All seals intact, hatches closed
- [ ] **Flotation** - Buoyancy verified
- [ ] **Retrieval plan** - Method to recover if drifts
- [ ] **Water conditions** - Current, waves acceptable
- [ ] **Tether** - Attached for testing (recommended)

## Operating Procedures

### Startup Procedure

1. **Clear area** - Ensure all people/animals at safe distance
2. **Announce startup** - "Powering on, stay clear"
3. **Connect battery** - Main power connection
4. **Wait for initialization** - Allow flight controller/computer to boot
5. **Verify systems** - Check telemetry, GPS, sensors
6. **Arm system** - Follow platform-specific arming procedure
7. **Final check** - Quick visual scan
8. **Announce operation** - "Taking off" / "Starting drive"

### During Operation

#### Operator Responsibilities
- **Maintain visual line of sight** (VLOS) at all times
- **Monitor telemetry** - Voltage, GPS, signal strength
- **Scan for hazards** - People, animals, aircraft (aerial), obstacles
- **Communicate** - With spotter and others in area
- **Respect limits** - Stay within planned operation area and capabilities

#### Spotter Responsibilities (if present)
- **Maintain visual contact** with platform
- **Scan for hazards** in all directions
- **Communicate hazards** to operator immediately
- **Do not distract operator** unnecessarily
- **Ready to take action** in emergency

#### Battery Management During Flight/Operation
- **Monitor voltage constantly** via telemetry or visual alarm
- **Plan return** - Start when battery reaches 30-40% (not less than 20%)
- **Land immediately** if voltage alarm sounds
- **Never** push battery to cutoff voltage

### Shutdown Procedure

1. **Return to home** - Safe landing/stopping area
2. **Land/stop** - Controlled, gentle
3. **Disarm** - Immediately after touchdown/stop
4. **Disconnect battery** - Wait 30 seconds, then disconnect
5. **Announce safe** - "Platform disarmed and safe"
6. **Check battery temperature** - Should be warm, not hot
7. **Post-operation inspection** - Check for new damage

## Emergency Procedures

### Loss of Control

**Aerial:**
1. **Attempt failsafe** - Trigger return-to-home if available
2. **Cut throttle** - If over safe area and low altitude
3. **Alert area** - Warn people in potential flight path
4. **Track platform** - Note where it goes
5. **Retrieve safely** - Disconnect battery first

**Ground/Marine:**
1. **Emergency stop** - Hit kill switch or disarm
2. **Alert others** - Warn of uncontrolled vehicle
3. **Pursue safely** - Don't endanger yourself
4. **Cut power remotely** - If failsafe available

### Platform Crash/Collision

1. **Disarm immediately** - Prevent further damage/injury
2. **Assess injuries** - Check if anyone hurt
3. **Call for help** - 911 if injuries serious
4. **Secure area** - Keep people away from damaged platform
5. **Disconnect battery** - After safe to approach
6. **Document** - Photos, notes for investigation
7. **Report** - To appropriate authorities if required

### Flyaway (Aerial)

1. **Attempt radio contact** - Try control inputs
2. **Attempt return-to-home** - Switch modes
3. **Alert others** - Warn of incoming drone if heading toward people
4. **Note direction** - Track heading and speed
5. **Use app/telemetry** - If available, track GPS location
6. **Cut power** - Last resort if over safe area
7. **Search and retrieve** - When safe
8. **Report to FAA** - If required (manned aircraft risk, etc.)

### Battery Fire

**See [Battery Safety - Emergency Response](battery-safety.md#emergency-response) for detailed procedures.**

**Quick reference:**
1. Alert everyone, evacuate
2. Use ABC or Class D extinguisher (NOT water)
3. Call 911 if large fire
4. Contain if safe (metal container, sand)
5. Let burn out in safe outdoor area if possible

### Injury

1. **Stop all operations immediately**
2. **Assess severity** - Breathing, bleeding, consciousness
3. **Call 911** - For serious injuries
4. **Render first aid** - If trained
5. **Do not move** - Unless immediate danger
6. **Keep calm** - Reassure injured person
7. **Document** - For incident report
8. **Contact emergency contacts** - Parents, administrators, etc.

## Operating Limits

### Weather Limits

#### Aerial Operations

| Condition | Maximum | Notes |
|-----------|---------|-------|
| **Wind** | 15 mph for beginners, 25 mph max | Platform-dependent |
| **Rain** | None (unless waterproof) | Electronics risk |
| **Temperature** | 32°F - 100°F | Battery performance affected outside range |
| **Visibility** | 3 statute miles minimum | FAA requirement |
| **Clouds** | 500' below, 2000' horizontal | FAA requirement in controlled airspace |

**Never fly in:**
- Thunderstorms or lightning within 10 miles
- Fog or low visibility
- High winds or gusts
- Freezing rain or snow

#### Ground Operations

Generally more weather-tolerant, but consider:
- Heavy rain (electronics risk unless waterproof)
- Ice/snow (traction loss)
- Extreme heat (battery/electronics stress)
- Lightning (outdoor operations)

#### Marine Operations

- Waves: Dependent on platform size
- Current: Within motor capability
- Wind: Affects surface vessels
- Water temperature: Cold affects batteries

### Physical Limits

**Aerial:**
- **Altitude:** 400 feet AGL maximum (USA recreational/Part 107)
- **Distance:** Visual line of sight (typically 1/4 mile max for visibility)
- **Speed:** Within pilot skill and platform capabilities

**Ground:**
- **Speed:** Based on environment and reaction time
- **Terrain:** Within platform capabilities (slope, obstacles)
- **Obstacles:** Maintain clearance for safe navigation

**Marine:**
- **Distance from shore:** Retrieval capability
- **Depth:** Sufficient for propellers/hull
- **Traffic:** Avoid boat traffic areas unless authorized

## Safe Operating Distances

### Aerial Platforms

**Minimum distances from:**
- **People (non-participants):** 25 feet minimum (recreational), varies by Part 107 category
- **Moving vehicles:** 50 feet
- **Structures:** 25 feet (unless inspecting)
- **Animals:** 50 feet (wildlife), 100 feet (livestock)
- **Other aircraft:** Give way, maintain separation

### Ground Platforms

**Minimum distances from:**
- **People (non-participants):** 10 feet
- **Obstacles:** 3 feet
- **Hazards (cliffs, water):** 10 feet
- **Animals:** 25 feet

### Marine Platforms

**Minimum distances from:**
- **Swimmers:** 100 feet
- **Other boats:** 50 feet (or per local waterway rules)
- **Docks/structures:** 10 feet
- **Wildlife:** 100 feet

## Risk Mitigation

### Before High-Risk Operations

Consider "high-risk" as:
- New platform or operator
- Challenging environment (wind, terrain, water conditions)
- Near people or property
- Testing new features/code
- Extended duration
- Night operations

**Additional precautions:**
- Extra spotter(s)
- Higher battery reserves (return at 50%)
- Reduced operating area
- Enhanced communication plan
- Standby equipment
- Professional photographer/videographer insurance (if applicable)

### Progressive Skill Development

**Don't attempt until proficient at previous level:**

**Level 1:** Hover/straight-line driving (controlled environment)
**Level 2:** Basic maneuvers (circles, figure-8, speed control)
**Level 3:** Moderate environments (light wind, uneven terrain)
**Level 4:** Advanced maneuvers (orbits, complex paths)
**Level 5:** Challenging environments (strong wind, rough terrain/water)
**Level 6:** Autonomous missions (waypoints, return-to-home)

## Record Keeping

### Flight/Operation Log

Maintain log with:
- Date and time
- Location
- Platform type/ID
- Battery ID and starting voltage
- Flight/operation duration
- Conditions (weather, environment)
- Operator name
- Any incidents or issues
- Maintenance performed

**Why logging matters:**
- Track battery cycles
- Identify patterns in issues
- Regulatory compliance (Part 107)
- Insurance claims
- Learning and improvement

### Incident Reports

Document any:
- Crashes or hard landings
- Loss of control
- Near-misses with people/aircraft
- Equipment failures
- Injuries
- Property damage

**Report should include:**
- What happened (facts, no speculation)
- When and where
- Who was involved
- Weather and conditions
- Platform status before incident
- Immediate actions taken
- Root cause analysis (after investigation)
- Corrective actions to prevent recurrence

## Training and Competency

### Before Solo Operation

Operators should demonstrate:
- [ ] Knowledge of safety procedures
- [ ] Completion of regulatory requirements (TRUST/Part 107)
- [ ] Understanding of platform operation
- [ ] Battery safety knowledge
- [ ] Emergency procedure knowledge
- [ ] Successful simulator training (if applicable)
- [ ] Supervised flight hours (10+ recommended)
- [ ] Emergency scenario responses

### Maintaining Competency

- **Regular practice** - Fly/drive at least monthly
- **Recurrent training** - Annual safety review
- **Simulator practice** - Maintain skills during off-season
- **Stay current** - Read about incidents and lessons learned
- **Update knowledge** - Regulations and best practices change

## Site Safety

### Field Setup

1. **Define operating area** - Use cones, flags, or markers
2. **Establish safety perimeter** - Keep spectators outside
3. **Position safety equipment** - Fire extinguisher, first aid accessible
4. **Designate roles** - Pilot, spotter, safety officer
5. **Communicate boundaries** - Ensure all participants understand

### Spectator Management

- Designated viewing area (25+ feet from operations)
- Briefing on safety (no sudden movements, stay in area)
- Children supervised by adults
- No distractions to operator during critical phases

### Multi-Operator Safety

If multiple platforms operating:
- **Designated flight/drive areas** - Separate if possible
- **Communication protocol** - Announce takeoffs, landings
- **One active at a time** - For beginners
- **Spotter coordination** - Clear role assignments
- **Emergency freeze** - All land/stop on command if hazard appears

## Maintenance Safety

### Regular Maintenance

- [ ] **Inspection after every 5 flights/operations** - Detailed check
- [ ] **Monthly inspections** - Even if not using (storage check)
- [ ] **Pre-season inspection** - After storage period
- [ ] **Post-incident inspection** - After any crash or hard landing

### Safe Maintenance Practices

- **Disconnect battery** before maintenance
- **Use proper tools** - Don't improvise
- **Work in good lighting** - See what you're doing
- **Organize parts** - Use trays, bags for small parts
- **Follow manufacturer instructions** - No shortcuts
- **Test after repairs** - Ground test before flight
- **Document maintenance** - Log all work performed

## Summary: The Safety Mindset

**Key behaviors of safe operators:**

1. **Checklist discipline** - Every time, no exceptions
2. **Conservative decision-making** - When in doubt, don't
3. **Situational awareness** - Constant scanning for hazards
4. **Respect for limitations** - Know and honor your limits
5. **Preparation** - Plan for emergencies before they happen
6. **Continuous learning** - Always improving knowledge and skills
7. **Communication** - Clear, frequent, respectful
8. **Responsibility** - Own your actions and their consequences

!!! quote "Safety Rule #1"
    **No flight/operation is so important that it's worth compromising safety.**

    You can always try again tomorrow under better conditions. You can't undo an injury or serious incident.

## Resources

### Safety Organizations
- [Academy of Model Aeronautics (AMA)](https://www.modelaircraft.org/safety)
- [Know Before You Fly](https://www.knowbeforeyoufly.org)
- [FAA Safety](https://www.faa.gov/uas/resources/safety_awareness)

### Training
- [FAA TRUST](https://www.faa.gov/uas/recreational_fliers/knowledge_test)
- [FAA Part 107](https://www.faa.gov/uas/commercial_operators)

### Incident Learning
- [NTSB Incident Database](https://www.ntsb.gov)
- RC forums incident discussion threads

## Next Steps

1. ✅ Read [Battery Safety](battery-safety.md) thoroughly
2. ✅ Complete [FAA requirements](faa-regulations.md) if flying aerial platforms
3. ✅ If educator, review [School Policies](school-policies.md)
4. ✅ Create your personal checklists based on your platform
5. ✅ Practice emergency procedures
6. ✅ Start building in [Getting Started](../getting-started/index.md)

---

**Last Updated:** November 2025
**Related Topics:** [Battery Safety](battery-safety.md) | [FAA Regulations](faa-regulations.md) | [Getting Started](../getting-started/index.md)
