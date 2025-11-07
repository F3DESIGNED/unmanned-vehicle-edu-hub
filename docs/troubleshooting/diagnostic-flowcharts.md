# Diagnostic Flowcharts

Visual decision trees to guide systematic troubleshooting of common issues. Follow the flow from symptoms to solutions.

## How to Use These Flowcharts

1. **Start at the top** with your symptom
2. **Answer questions** honestly at each decision point
3. **Follow the arrows** based on your answers
4. **Perform tests** as indicated
5. **Document your path** through the flowchart
6. **If solution doesn't work**, backtrack and try alternative paths

## Vehicle Won't Arm

```mermaid
graph TD
    A[Vehicle Won't Arm] --> B{Battery Connected?}
    B -->|No| C[Connect Battery]
    B -->|Yes| D{Flight Controller Powered?}

    D -->|No| E[Check Power Connection<br/>Check Battery Voltage]
    D -->|Yes| F{Transmitter On and Bound?}

    F -->|No| G[Turn on Transmitter<br/>Check Binding]
    F -->|Yes| H{Arm Switch in Correct Position?}

    H -->|No| I[Move Switch to Arm Position]
    H -->|Yes| J{Pre-Arm Checks Passing?}

    J -->|Don't Know| K[Connect to Configurator<br/>Check Messages Tab]
    J -->|No| L{Check Specific Error}

    L --> M{GPS Lock?}
    L --> N{Compass Calibrated?}
    L --> O{Accelerometer Calibrated?}
    L --> P{Throttle at Zero?}

    M -->|No| M1[Wait for GPS Lock<br/>6+ Satellites]
    N -->|No| N1[Calibrate Compass<br/>Away from Metal]
    O -->|No| O1[Calibrate Accelerometer<br/>Level Surface]
    P -->|No| P1[Lower Throttle Stick]

    J -->|Yes| Q{Mode Allows Arming?}
    Q -->|No| R[Switch to Stabilize/Manual]
    Q -->|Yes| S[Check Arming Sequence<br/>Documentation]

    C --> T[Retest]
    E --> T
    G --> T
    I --> T
    M1 --> T
    N1 --> T
    O1 --> T
    P1 --> T
    R --> T
    S --> U[Advanced: Check Logs<br/>Seek Community Help]
```

## No Power to System

```mermaid
graph TD
    A[No Power to System] --> B{Battery Charged?}
    B -->|No| C[Charge Battery]
    B -->|Don't Know| D[Test Battery with Multimeter<br/>Should read nominal voltage]
    B -->|Yes| E{Battery Connected Properly?}

    E -->|No| F[Check Polarity<br/>Plug in Securely]
    E -->|Yes| G{Check Connector}

    G --> H{Visual Damage to Connector?}
    H -->|Yes| I[Replace Connector<br/>Resolder if Needed]
    H -->|No| J{Continuity Through Power Leads?}

    J -->|No| K[Repair Wire Break<br/>Replace Cable]
    J -->|Yes| L{Voltage at Flight Controller?}

    L -->|No| M{Fuse/Protection Blown?}
    M -->|Yes| N[Replace Fuse<br/>Find Cause of Overcurrent]
    M -->|No| O[Check PDB/Distribution<br/>Replace if Damaged]

    L -->|Yes| P{Flight Controller LED On?}
    P -->|No| Q[Flight Controller Damaged<br/>Check for Shorts]
    P -->|Yes| R[Power Present<br/>Check Other Components]

    C --> S[Retest]
    D --> B
    F --> S
    I --> S
    K --> S
    N --> T[Test Under Load<br/>Monitor Current]
    O --> S
    Q --> U[Replace FC<br/>After Confirming Issue]
    R --> V[Check Individual Component<br/>Power Requirements]
```

## Unstable Flight / Oscillations

