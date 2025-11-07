# INAV Flight Controller

INAV (INternet of AViation) is a GPS-enabled navigation firmware perfect for autonomous waypoint missions, long-range flight, and return-to-home capabilities on racing-style hardware.

## Overview

**INAV** bridges the gap between Betaflight's manual control focus and ArduPilot's advanced autonomy. It provides GPS waypoint navigation on affordable racing flight controllers.

### Key Features
- **GPS Waypoint Missions**: Full autonomous navigation
- **Return to Home (RTH)**: Automatic emergency return
- **Position Hold**: GPS-assisted hovering
- **Based on Betaflight**: Familiar interface and configuration
- **Excellent Fixed-Wing Support**: Superior to Betaflight for planes
- **OSD with GPS Data**: Real-time navigation info in goggles

### Educational Strengths
- GPS autonomy on budget hardware
- Easier than ArduPilot for basic missions
- Good for learning navigation concepts
- Excellent for long-range exploration
- Fixed-wing support (trainer planes, flying wings)

### Limitations
- Less advanced than ArduPilot for complex missions
- Not optimized for racing/acrobatics (use Betaflight instead)
- Limited sensor integration compared to Pixhawk
- Smaller community than Betaflight

### When to Use INAV
- You want GPS missions but don't need Pixhawk-level complexity
- Budget constraints (uses same FCs as Betaflight)
- Fixed-wing educational platforms
- Long-range exploration projects
- Teaching navigation fundamentals

## Supported Hardware

### Flight Controllers

INAV supports most F4, F7, and H7 flight controllers that support Betaflight.

#### Recommended Hardware

**Matek F722-SE** ($50-60)
- Built-in barometer, magnetometer, SD card
- Excellent sensor suite for navigation
- **Best For**: Most educational INAV builds

**Matek F722-WPX** ($60-70)
- Wing-specific design
- Voltage regulator for servos
- **Best For**: Fixed-wing platforms

**Matek F405-SE/STD** ($30-45)
- Budget option with good sensors
- **Best For**: Entry-level GPS navigation learning

**SpeedyBee F7 V3** ($45-55)
- Integrated barometer
- WiFi configuration option
- **Best For**: Modern all-around navigation builds

### Required Peripherals

#### GPS Module (Essential)
**M8N GPS** ($15-25)
- Dual GPS + Compass module
- Most common, good accuracy (2-3m)
- UBLOX M8N chip

**M10 GPS** ($25-40)
- Newer generation, faster lock
- Better accuracy (~1-2m)
- UBLOX M10 chip

**Beitian BN-880** ($20-30)
- Integrated compass and GPS
- Good budget option

#### Magnetometer (Compass)
- Usually integrated with GPS module
- Essential for accurate heading
- External compass less prone to interference than onboard

#### Barometer
- Usually built into flight controller
- Required for altitude hold
- Check FC specs to confirm presence

## Installation & Setup

### INAV Configurator

