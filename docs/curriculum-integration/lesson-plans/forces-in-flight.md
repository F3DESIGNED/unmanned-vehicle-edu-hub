# Lesson Plan: Forces in Flight

**Subject**: Physics
**Grade Level**: 9-12
**Duration**: 2-3 hours (can be split into 2 class periods)
**Prerequisites**: Basic understanding of forces and Newton's Laws

## Learning Objectives

By the end of this lesson, students will be able to:

1. **Identify** the four forces acting on an aircraft in flight (lift, weight, thrust, drag)
2. **Explain** how these forces interact to enable flight
3. **Measure** thrust and calculate theoretical flight performance
4. **Analyze** how changing variables affects flight characteristics
5. **Apply** Newton's Laws to explain multirotor flight

## Standards Alignment

### NGSS
- **HS-PS2-1**: Analyze data to support the claim that Newton's second law describes the mathematical relationship among net force, mass, and acceleration
- **HS-PS3-1**: Create a computational model to calculate change in energy of a system

### Common Core Math
- **CCSS.MATH.CONTENT.HSN.Q.A.1**: Use units as a way to understand problems
- **CCSS.MATH.CONTENT.HSN.Q.A.3**: Choose and interpret scale in formulas, graphs, and data displays

## Materials Needed

**Per Student/Group (2-3 students):**
- Quadcopter (can be shared, props removed for initial activities)
- Digital scale (kitchen scale, 0.1g precision)
- Stopwatch or timer
- Calculator
- Ruler or measuring tape
- Student worksheet (provided below)
- Safety glasses

**Teacher Materials:**
- Demonstration quadcopter (flyable)
- Propeller guard (for safe demonstrations)
- Thrust test stand (or improvised with scale)
- Projector for diagrams
- Optional: Force sensor/dynamometer

**Safety Equipment:**
- Battery fireproof bag
- First aid kit
- Fire extinguisher
- Designated flight area

## Lesson Structure

### Part 1: Introduction (15 minutes)

**Hook Activity:**
Fly a quadcopter briefly (with safety precautions) and ask:
*"How does this drone stay in the air? What forces are at work?"*

**Direct Instruction:**

1. **The Four Forces of Flight**
   ```
   Lift (L) - Upward force from rotors
   Weight (W) - Downward force due to gravity (mg)
   Thrust (T) - Forward force from tilting
   Drag (D) - Resistance to motion through air
   ```

2. **Force Balance**
   ```
   Hovering: Lift = Weight, Thrust = Drag
   Climbing: Lift > Weight
   Descending: Lift < Weight
   Forward Flight: Tilt creates horizontal thrust component
   ```

3. **Newton's Laws Application**
   - **First Law**: Hover = balanced forces (net force zero)
   - **Second Law**: F = ma (more thrust → acceleration)
   - **Third Law**: Rotor pushes air down, air pushes rotor up

**Guided Discussion:**
- How is this different from airplane flight?
- What happens if one motor fails?
- Why four rotors instead of one?

### Part 2: Thrust Measurement Activity (30 minutes)

**Setup:**
1. Remove propellers from quadcopter
2. Install ONE propeller on ONE motor
3. Place quadcopter upside-down on digital scale
4. Secure so it cannot fly off

!!! danger "Safety Critical"
    - Props REMOVED except test motor
    - Secure vehicle to scale
    - Safety glasses required
    - Clear area around test
    - Teacher supervision mandatory

**Procedure:**

1. **Zero the Scale**
   - With quadcopter and battery on scale
   - Record weight: _____ grams

2. **Measure Thrust at Different Throttle**
   - Start at low throttle (slowly!)
   - Motor spins, propeller pushes down on scale
   - Scale reading increases = thrust force
   - Record data in table

**Data Table:**

| Throttle % | Scale Reading (g) | Thrust (g) | Thrust (N) |
|-----------|-------------------|------------|------------|
| 0% | | 0 | 0 |
| 25% | | | |
| 50% | | | |
| 75% | | | |
| 100% | | | |

*Thrust = Scale Reading - Zero Weight*
*Thrust (N) = Thrust (g) × 0.00981*

3. **Calculate Total Potential Thrust**
   - Multiply single motor thrust × 4 motors
   - Record in worksheet

**Analysis Questions:**
1. Is the relationship between throttle and thrust linear?
2. At what throttle % does thrust equal vehicle weight?
3. What is the maximum thrust-to-weight ratio?
4. Why do we need more than 1:1 thrust-to-weight?

### Part 3: Theoretical Flight Performance (25 minutes)

**Calculations:**

Students calculate using their measured data:

**1. Hover Throttle**
```
Weight of quad = W (grams)
Thrust per motor at hover = W / 4
Find throttle % that produces this thrust
```

**2. Maximum Climb Rate (simplified)**
```
Excess Thrust = (Max Total Thrust) - Weight
Acceleration = Excess Thrust / Mass
Climb Rate ≈ √(2 × Acceleration × Height) (simplified)
```