```mermaid
graph TD
    A[Unstable Flight/Oscillations] --> B{When Does it Occur?}
    B -->|Immediately on Takeoff| C{All Conditions or Specific?}
    B -->|During Flight| D{What Throttle Position?}
    B -->|On Landing| E[Likely Ground Effect<br/>Normal for Some Builds]

    C -->|All Conditions| F{Propellers Correct?}
    F -->|Not Sure| G[Check Propeller Direction<br/>Match Motor Spin Direction]
    F -->|Yes| H{Motor Direction Correct?}

    H -->|Not Sure| I[Test in Betaflight/ArduPilot<br/>Match Diagram]
    H -->|Yes| J{Recent PID Changes?}

    J -->|Yes| K[Revert to Default PIDs<br/>Start Tuning Fresh]
    J -->|No| L{Mechanical Issues?}

    L --> M[Check for:<br/>- Bent Props<br/>- Loose Screws<br/>- Bent Arms<br/>- Cracked Frame]

    D -->|Low Throttle| N[Propwash Oscillation]
    N --> O[Increase D Gain<br/>Add Low Pass Filters]

    D -->|Mid Throttle| P[PID Tuning Issue]
    P --> Q{High Frequency Buzz?}
    Q -->|Yes| R[D Gain Too High<br/>Reduce D Term]
    Q -->|No| S[P Gain Too High<br/>Reduce P Term]

    D -->|High Throttle| T{Motors Getting Hot?}
    T -->|Yes| U[Excessive D Filtering<br/>Reduce D Gain]
    T -->|No| V[Check Vibration Dampening<br/>Soft Mount FC]

    E --> W[Reduce Throttle Earlier<br/>Land More Gently]

    G --> X[Retest]
    I --> X
    K --> X
    M --> Y[Repair/Replace<br/>Then Retest]
    O --> X
    R --> X
    S --> X
    U --> X
    V --> X
```

## GPS Issues

```mermaid
graph TD
    A[GPS Not Working] --> B{GPS Module Powered?}
    B -->|No| C[Check Wiring<br/>Check Voltage at GPS]
    B -->|Yes| D{LED on GPS Blinking?}

    D -->|No| E[Check Communication<br/>UART Settings]
    D -->|Yes| F{How Many Satellites?}

    F -->|0| G{GPS Protocol Correct?}
    G -->|Not Sure| H[Set to Auto or UBX<br/>Check FC Firmware Docs]
    G -->|Yes| I{Clear Sky View?}

    I -->|No| J[Move to Open Area<br/>Away from Buildings]
    I -->|Yes| K[GPS Module May Be Faulty<br/>Try Different Location First]

    F -->|1-5| L{Getting More Over Time?}
    L -->|Yes| M[Wait for Full Lock<br/>Can Take Several Minutes]
    L -->|No| N{Interference Present?}

    N --> O[Check for:<br/>- Metal objects nearby<br/>- Video TX interference<br/>- Power line EMI]

    F -->|6-9| P{HDOP Value?}
    P -->|>2.0| Q[Marginal GPS Quality<br/>Wait or Relocate]
    P -->|<2.0| R[Acceptable for Flight<br/>10+ Preferred]

    F -->|10+| S{Still Issues?}
    S -->|Position Hold Drift| T[Check Compass Calibration<br/>Magnetic Interference]
    S -->|Won't Use GPS| U[Check Flight Mode Requirements<br/>Enable GPS Features in FC]

    C --> V[Retest]
    E --> W[Check Parameters:<br/>SERIALx_PROTOCOL<br/>GPS_TYPE]
    H --> V
    J --> V
    K --> X[Replace GPS Module]
    M --> Y[Wait Patiently]
    O --> Z[Eliminate Interference<br/>Shield Cables]
    T --> AA[Calibrate Away from Metal<br/>Check Orientation]
    U --> AB[Enable Auto Mode<br/>Set GPS Requirements]
```

## Communication/Connection Issues