**Download**: [INAV Configurator](https://github.com/iNavFlight/inav-configurator/releases)

Available for Windows, Mac, Linux, Android.

### Firmware Installation

1. **Connect FC via USB**
2. **Firmware Flasher** tab
3. **Select Target**: Auto-detect or manual selection
4. **Select Version**: Latest stable (7.0+ as of 2024)
5. **Flash Firmware**
6. **Reconnect** after completion

**Note**: INAV and Betaflight cannot coexist - flashing one overwrites the other

### Setup Wizard

INAV includes a comprehensive setup wizard.

#### 1. Board & Vehicle Type

**Board Orientation**:
- 0° for standard FC mounting
- Adjust if FC mounted at angle

**Vehicle Type**:
- **Multirotor**: Quadcopter, hexacopter, etc.
- **Airplane**: Fixed-wing platforms
- **Flying Wing**: Delta wing, no tail

#### 2. Calibration

**Accelerometer**:
- Place vehicle on level surface
- Click calibrate, wait for completion

**Magnetometer (Compass)**:
- Critical for navigation
- Calibrate outdoors, away from metal
- Rotate vehicle in all orientations
- Progress bars turn green when complete

**Tips**:
- Do compass calibration in the area you'll fly (local magnetic field)
- Keep motors/ESCs powered during calibration (they affect magnetic field)
- Re-calibrate if you move to significantly different location

#### 3. GPS Configuration

**GPS Protocol**: Auto-detect (UBLOX, NMEA, MSP)
**Baudrate**: 115200 for UBLOX

**Connection**:
- GPS TX → FC RX (usually UART2 RX)
- GPS RX → FC TX (usually UART2 TX)
- +5V, GND

**Compass Orientation**:
- Set to match your GPS module mounting
- 0° for standard forward-facing
- Use "Compass Align" if mounted at angle

#### 4. Receiver Setup

**Serial Receivers** (SBUS, CRSF):
- Connect to UART (usually UART1 or UART3)
- Select serial protocol

**Verify Channels**:
- All sticks should show movement
- Range approximately 1000-2000μs

#### 5. Motor & ESC Configuration

**Motor Layout**:
- Select quad X, quad H, hexa X, etc.

**ESC Protocol**:
- **DSHOT600**: Recommended
- **DSHOT300**: More reliable for longer ESC wires
- **Oneshot125**: Legacy, still works

**Motor Direction**:
- INAV supports motor direction reversal (DShot required)
- Or swap any two motor wires

## Flight Modes

### Manual Modes

**Angle Mode** (Self-Leveling)
- Horizon stays level when sticks centered
- **Best For**: Beginners, line-of-sight, stable video

**Horizon Mode**
- Self-leveling near center
- Allows flips/rolls at extreme stick positions
- Blends Angle and Acro

**Acro Mode** (Manual)
- No self-leveling, full manual control
- Less common in INAV (most users want GPS features)

### GPS-Assisted Modes

**NAV Alt Hold**
- Maintains altitude using barometer
- Manual horizontal control
- **Best For**: Easier manual flight

**NAV Pos Hold**
- Maintains position using GPS
- Holds altitude and horizontal position
- **Best For**: Stable hovering, photographs, testing

**NAV Cruise**
- Maintains heading and altitude
- Like cruise control for multirotors/planes
- **Best For**: Long-range cruising

### Autonomous Modes

**NAV RTH** (Return to Home)
- Climbs to safe altitude, flies straight home, lands
- Triggered manually or by failsafe
- **Best For**: Emergency return, low battery, signal loss

**NAV WP** (Waypoint)
- Follows pre-programmed mission
- Flies through GPS coordinates
- **Best For**: Autonomous missions, mapping, demonstrations

**NAV Launch** (Fixed-Wing)
- Hand-launch detection for airplanes
- Automatic climb to cruise altitude
- **Best For**: Airplane launches

### Emergency Modes

**Failsafe**
- Activates automatically on signal loss
- Default: RTH mode
- **Critical Safety Feature**

## Configuration

### Ports Tab

Assign peripherals to UARTs.

**Typical Configuration**:
- **UART1**: Receiver (Serial RX)
- **UART2**: GPS (GPS)
- **UART3**: VTX control (optional)
- **UART4**: BlackBox logging device

### GPS & Sensors Tab

**GPS Settings**:
- **Provider**: Auto-detect
- **Ground Speed**: For fixed-wing cruise speed
- **GPS Model**: M8N or M10

**Magnetometer**:
- Enable and calibrate
- Essential for navigation accuracy

**Barometer**:
- Enable for altitude hold
- Usually auto-detected

**Pitot Tube** (Fixed-Wing):
- Airspeed sensor for planes
- Optional but recommended for wind compensation

### Navigation Tab

#### Navigation Modes

**RTH Settings**:
- **RTH Altitude**: Climb altitude before returning (default 10m)
- **RTH Allow Landing**: Permit auto-land at home (recommended: enabled)
- **RTH Climb First**: Climb before flying home (safety)
- **RTH Altitude Control**: Mode for altitude during return

**Position Hold**:
- **Max Angle**: Maximum tilt in pos hold (20° typical)
- **Max Altitude**: Maximum altitude allowed
- **Max Speed**: Maximum horizontal speed in nav modes

#### Mission Settings

**Waypoint Settings**:
- **WP Radius**: How close to waypoint before moving to next (2m typical)
- **WP Safe Distance**: Distance from home where WP mode disabled (50m)
- **WP Max Altitude**: Maximum mission altitude (safety limit)

### Modes Tab

Assign modes to transmitter switches.

**Essential Mode Setup**:
1. **ARM**: Dedicated switch
2. **ANGLE**: Self-leveling (always active for beginners)
3. **NAV Alt Hold**: Single switch for altitude hold
4. **NAV Pos Hold**: Hold position switch
5. **NAV RTH**: Emergency return switch (easily accessible)
6. **NAV WP**: Activate mission (keep on separate switch)

**Advanced**:
- **BEEPER**: Lost model alarm
- **HOME RESET**: Set new home location
- **WP PLANNER**: Deprecated, use mission planning software

### Receiver Tab

Map channels and verify operation.

**Standard Mapping**:
- **Roll, Pitch, Throttle, Yaw**: Channels 1-4
- **AUX1-8**: Channels 5-12 (mode switches)

**Endpoint Adjustment**:
- Ensure full range 1000-2000μs
- Adjust on transmitter, not in INAV (best practice)

### PID Tuning

INAV has separate PID profiles for different flight conditions.

**Profiles**:
- **Profile 1**: Default tuning
- **Profile 2-3**: Alternative tunes (windy conditions, heavy payload)

**Tuning Recommendations**:
- Start with defaults for your vehicle type
- Adjust only if oscillations occur
- Log flights and analyze for tuning needs

### OSD Tab

Configure on-screen display for FPV goggles.

**Navigation-Specific Elements**:
- **GPS Coordinates**: Current location
- **GPS Satellites**: Lock quality (10+ ideal)
- **Home Direction**: Arrow pointing home
- **Home Distance**: Range to home point
- **Ground Speed**: Speed over ground (GPS)
- **Altitude**: Barometric or GPS altitude
- **Battery Remaining**: Critical for RTH planning

**Layout**:
- Keep critical info (battery, GPS status) always visible
- Home arrow in center for easy orientation

## Mission Planning

### Creating Waypoint Missions

#### Using INAV Configurator

1. **Mission Control** tab
2. Click map to add waypoints (Shift+Click)
3. Right-click waypoint to edit:
   - **Altitude**: Set waypoint altitude (meters)
   - **Speed**: Flight speed to waypoint (cm/s)
   - **Action**: Waypoint, RTH, Jump (loop), Land

4. **Save to FC**: Upload mission to flight controller
5. **Verify**: Check mission makes sense before flight

#### Mission Planning Software

**Mission Planner for INAV** (Desktop)
- More advanced than Configurator
- Terrain awareness
- Survey/grid patterns

**Mobile Field Configurator** (Android)
- In-field mission editing
- Mobile convenience

### Waypoint Actions

**Waypoint**: Fly to GPS coordinate at specified altitude
**RTH**: Return to home from current mission point
**Jump**: Loop back to earlier waypoint (limited loops)
**Land**: Descend and disarm at waypoint
**Set POI**: Point camera at location (requires gimbal)

### Mission Tips

1. **First Mission**: Simple 3-4 waypoint square, low altitude, slow speed
2. **RTH Altitude**: Ensure higher than all obstacles
3. **Takeoff**: Manual takeoff, engage NAV WP in air (safer than auto-takeoff)
4. **Battery Buffer**: Plan for 30% battery remaining at mission end (for RTH)
5. **Visual Range**: Keep within sight for first missions
6. **Abort Plan**: Know how to cancel mission (switch out of NAV WP mode)

### Example Missions

**Mission 1: Simple Square**
```
WP1: 10m North, 20m altitude, 5m/s
WP2: 10m East, 20m altitude, 5m/s
WP3: 10m South, 20m altitude, 5m/s
WP4: 10m West (home), 20m altitude, 5m/s
WP5: RTH (return to home)
```

**Mission 2: Survey Pattern**
```
WP1: North edge, 30m altitude
WP2: North edge + 50m East, 30m altitude
WP3: South edge + 50m East, 30m altitude
WP4: South edge + 100m East, 30m altitude
... (continue parallel lines)
WPn: RTH
```

## Failsafe Configuration

**Critical for safe autonomous flight**

### Receiver Failsafe

**Stage 1: Signal Loss Detected**
- **Procedure**: RTH (recommended)
- **Guard Time**: 0.5-1.0 seconds

**Stage 2: Extended Loss**
- **Procedure**: Land or Continue RTH
- **Time**: After 60s (adjustable)

**Configuration**:
1. **Configuration** → **Failsafe**
2. Set **Procedure** to RTH
3. Set **Throttle Low Delay** (time before disarm)
4. **Test**: Turn off transmitter, verify RTH activates

### GPS Failsafe

**Action if GPS lost during autonomous flight**:
- Emergency landing (multirotor)
- Switch to manual control (if enabled)

**Prevention**:
- Ensure 10+ satellites before autonomous modes
- Avoid flights during magnetic storms
- Keep GPS module clear of obstructions

### Battery Failsafe

**Triggers RTH at low voltage**:
- Set warning voltage (e.g., 3.5V per cell)
- Set critical voltage (e.g., 3.3V per cell)
- Plan missions to reserve 30% battery

## Pre-Flight Checklist

### GPS-Specific Checks

- [ ] **GPS Lock**: 10+ satellites, HDOP <2.0
- [ ] **Home Position Set**: Verify on OSD or Configurator map
- [ ] **Compass Calibrated**: Check heading accuracy (compare to phone compass)
- [ ] **Flight Plan Loaded**: Mission uploaded and verified
- [ ] **RTH Altitude**: Set above all obstacles in area
- [ ] **Battery Sufficient**: Enough for mission + 30% reserve
- [ ] **Failsafes Tested**: RTH triggers correctly on signal loss
- [ ] **Weather Check**: Wind <15mph for beginners, no rain

### Standard Pre-Flight

- [ ] Props secure and undamaged
- [ ] All screws tight
- [ ] Battery voltage correct
- [ ] Radio signal strong
- [ ] Motors spin correctly (with props OFF)

## Flying with INAV

### First GPS Flight

1. **Takeoff Manually** in Angle mode
2. **Gain Altitude**: Climb to 10-20m
3. **Test Alt Hold**: Switch to NAV Alt Hold, verify altitude locks
4. **Test Pos Hold**: Switch to NAV Pos Hold, let go of sticks, verify holds position
5. **Test RTH**: Fly 20m away, switch to NAV RTH, verify returns to home
6. **Land Manually**: Take control, descend and land

**Do NOT**:
- Engage autonomous modes during takeoff (takeoff manually first)
- Fly autonomous missions on first flight
- Trust GPS indoors (GPS doesn't work indoors)

### Autonomous Mission Flight

1. **Manual Takeoff**: Climb to mission altitude
2. **Final Check**: GPS sats, battery, home position
3. **Engage NAV WP**: Flip mission switch, vehicle flies to first waypoint
4. **Monitor**: Watch for unexpected behavior
5. **Abort if Needed**: Switch out of NAV WP to Angle mode
6. **Mission Complete**: Vehicle executes RTH or continues per mission
7. **Manual Landing**: Take control for final landing (or allow auto-land)

## Logging & Analysis

### BlackBox Logging

**Enable Logging**:
1. **Logging** tab
2. **Device**: SD Card or Flash
3. **Sample Rate**: 500Hz-1kHz

**Analysis**:
- Download logs after flight
- Open in **BlackBox Explorer**
- Check navigation performance, GPS quality, motor output

### Log Analysis for Navigation

**GPS Data**:
- Check for GPS glitches or jumps
- Verify HDOP stayed low (<2.0)
- Look for compass interference (erratic heading)

**Navigation Performance**:
- Compare desired vs actual position
- Check waypoint accuracy
- Identify drift or positioning errors

## Fixed-Wing with INAV

INAV excels at fixed-wing autonomous flight.

### Setup Differences

**Vehicle Type**: Select Airplane or Flying Wing

**Servo Configuration**:
- Assign servos to outputs
- Set servo mid-points and ranges
- Configure elevon mixing (for flying wings)

**Cruise Speed**:
- Set cruise throttle and speed
- INAV maintains airspeed automatically

**Launch Mode**:
- **NAV Launch**: Detects hand-launch, climbs to altitude
- Set climb angle and speed

### Fixed-Wing Missions

**Advantages**:
- Much longer flight times (30-60+ minutes)
- Larger coverage area
- More efficient for mapping/survey

**Considerations**:
- Requires more space (can't hover)
- Landing is more complex (landing mode or manual)
- Stall speed awareness critical

## Troubleshooting

### GPS Issues

**No GPS Lock**
- Need clear sky view (outdoors)
- Can take 2-5 minutes for first lock
- Check GPS antenna orientation (ceramic patch upward)

**Inaccurate Position Hold**
- Compass interference (recalibrate away from metal)
- Low satellite count (wait for 10+)
- High HDOP (indicates poor GPS geometry)

### Navigation Issues

**RTH Flies Wrong Direction**
- Compass not calibrated or interfered
- Solution: Recalibrate compass, check for magnetic sources

**Won't Arm in GPS Mode**
- Insufficient satellites
- Home position not set
- GPS HDOP too high

**Drifts in Pos Hold**
- Compass calibration off
- Vibration affecting sensors
- Wind exceeding position hold capability

### Failsafe Issues

**RTH Doesn't Trigger**
- Failsafe not configured correctly
- Receiver failsafe overriding (set receiver to "no pulses")
- Check failsafe tab settings

**RTH Altitude Too Low/High**
- Adjust RTH_ALT parameter
- Consider terrain and obstacles

## Educational Activities

### Navigation Experiments

1. **GPS Accuracy Test**: Pos hold for 5 minutes, measure drift from markers
2. **Waypoint Precision**: Fly mission over ground targets, measure accuracy
3. **RTH Testing**: Activate RTH from various distances and altitudes
4. **Wind Effect Study**: Fly same mission in different wind conditions
5. **Battery Life Mission**: Plan mission to test actual flight time vs theoretical

### Competition Ideas

- **Precision Landing**: Autonomous mission ending on target
- **Search Pattern**: Locate "missing person" marker with camera
- **Delivery Mission**: Carry payload to GPS coordinates
- **Speed Run**: Fastest time through waypoint course

## Safety & Best Practices

### Autonomous Flight Safety

- **Always have manual override ready**: Know how to quickly switch to Angle mode
- **Visual observer required**: Someone watching drone at all times
- **Geofencing**: Set max altitude and distance limits
- **Start conservative**: Slow speeds, low altitudes, simple missions
- **Battery reserve**: Always plan for 30% remaining after mission

### Legal Considerations

- **FAA Part 107**: Required for commercial use in US
- **VLOS Requirement**: Maintain visual line of sight
- **Registration**: >250g drones must be registered
- **Airspace Authorization**: Required for controlled airspace

## Resources

### Software Downloads

- [INAV Configurator](https://github.com/iNavFlight/inav-configurator/releases)
- [Mobile Configurator (Android)](https://play.google.com/store/apps/details?id=com.eziosoft.ezgui)
- [Mission Planner for INAV](https://github.com/iNavFlight/inav-configurator/wiki)

### Documentation

- [INAV GitHub Wiki](https://github.com/iNavFlight/inav/wiki)
- [INAV Fixed-Wing Guide](https://github.com/iNavFlight/inav/wiki/Howto:-CC3D-flight-controller-board-setup-for-GPS-navigation)
- [INAV Discord](https://discord.gg/peg2hhbYwN) - Community support

### Learning Resources

- **Painless360 YouTube**: Excellent INAV tutorials and setup guides
- **INAV Official YouTube**: Feature demonstrations
- **Nick Burns YouTube**: Fixed-wing INAV focus

### Example Configurations

- [INAV Mission Examples](../../../code/flight-controllers/inav-missions/)
- [Fixed-Wing Configs](../../../code/flight-controllers/inav-configs/fixed-wing/)

---

**Next**: [CleanFlight →](cleanflight.md) | [Back to Flight Controllers →](../index.md)
