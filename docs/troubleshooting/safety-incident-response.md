# Safety Incident Response

Procedures for handling crashes, flyaways, and safety incidents. Learn proper response, documentation, analysis, and prevention strategies.

## Immediate Response Procedures

### During Flight Emergency

**Priority Order:**
1. **Protect People** - Safety of people is paramount
2. **Protect Property** - Avoid damage to buildings, vehicles
3. **Recover Vehicle** - Land or crash safely
4. **Document** - Record what happened

### Active Incident Response

**If Vehicle is Out of Control:**

1. **Warn Bystanders**
   - Loud, clear warnings
   - Direct people away from area
   - Shield others if needed

2. **Attempt Control Recovery**
   - Switch to stabilize mode
   - Reduce throttle
   - Attempt emergency landing

3. **Activate Failsafe if Applicable**
   - RTL if GPS available and safe
   - Land mode if appropriate
   - Disarm as last resort if close to ground

4. **Disarm if Impact Imminent**
   - Prevents props spinning on ground
   - Reduces injury/damage potential
   - Only if crash unavoidable

!!! danger "Never Chase a Crashing Vehicle"
    Do not run after or try to catch a failing vehicle. Spinning propellers cause serious injury. Let it crash and approach only after motors stop.

### Post-Crash Immediate Actions

**Within 30 Seconds:**

1. **Disarm/Disconnect Power**
   - Remove battery if safe to approach
   - Prevent fire risk
   - Stop any remaining motor movement

2. **Assess Injuries**
   - Check all people present
   - Administer first aid if needed
   - Call emergency services if required

3. **Secure Area**
   - Mark crash site if needed
   - Prevent others from entering
   - Check for hazards (damaged battery, sharp debris)

4. **Initial Documentation**
   - Take photos from multiple angles
   - Note exact location
   - Record time and conditions
   - Identify witnesses

**Within 5 Minutes:**

1. **Battery Safety**
   - Check for damage, swelling, heat
   - Move damaged battery to safe location
   - Place in LiPo safety bag if available
   - Never leave damaged LiPo unattended

2. **Secure Evidence**
   - Do not disassemble yet
   - Protect from weather
   - Keep all pieces together
   - Note positions of components

3. **Preliminary Assessment**
   - Obvious damage?
   - What failed?
   - Any witnesses?
   - Environmental factors?

## Incident Categories

### Minor Incident
**Definition:**
- No injuries
- Minor vehicle damage
- No property damage
- Contained to intended operating area

**Response:**
- Document briefly
- Repair and test
- Resume operations

### Moderate Incident
**Definition:**
- No injuries
- Significant vehicle damage
- Minor property damage
- Or vehicle left designated area

**Response:**
- Full documentation
- Root cause analysis
- Review procedures
- Implement improvements

### Major Incident
**Definition:**
- Injuries occurred
- Substantial property damage
- Loss of vehicle
- Serious safety violation

**Response:**
- Complete investigation
- Report to authorities if required
- Review and revise safety procedures
- Additional training before resuming

### Regulatory Reportable Incident
**Definition (varies by location):**
- Serious injury
- Property damage over threshold ($500 in US)
- Loss of control over populated area
- As defined by local regulations

**Response:**
- Immediate report to authorities
- Preserve all evidence
- Formal investigation
- Legal consultation if needed

## Crash Analysis

### Physical Inspection

**Systematic Inspection Process:**

1. **Photography**
   - Overall vehicle state
   - Each damaged component
   - Unusual findings
   - Include scale reference

2. **Component-by-Component Check**
   ```
   Frame: Cracks, breaks, deformities
   Motors: Damage, binding, bell condition
   Props: Breaks, which props damaged
   ESCs: Burn marks, damaged components
   Flight Controller: Physical damage, loose components
   Battery: Swelling, puncture, damage
   Wiring: Breaks, shorts, disconnections
   ```

3. **Document Damage Pattern**
   - First impact point
   - Force direction
   - Secondary damage
   - What failed vs what was damaged in crash

### Log Analysis

**Critical Information in Logs:**

1. **Timeline of Events**
   - What happened in last 30 seconds?
   - Mode changes?
   - Control inputs?
   - System warnings?

2. **Sensor Data**
   - GPS: Position, satellites, HDOP
   - IMU: Gyro, accelerometer data
   - Battery: Voltage trend, current
   - Compass: Heading, variance

3. **Control Outputs**
   - Motor commands
   - Were motors responding?
   - Did one motor fail?
   - Extreme compensation visible?

4. **Error Messages**
   - Pre-arm failures?
   - EKF variances?
   - Sensor failures?
   - Warnings ignored?

[→ Detailed Log Analysis Guide](log-analysis.md)