```mermaid
graph TD
    A[Can't Connect to Flight Controller] --> B{Using USB?}
    B -->|Yes| C{Computer Detects Device?}
    B -->|No| D[Using Wireless/Telemetry]

    C -->|No| E{Tried Different Cable?}
    E -->|No| F[Try Different USB Cable<br/>Data cables not just power]
    E -->|Yes| G{Tried Different USB Port?}

    G -->|No| H[Try Different Port<br/>USB 2.0 Sometimes Better]
    G -->|Yes| I{Driver Installed?}

    I -->|No| J[Install CP210x or FTDI Driver<br/>Check FC Chip Type]
    I -->|Yes| K{FC Powered Separately?}

    K -->|No| L[May Need External Power<br/>Some FCs Don't Power via USB Alone]
    K -->|Yes| M[FC Hardware Issue<br/>Check for Physical Damage]

    C -->|Yes| N{Correct COM Port Selected?}
    N -->|No| O[Select Correct Port<br/>Disconnect Others to Verify]
    N -->|Yes| P{Correct Baud Rate?}

    P -->|No| Q[Try 115200<br/>Then 57600]
    P -->|Yes| R{Boot Button Needed?}

    R -->|Maybe| S[Some FCs Need Boot Button<br/>Hold While Connecting]
    R -->|No| T[Check Firmware Compatible<br/>Reflash if Needed]

    D --> U{Radio Link Quality?}
    U -->|Weak/None| V[Check:<br/>- Antenna Connected<br/>- Power to Radio<br/>- Correct Frequency<br/>- Range]

    U -->|Good| W{MAVLink/Protocol Settings?}
    W --> X[Verify:<br/>- SERIAL Protocol<br/>- Baud Rate Match<br/>- System ID<br/>- Ground Station Settings]

    F --> Y[Retest Connection]
    H --> Y
    J --> Y
    L --> Y
    M --> Z[Inspect/Replace FC]
    O --> Y
    Q --> Y
    S --> Y
    T --> Y
    V --> AA[Fix Radio Issues<br/>See Telemetry Troubleshooting]
    X --> Y
```

## Motor Not Spinning

```mermaid
graph TD
    A[Motor Not Spinning] --> B{Which Motors?}
    B -->|All Motors| C{Armed?}
    C -->|No| D[Arm Vehicle Safely<br/>Props Off]
    C -->|Yes| E{Throttle Above Minimum?}

    E -->|No| F[Raise Throttle<br/>Check Motor Test in Config]
    E -->|Yes| G{Power to ESCs?}

    G -->|No| H[Check Power Distribution<br/>Battery Connection]
    G -->|Yes| I[Check ESC Connections<br/>All ESCs May Be Bad]

    B -->|One Motor| J{ESC Beeping Error?}
    J -->|Yes| K[Interpret Beep Code<br/>See ESC Manual]
    J -->|No| L{Swap Motor with Working One}

    L --> M{Swapped Motor Works?}
    M -->|Yes| N[Original Motor Bad<br/>Replace Motor]
    M -->|No| O{Swap ESC with Working One}

    O --> P{Swapped ESC Works?}
    P -->|Yes| Q[Original ESC Bad<br/>Replace ESC]
    P -->|No| R{Check FC Motor Output}

    R --> S[Swap FC Signal Wire]
    S --> T{Motor Now Works?}
    T -->|Yes| U[FC Motor Pad Damaged<br/>Repair or Replace FC]
    T -->|No| V[Check Wiring/Soldering<br/>Continuity Test]

    B -->|Multiple Motors| W{Same Bus/Row of ESC?}
    W -->|Yes| X[Check 4-in-1 ESC<br/>May Have Failed Section]
    W -->|No| Y{Pattern to Failure?}

    Y --> Z[Diagonal: Check FC Orientation<br/>Adjacent: Check Wiring]

    D --> AA[Retest]
    F --> AA
    H --> AB[Fix Power Issues]
    I --> AC[Diagnose ESC Issue]
    K --> AD[Address Error:<br/>- Calibration<br/>- Timing<br/>- Current Limit]
    N --> AE[Replace and Test]
    Q --> AE
    U --> AF[FC Repair Needed]
    V --> AG[Repair Connections]
    X --> AH[Replace 4-in-1 ESC]
    Z --> AI[Check Configuration]
```