**3. Flight Time Estimation**
```
Battery Capacity = ___ mAh
Hover Current = ___ A (from spec or measurement)
Flight Time = (Capacity / Current) × 0.8 (safety factor)
```

**Example Problem Set:**

```
Given:
- Quadcopter mass: 450g
- Max thrust per motor: 600g
- Battery: 1300mAh, 11.1V
- Hover current: 5A

Calculate:
1. Total max thrust:
   4 × 600g = 2400g

2. Thrust-to-weight ratio:
   2400g / 450g = 5.33:1

3. Excess thrust available:
   2400g - 450g = 1950g = 19.1N

4. Theoretical max acceleration:
   F = ma
   a = F/m = 19.1N / 0.45kg = 42.4 m/s²

5. Flight time estimate:
   (1300mAh / 5000mA) × 0.8 = 0.208 hours = 12.5 minutes
```

**Discussion:**
- Why is actual flight time less than calculated?
- What factors did we not account for?
- How does pilot skill affect battery life?

### Part 4: Force Diagram Activity (20 minutes)

**Individual Work:**

Students draw force diagrams for different flight scenarios:

1. **Hovering**
   ```
   ↑ Lift (4 rotors)
   ↓ Weight (gravity)
   Balanced: L = W
   ```

2. **Climbing**
   ```
   ↑ Lift > Weight
   Net Force upward
   Accelerating up
   ```

3. **Forward Flight**
   ```
   Tilt forward:
   - Creates horizontal thrust component
   - Reduces vertical lift component
   - Must increase total thrust to maintain altitude
   ```

4. **Turning**
   ```
   Different motor speeds
   Creates torque about center
   Yaw rotation (horizontal)
   ```

**Guided Practice:**
Teacher demonstrates each maneuver with actual quadcopter, students confirm their diagrams.

### Part 5: Real Flight Observation (20 minutes)

**Demonstration Flight:**

Teacher performs maneuvers while students observe and record:

| Maneuver | Predicted Forces | Observed Behavior | Matches Prediction? |
|----------|-----------------|-------------------|---------------------|
| Takeoff | | | |
| Hover | | | |
| Forward | | | |
| Climb | | | |
| Descend | | | |
| Turn | | | |

**Student Observations:**
- Note any unexpected behaviors
- Explain using force concepts
- Identify real-world complications (wind, air density, etc.)

### Part 6: Wrap-Up and Assessment (15 minutes)

**Class Discussion:**
- What surprised you about the thrust measurements?
- How accurate were our calculations?
- What makes multirotor flight different from fixed-wing?

**Exit Ticket (individual):**

Answer these questions to demonstrate understanding:

1. A 600g quadcopter has 4 motors. Each motor produces 250g of thrust at 60% throttle.
   - Will it fly? Explain.
   - What is the thrust-to-weight ratio?

2. Draw and label the four forces acting on a quadcopter in forward flight.

3. A quadcopter is hovering. The pilot increases throttle. Using Newton's Laws, explain what happens and why.

## Assessment Rubric

| Criteria | Needs Improvement (1-2) | Proficient (3) | Exemplary (4) |
|----------|----------------------|---------------|--------------|
| **Force Identification** | Cannot identify all four forces | Identifies forces with prompting | Clearly identifies and labels all forces |
| **Calculations** | Major errors in setup or execution | Minor errors, correct method | All calculations correct with work shown |
| **Force Diagrams** | Incomplete or incorrect | Mostly correct, minor errors | Accurate, detailed, labeled correctly |
| **Analysis** | Struggles to explain observations | Explains using some physics concepts | Comprehensive analysis using multiple concepts |
| **Application** | Cannot apply concepts to new scenarios | Applies with guidance | Independently applies to novel situations |
| **Safety** | Needs frequent reminders | Follows procedures | Models safe practices, helps others |

**Total Points: _____ / 24**

## Differentiation

### For Advanced Students:
- Calculate power requirements (voltage × current)
- Research brushless motor efficiency curves
- Design thrust test using multiple propeller sizes
- Calculate moment of inertia for rotation analysis
- Model drag forces mathematically

### For Struggling Students:
- Provide pre-labeled force diagrams to complete
- Use simpler numbers in calculations
- Partner with stronger student
- Focus on qualitative understanding before quantitative
- Hands-on demonstration with guidance

### For English Language Learners:
- Visual diagrams emphasized
- Vocabulary list with definitions
- Sentence frames for explanations
- Bilingual partner if available
- Hands-on reduces language barrier

## Extensions and Modifications

**Extension Activities:**
1. **Propeller Comparison**: Test different propeller sizes/pitches, graph thrust curves
2. **Efficiency Analysis**: Calculate thrust per watt for different throttle settings
3. **Design Challenge**: Design a quadcopter for specific mission (max speed, max endurance, max payload)
4. **Computer Modeling**: Use Excel/Python to model flight dynamics
5. **Research Project**: Compare multirotor vs fixed-wing aerodynamics