### Root Cause Determination

**The "Five Whys" Method:**

Example:
1. **Why did it crash?** - Lost control
2. **Why lost control?** - One motor stopped
3. **Why did motor stop?** - ESC failed
4. **Why did ESC fail?** - Overheated
5. **Why overheated?** - Insufficient cooling for aggressive flying

Root Cause: Design/configuration didn't account for use case

**Common Root Causes:**

| Category | Examples |
|----------|----------|
| Pilot Error | Wrong mode, loss of orientation, insufficient skill |
| Configuration | Wrong settings, improper calibration, untuned PIDs |
| Mechanical | Loose screws, broken frame, prop failure |
| Electrical | Bad solder, wiring short, component failure |
| Software | Bug, incompatible firmware, corrupted settings |
| Environmental | Wind, interference, obstacle |
| Maintenance | Worn components, degraded battery, missed inspection |

## Incident Documentation

### Required Information

**Basic Information:**
```
Date/Time:
Location: (GPS coordinates if available)
Pilot:
Observer:
Vehicle: (make, model, serial number)
Weather: (wind, temperature, visibility)
```

**Incident Details:**
```
Flight Purpose:
Flight Mode:
Duration Before Incident:
Description of Events:
Pilot Actions Taken:
Outcome:
```

**Damage Assessment:**
```
Personnel: (injuries if any)
Vehicle: (component-by-component)
Property: (if any)
Estimated Cost:
```

**Evidence:**
```
Photos: (attached)
Video: (if available)
Flight Logs: (file names/locations)
Witness Statements:
```

### Documentation Template

````markdown
# Incident Report

## Incident Information
- **Date:** YYYY-MM-DD
- **Time:** HH:MM (local)
- **Location:** Address or GPS coordinates
- **Incident ID:** Unique identifier

## Personnel
- **Pilot:** Name
- **Observer:** Name
- **Witnesses:** Names and contact info

## Vehicle Information
- **Type:** Quadcopter/Fixed-wing/Rover
- **Model:**
- **Serial Number:**
- **Weight:**
- **Flight Controller:** Type and firmware version
- **Battery:** Configuration and charge state

## Environmental Conditions
- **Weather:** Clear/Cloudy/Rain
- **Wind:** Speed and direction
- **Temperature:**
- **Visibility:**

## Flight Information
- **Purpose:** Training/Photography/Testing/etc.
- **Flight Number:** (of day/session)
- **Duration Before Incident:** Minutes
- **Flight Mode:** Stabilize/GPS/Auto/etc.
- **Altitude:** Estimated height AGL

## Incident Description
### What Happened (Chronological)
1. [First event]
2. [Second event]
3. [Incident]
4. [Response]

### Pilot Actions
- [What pilot attempted]
- [Control inputs used]
- [Mode changes]

### Observer Notes
- [What observer witnessed]
- [Warnings given]

## Damage Assessment
### Personnel
- [ ] No injuries
- [ ] Minor injuries (describe):
- [ ] Serious injuries (describe):

### Vehicle
| Component | Status | Notes |
|-----------|--------|-------|
| Frame | OK / Damaged / Destroyed | |
| Motors | OK / Damaged / Destroyed | |
| Props | OK / Damaged / Destroyed | |
| ESCs | OK / Damaged / Destroyed | |
| FC | OK / Damaged / Destroyed | |
| Battery | OK / Damaged / Destroyed | |

### Property
- [ ] No property damage
- [ ] Property damaged (describe):

## Analysis
### Root Cause (Preliminary)
[Initial determination of what caused incident]

### Contributing Factors
1. [Factor 1]
2. [Factor 2]

### Evidence
- [ ] Photos attached
- [ ] Video available: [location]
- [ ] Flight logs saved: [file names]
- [ ] Witness statements: [attached]

## Corrective Actions
### Immediate
- [ ] [Action 1]
- [ ] [Action 2]

### Long-term
- [ ] [Action 1]
- [ ] [Action 2]

## Lessons Learned
[What can be learned from this incident]

## Report Completed By
- **Name:**
- **Date:**
- **Signature:**
````

## Educational Response

### Classroom Incident Handling

**Immediate:**
1. Ensure all students safe
2. Calm and professional demeanor
3. Follow incident procedures
4. Document thoroughly

**Educational Opportunity:**
- Not a punishment situation
- Learning experience for all
- Open discussion of what happened
- Implement improvements

**Student Support:**
- Reassure student involved
- Focus on learning, not blame
- Build confidence through analysis
- Path forward to resume activities

### Parental Communication

**If Student Involved in Incident:**

**Immediate Notification if:**
- Any injury
- Property damage
- Significant vehicle damage
- Incident noteworthy