## Compass Errors

```mermaid
graph TD
    A[Compass Errors/Issues] --> B{Error Type?}
    B -->|Compass Not Calibrated| C[Perform Calibration:<br/>1. Away from Metal<br/>2. Rotate All Axes<br/>3. Complete Pattern]

    B -->|Compass Variance High| D{Recent Changes to Build?}
    D -->|Yes| E[Check for:<br/>- New Magnetic Components<br/>- Moved GPS/Compass<br/>- Added Metal Parts]
    D -->|No| F{Compass Orientation Correct?}

    F -->|Not Sure| G[Verify Physical Orientation<br/>Set COMPASS_ORIENT Parameter]
    F -->|Yes| H{Magnetic Interference?}

    H --> I[Test for Interference:<br/>1. Arm Vehicle<br/>2. Increase Throttle<br/>3. Watch Compass in GCS]

    I --> J{Compass Heading Changes?}
    J -->|Yes| K[Current Causing Interference]
    K --> L[Solutions:<br/>- Move GPS/Compass Further<br/>- Use External GPS<br/>- Twist Power Wires<br/>- Add Shielding]

    J -->|No| M{Environmental Sources?}
    M --> N[Check for:<br/>- Power Lines<br/>- Large Metal Objects<br/>- Indoor Operation<br/>- Vehicle On Metal Table]

    B -->|Compass Direction Wrong| O{180° Opposite?}
    O -->|Yes| P[Rotation Issue<br/>Check COMPASS_ORIENT<br/>Try Different Settings]
    O -->|No| Q[Declination Issue<br/>Enable Auto Declination<br/>Or Set Manually]

    B -->|Multiple Compass Conflict| R{Using Multiple Compasses?}
    R -->|Yes| S[Prioritize/Disable:<br/>- Identify Which is Accurate<br/>- Disable Others<br/>- Set COMPASS_USE Parameters]
    R -->|No| T[Internal vs External<br/>Disable Internal if Using GPS/Compass]

    C --> U[Retest Outdoors]
    E --> V[Reduce Interference<br/>Recalibrate]
    G --> U
    L --> U
    N --> W[Move to Better Location<br/>Remove Sources]
    P --> U
    Q --> U
    S --> U
    T --> U
```

## Video Signal Issues (FPV)

```mermaid
graph TD
    A[FPV Video Problems] --> B{Symptom?}
    B -->|No Video| C{VTX Powered?}
    C -->|No| D[Check Power Connection<br/>Verify Voltage]
    C -->|Yes| E{Antenna Connected?}

    E -->|No| F[STOP! Connect Antenna<br/>VTX Can Burn Out]
    E -->|Yes| G{Camera Powered?}

    G -->|No| H[Check Camera Power<br/>Correct Voltage for Camera]
    G -->|Yes| I{VTX LED On?}

    I -->|No| J[VTX May Be Damaged<br/>Check for Burn Marks]
    I -->|Yes| K{Correct Channel on Goggles?}

    K -->|Not Sure| L[Auto-Scan on Goggles<br/>Or Manually Try Channels]
    K -->|Yes| M[Check Video Connection<br/>Camera to VTX]

    B -->|Static/Noise| N{How Much Static?}
    N -->|Complete Snow| O[Weak Signal<br/>Try Higher VTX Power]
    N -->|Partial| P{Patterns in Static?}

    P -->|Horizontal Lines| Q[Electrical Noise<br/>Add Capacitor to Power<br/>LC Filter Recommended]
    P -->|Random| R[RF Interference<br/>Change Channel<br/>Check Antenna]

    B -->|Intermittent| S{When Does it Cut Out?}
    S -->|During Throttle Changes| T[Power Noise<br/>Voltage Sag<br/>Add Capacitor]
    S -->|At Distance| U[Range Issue<br/>Better Antenna<br/>Higher Power<br/>Check Orientation]
    S -->|Random| V[Loose Connection<br/>Check All Cables<br/>Resolder]

    B -->|Wrong Aspect Ratio| W[Camera/VTX Mismatch<br/>Set Both to 4:3 or 16:9]

    B -->|Colored Lines| X{Vertical or Horizontal?}
    X -->|Vertical| Y[Sync Issue<br/>Check Camera Format<br/>NTSC vs PAL]
    X -->|Horizontal| Z[Noise/Interference<br/>Filter Power Supply]

    D --> AA[Retest]
    F --> AA
    H --> AA
    J --> AB[Replace VTX]
    L --> AA
    M --> AC[Resolder/Replace Cable]
    O --> AD[Increase Power<br/>Check Regulations]
    Q --> AE[Add Filtering]
    R --> AF[Change Frequency]
    T --> AE
    U --> AG[Improve RF Link]
    V --> AC
    W --> AA
    Y --> AH[Match Camera/VTX Format]
    Z --> AE
```