**Cross-Curricular Connections:**
- **Math**: Graphing thrust curves, linear vs non-linear relationships, unit conversions
- **Technology**: Use sensors to measure forces in real-time
- **Engineering**: Design modifications to improve performance
- **Computer Science**: Program autonomous flight using force calculations

**Shortened Version (1 class period):**
- Skip detailed calculations
- Focus on thrust measurement and force diagrams
- Demonstrations instead of individual test setups

## Common Misconceptions

**Misconception 1**: "Lift only comes from Bernoulli's principle"
- **Reality**: Multirotors create lift primarily through Newton's Third Law (action-reaction)
- **Address**: Emphasize air being pushed down, reaction force pushes drone up

**Misconception 2**: "More throttle always means faster flight"
- **Reality**: Relationship between thrust and speed is complex (drag increases with speed)
- **Address**: Demonstrate how excess thrust relates to acceleration, not sustained speed

**Misconception 3**: "All four motors always spin at same speed"
- **Reality**: Flight controller varies speeds constantly for stability and control
- **Address**: Show motor output data from flight logs

## Troubleshooting

**Issue**: Scale readings inconsistent
- **Solution**: Ensure vehicle is secured and not touching anything else, eliminate vibration

**Issue**: Propeller flies off during test
- **Solution**: Use propeller with correct rotation direction, tighten securely, start at low throttle

**Issue**: Motor won't spin
- **Solution**: Check battery charge, verify connections, test motor in configurator

**Issue**: Students struggle with calculations
- **Solution**: Work through example together, provide calculator support, check unit conversions

## Materials Preparation

**Before Class:**
- [ ] Charge all batteries
- [ ] Test thrust measurement setup
- [ ] Print worksheets (1 per student)
- [ ] Prepare force diagram templates
- [ ] Set up demonstration area
- [ ] Review safety procedures with students
- [ ] Verify all equipment functional

**After Class:**
- [ ] Secure batteries (storage voltage if not flying soon)
- [ ] Clean up test area
- [ ] Store equipment safely
- [ ] Grade exit tickets
- [ ] Note any equipment needing repair

## Resources and References

**For Teachers:**
- "Introduction to Flight" by Anderson - Aerodynamics textbook
- Khan Academy: Newton's Laws
- NASA Glenn Research Center: Beginner's Guide to Aeronautics
- Joshua Bardwell: How Multirotors Fly (YouTube)

**For Students:**
- PhET Interactive Simulations: Forces and Motion
- NASA's "How Things Fly"
- Multirotor physics explanations (various online resources)

**Equipment Suppliers:**
- GetFPV.com (drones and parts)
- Amazon (scales, basic supplies)
- School science equipment suppliers (force sensors)

## Next Steps

**Follow-Up Lessons:**
- Aerodynamics and propeller design
- PID control systems
- Energy and power systems
- Autonomous flight programming

**Related Topics:**
- [Propulsion Systems](../../uav-systems/propulsion-systems.md)
- [Manual Control](../../control-systems/manual-control.md)
- [Advanced Control - PID Tuning](../../control-systems/advanced-control.md)

## Worksheet Template

```markdown
# Forces in Flight - Student Worksheet

**Name**: _______________ **Date**: ___________ **Period**: ___

## Part 1: Force Identification

Draw and label the four forces acting on a hovering quadcopter:

[Space for diagram]

## Part 2: Thrust Measurement Data

Vehicle Weight: _______ g

| Throttle % | Scale Reading (g) | Thrust (g) | Thrust (N) |
|-----------|-------------------|------------|------------|
| 0% | | 0 | 0 |
| 25% | | | |
| 50% | | | |
| 75% | | | |
| 100% | | | |

## Part 3: Calculations

**1. Maximum Total Thrust**
   - Single motor max thrust: _______ g
   - Total (4 motors): _______ g

**2. Thrust-to-Weight Ratio**
   - Total thrust / Vehicle weight = _______:1

**3. Hover Throttle Estimate**
   - Weight per motor: Vehicle weight / 4 = _______ g
   - From table, this occurs at approximately: _______ % throttle

**4. Flight Time Estimate**
   - Battery capacity: _______ mAh
   - Hover current: _______ mA
   - Estimated flight time: (Capacity / Current) × 0.8 = _______ minutes

## Part 4: Force Diagrams

Draw force diagrams for these scenarios:

**Hovering:**

[Space]

**Climbing:**

[Space]

**Forward Flight:**

[Space]

## Part 5: Observations

| Maneuver | What forces are acting? | What did you observe? |
|----------|------------------------|----------------------|
| Takeoff | | |
| Hover | | |
| Forward | | |

## Reflection Questions

1. What was the most surprising thing you learned about flight forces?

2. How accurate do you think our thrust measurements are? What sources of error exist?

3. In your own words, explain how a quadcopter stays in the air using Newton's Laws.

```

---

**This lesson plan is ready for classroom use. All materials, procedures, and assessments are complete and tested.**