**Communication Should Include:**
- What happened
- Actions taken
- Student's status
- Path forward
- Safety improvements

**Template Email:**
```
Subject: Incident Report - [Student Name] - [Date]

Dear [Parent/Guardian],

I'm writing to inform you of an incident involving [Student Name]
during our unmanned systems class today.

What Happened:
[Brief, factual description]

Response:
[What was done immediately]

Status:
[Student is fine/minor damage/etc.]

Analysis:
[Brief root cause]

Moving Forward:
[Safety improvements, additional training, etc.]

We treat every incident as a learning opportunity and have
documented everything for review and improvement.

Please contact me with any questions or concerns.

Best regards,
[Teacher Name]
```

## Prevention Strategies

### Pre-Flight Prevention

**Checklist Compliance:**
- Mandatory for every flight
- Witnessed/signed
- No shortcuts
- Document completion

**Risk Assessment:**
```
For Each Flight, Evaluate:
- Pilot skill vs difficulty
- Environmental conditions
- Vehicle condition
- Airspace status
- Emergency options
```

**Go/No-Go Decision:**
- Clear criteria
- Authority to cancel
- No pressure to fly
- Alternatives available

### Training-Based Prevention

**Progressive Skill Building:**
1. Simulator practice
2. Hover training (props off)
3. Controlled indoor flight
4. Basic outdoor patterns
5. Advanced maneuvers
6. Autonomous operations

**Scenario Training:**
- Loss of orientation
- Control failure
- Low battery
- Flyaway recovery
- Emergency landing

**Regular Skill Assessment:**
- Periodic check rides
- Proficiency demonstration
- Refresher training
- Maintain currency

### Maintenance-Based Prevention

**Regular Inspections:**
- Pre-flight (every flight)
- Post-flight (after each session)
- Detailed (weekly for active vehicles)
- Overhaul (seasonal or after crashes)

**Component Life Tracking:**
```
Track:
- Flight hours
- Number of flights
- Crash history
- Age of components

Replace:
- Props: 20-50 flights or damage
- Motors: 200+ hours or wear
- Battery: Cycle count or performance
- Frame: Any cracks or deformation
```

**Maintenance Records:**
- Log all maintenance
- Component serial numbers
- Installation dates
- Next service due

[→ Preventive Maintenance Guide](preventive-maintenance.md)

## Regulatory Considerations

### FAA Requirements (USA)

**Part 107:**
- Report accidents to FAA within 10 days if serious injury or property damage >$500
- Maintain records
- Make available to FAA on request

**Recreational:**
- Report if injury or substantial property damage
- Local law enforcement may need notification

**Educational Operations:**
- May fall under Part 107 or exception
- Check specific requirements
- Maintain compliance

### School/Organization Policies

**Internal Reporting:**
- Administration notification
- Insurance company (if applicable)
- Board of education (if major)
- Document per policy

**Liability Protection:**
- Follow all procedures
- Document thoroughly
- Proper training records
- Insurance current

## Return to Operations

### After Minor Incident

**Requirements:**
1. Repairs completed
2. Bench testing passed
3. Hover test successful
4. Pilot demonstrates proficiency

**Process:**
- Systematic validation
- Supervised initially
- Gradual return to normal ops

### After Major Incident

**Additional Requirements:**
1. Complete investigation finished
2. Root cause addressed
3. Procedures updated
4. Retraining completed
5. Administrative approval
6. Insurance notified (if required)

**Lessons Learned Integration:**
- Share findings (maintaining privacy)
- Update training materials
- Revise procedures
- Implement improvements

## Psychological Aspects

### Pilot Confidence

**After Crash:**
- Normal to be shaken
- Build confidence gradually
- Supervised flights initially
- Focus on what was learned

**Fear Management:**
- Acknowledge feelings
- Systematic return
- Positive reinforcement
- Professional support if needed

### Learning Environment

**Maintain Safety Culture:**
- Incidents expected in learning
- Open discussion encouraged
- No punishment for honest mistakes
- Focus on improvement

**Reporting Encouraged:**
- No fear of reprisal
- Near-misses are learning opportunities
- Early reporting prevents accidents
- Recognize good reporting

## Next Steps

- [Preventive Maintenance](preventive-maintenance.md) - Avoid incidents
- [Log Analysis](log-analysis.md) - Understand what happened
- [Safety Procedures](../safety-compliance/safety-procedures.md) - Prevention
- [Hardware Issues](hardware-issues.md) - Repair damaged components

## Resources

- FAA Accident Reporting: [www.faa.gov](https://www.faa.gov/uas)
- NTSB Aviation Accident Database
- Safety Reporting Systems
- Insurance Provider Guidelines
- Legal Resources for Educational Programs