## Using Flowcharts in Education

### Individual Learning
Students can work through flowcharts to develop diagnostic thinking:

1. Present problem scenario
2. Student follows flowchart
3. Document decision path
4. Perform indicated tests
5. Report findings

### Group Problem Solving
Use flowcharts for collaborative troubleshooting:

1. Team reviews symptom together
2. Assign roles (reader, tester, documenter)
3. Work through flowchart as team
4. Discuss why each path was taken
5. Present solution to class

### Creating Custom Flowcharts
Advanced activity:

1. Identify common issue in your builds
2. Research troubleshooting steps
3. Create flowchart using Mermaid
4. Test with real problems
5. Refine based on results
6. Share with community

## Flowchart Symbols

Understanding the decision tree elements:

- **Rectangle**: Action to perform
- **Diamond**: Decision point / question
- **Arrow**: Flow direction
- **Terminal (rounded)**: Start or end point

## Advanced Troubleshooting

When flowcharts don't resolve the issue:

### Check Logs
Review detailed flight logs for patterns and anomalies.
[→ Log Analysis Guide](log-analysis.md)

### Component Isolation
Systematically isolate and test individual components:

1. Remove all unnecessary components
2. Test with minimal configuration
3. Add components back one at a time
4. Identify problematic component

### Voltage/Current Testing
Use multimeter to verify power delivery:

- Measure at source (battery)
- Measure at distribution (PDB)
- Measure at component
- Compare to specifications

### Waveform Analysis
For advanced users with oscilloscope:

- Check signal quality
- Identify noise sources
- Verify timing
- Analyze communication protocols

## Preventive Measures

Avoid many issues by following best practices:

- **Pre-flight Checks**: Catch problems before flight
- **Regular Inspection**: Scheduled maintenance
- **Proper Soldering**: Reduce connection failures
- **Quality Components**: Fewer failures
- **Good Cable Management**: Prevent shorts and breaks
- **Documentation**: Track changes and configurations

[→ Preventive Maintenance Guide](preventive-maintenance.md)

## Next Steps

For issues not covered by flowcharts:

- [Hardware Issues](hardware-issues.md) - Detailed component troubleshooting
- [Software Issues](software-issues.md) - Configuration and firmware problems
- [Flight Operation Issues](flight-operation-issues.md) - Flying problems
- [Log Analysis](log-analysis.md) - Interpreting flight data

## Contributing Flowcharts

Help improve this resource:

1. Identify common issues not covered
2. Draft flowchart on paper
3. Create Mermaid diagram
4. Test with real scenarios
5. Submit pull request with:
   - Flowchart code
   - Description of problem
   - Testing results

## Additional Resources

- Mermaid Live Editor: Create and test flowcharts
- Community Forums: Search for similar issues
- Flight Controller Documentation: Specific error codes
- Component Datasheets: Specifications and testing procedures
