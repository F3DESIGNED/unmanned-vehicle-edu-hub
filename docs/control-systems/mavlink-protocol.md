# MAVLink Protocol

MAVLink (Micro Air Vehicle Link) is the de facto standard communication protocol for unmanned vehicles. It enables communication between flight controllers, ground stations, companion computers, and other MAVLink-compatible systems.

## What is MAVLink?

MAVLink is a lightweight messaging protocol designed for:

- **Telemetry**: Real-time vehicle state monitoring
- **Commands**: Sending instructions to vehicle
- **Mission Management**: Uploading and managing waypoint missions
- **Parameter Configuration**: Reading and writing vehicle settings
- **File Transfer**: Log downloads, firmware updates

```mermaid
graph LR
    A[Ground Station] <-->|MAVLink| B[Telemetry Radio]
    B <-->|MAVLink| C[Flight Controller]
    C <-->|MAVLink| D[Companion Computer]
    D <-->|MAVLink| E[Payload Controller]
```

## MAVLink Versions

### MAVLink 1.0
- Original version
- 8-byte header
- Maximum 255 message IDs
- Still widely supported

### MAVLink 2.0
- Extended message IDs (24-bit)
- Packet signing for security
- Message extensions
- Backward compatible
- **Recommended for new projects**

## Protocol Structure

### MAVLink 2.0 Packet Format

```
| STX | LEN | INC | CMP | SEQ | SYS | COM | MSG_ID (24-bit) | PAYLOAD | CHECKSUM | SIGNATURE |
```

**Field Descriptions:**

- **STX**: Start byte (0xFD for MAVLink 2)
- **LEN**: Payload length
- **INC**: Incompatibility flags
- **CMP**: Compatibility flags
- **SEQ**: Packet sequence number
- **SYS**: System ID (sender)
- **COM**: Component ID (sender)
- **MSG_ID**: Message type identifier
- **PAYLOAD**: Message-specific data
- **CHECKSUM**: CRC for error detection
- **SIGNATURE** (optional): Cryptographic signature

## System and Component IDs

### System IDs
Identify different vehicles in a multi-vehicle system:

- `1`: First vehicle
- `2`: Second vehicle
- `255`: Ground station (typical)
- `0`: Broadcast to all systems

### Component IDs
Identify subsystems within a vehicle:

- `1`: Autopilot/flight controller
- `100`: Camera
- `140`: Companion computer
- `155`: GPS1
- `156`: GPS2
- `190`: Gimbal

**Example:**
A message from System 1, Component 1 (flight controller) to System 255 (ground station).

## Common Message Types

### Telemetry Messages

#### HEARTBEAT (ID: 0)
Sent periodically by all MAVLink systems.

**Contents:**
- System type (quadcopter, rover, etc.)
- Autopilot type (ArduPilot, PX4, etc.)
- System mode
- Armed state

**Frequency:** 1 Hz typical

**Purpose:**
- Presence detection
- System identification
- Connection health monitoring

#### ATTITUDE (ID: 30)
Vehicle orientation and rotation rates.

**Contents:**
- Roll, pitch, yaw (radians)
- Roll rate, pitch rate, yaw rate (rad/s)

**Frequency:** 10-50 Hz

**Educational Use:**
- Real-time orientation display
- Flight dynamics analysis
- Student flight performance review

#### GLOBAL_POSITION_INT (ID: 33)
GPS position and velocity.

**Contents:**
- Latitude, longitude (degrees * 1e7)
- Altitude MSL, altitude AGL (mm)
- Ground velocity X, Y, Z (cm/s)
- Heading (centidegrees)

**Frequency:** 5-10 Hz

**Educational Use:**
- Map-based tracking
- Navigation performance analysis
- Speed and heading displays

#### GPS_RAW_INT (ID: 24)
Raw GPS sensor data.

**Contents:**
- Latitude, longitude, altitude
- Satellites visible
- Fix type (none, 2D, 3D, DGPS, RTK)
- HDOP, VDOP (dilution of precision)
- Velocity and course

**Educational Use:**
- GPS quality monitoring
- Satellite constellation analysis
- Understanding GPS limitations

#### SYS_STATUS (ID: 1)
System health and status.

**Contents:**
- Battery voltage and current
- Battery remaining (%)
- Communication drops
- Communication errors
- Sensor health flags

**Frequency:** 1-10 Hz

**Educational Use:**
- Battery monitoring
- System health dashboard
- Failure detection

### Command Messages

#### COMMAND_LONG (ID: 76)
Generic command packet.

**Common Commands:**

| Command ID | Name | Purpose |
|-----------|------|---------|
| 16 | MAV_CMD_NAV_WAYPOINT | Navigate to waypoint |
| 21 | MAV_CMD_NAV_LAND | Land at location |
| 22 | MAV_CMD_NAV_TAKEOFF | Takeoff from ground |
| 300 | MAV_CMD_MISSION_START | Start mission |
| 400 | MAV_CMD_COMPONENT_ARM_DISARM | Arm/disarm motors |
| 176 | MAV_CMD_DO_SET_MODE | Change flight mode |

**Example - Arm Command:**
```
command: 400 (MAV_CMD_COMPONENT_ARM_DISARM)
param1: 1 (arm = 1, disarm = 0)
param2: 0 (unused)
confirmation: 0
target_system: 1
target_component: 1
```

#### MISSION_ITEM_INT (ID: 73)
Mission waypoint definition.

**Contents:**
- Sequence number
- Frame (global, relative, terrain)
- Command (waypoint, loiter, land, etc.)
- Parameters (specific to command)
- Latitude/longitude (degrees * 1e7)
- Altitude

**Educational Use:**
- Programming missions
- Understanding mission structure
- Custom mission command implementation

### Parameter Messages

#### PARAM_REQUEST_LIST (ID: 21)
Request all parameters from vehicle.

#### PARAM_REQUEST_READ (ID: 20)
Request specific parameter value.

#### PARAM_SET (ID: 23)
Set parameter value.

**Educational Use:**
- Configuration management
- Performance tuning
- Understanding vehicle settings

## Communication Links

### Serial Connection (UART)
Direct wired connection between devices.

**Typical Use:**
- Flight controller ↔ Telemetry radio
- Flight controller ↔ Companion computer
- Ground station ↔ Telemetry radio via USB

**Configuration:**
- Baud rate: 57600 (standard), 115200 (higher throughput)
- Data bits: 8
- Parity: None
- Stop bits: 1

**Wiring:**
```
Device A TX → Device B RX
Device A RX → Device B TX
GND → GND
```

### Wireless Telemetry
Radio link for remote communication.

**Common Frequencies:**
- 433 MHz: Long range, may require license
- 868 MHz: European ISM band
- 915 MHz: North American ISM band
- 2.4 GHz: Short range, high bandwidth

**Popular Systems:**
- SiK Radios: 433/915 MHz, open-source firmware
- RFD900x: Long range, 900 MHz
- XBee: Mesh networking capable
- ESP8266/ESP32: WiFi-based, low cost

**Recommended for Education:**
SiK radios (433/915 MHz) - reliable, affordable, configurable

### Network (UDP/TCP)
IP-based communication over WiFi or Ethernet.

**Applications:**
- Companion computer to ground station
- Simulation (SITL) connections
- High-bandwidth telemetry
- Multiple simultaneous connections

**Example:**
```
Ground Station: 192.168.1.100:14550 (receive)
Vehicle WiFi: 192.168.1.10:14555 (transmit)
Protocol: UDP
```

## Ground Control Stations

### Mission Planner
**Platform:** Windows (primarily)
**Features:**

- Comprehensive parameter management
- Flight planning
- Real-time telemetry
- Log analysis
- HUD displays
- Script execution

**Best For:** Advanced configuration, ArduPilot systems

### QGroundControl
**Platform:** Windows, Mac, Linux, Android, iOS
**Features:**

- Cross-platform
- Modern interface
- PX4 and ArduPilot support
- Video streaming
- Mobile-friendly

**Best For:** Versatility, in-field operations

### MAVProxy
**Platform:** Command-line, Windows/Mac/Linux
**Features:**

- Lightweight
- Scriptable
- Module-based
- Python integration
- Multiple simultaneous connections

**Best For:** Automation, development, headless systems

## Companion Computers

Companion computers add computational power for advanced autonomy, computer vision, and custom behaviors.

### Popular Companion Computer Platforms

#### Raspberry Pi 4
**Specs:**

- 4 cores @ 1.5 GHz
- 2-8 GB RAM
- GPIO, USB, CSI camera
- ~$35-75

**Best For:** Computer vision, moderate AI workloads

#### NVIDIA Jetson Nano
**Specs:**

- Quad-core ARM @ 1.43 GHz
- 4 GB RAM
- 128-core Maxwell GPU
- ~$100

**Best For:** Deep learning, real-time AI, advanced vision

#### Odroid XU4
**Specs:**

- 8 cores (4+4 big.LITTLE)
- 2 GB RAM
- USB 3.0
- ~$60

**Best For:** Performance-intensive tasks, good cooling

### Connecting Companion Computer

**Physical Connection:**
```
Flight Controller TELEM2 (UART) → Companion Computer GPIO/USB
TX → RX
RX → TX
GND → GND
+5V → +5V (if powering companion from FC)
```

**Configuration:**

Flight controller parameters (ArduPilot):
```
SERIAL2_PROTOCOL = 2 (MAVLink 2)
SERIAL2_BAUD = 921600 (high speed)
```

Companion computer (example using MAVProxy):
```bash
mavproxy.py --master=/dev/ttyAMA0 --baudrate 921600 \
            --out=udp:192.168.1.100:14550
```

### DroneKit (Python Library)

Simple programmatic control using MAVLink:

```python
from dronekit import connect, VehicleMode

# Connect to vehicle
vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=921600)

# Read telemetry
print(f"Battery: {vehicle.battery.voltage}V")
print(f"GPS: {vehicle.gps_0.satellites_visible} satellites")
print(f"Mode: {vehicle.mode.name}")

# Send command
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True

# Listen to attribute changes
@vehicle.on_attribute('location.global_frame')
def location_callback(self, attr_name, value):
    print(f"Location: {value}")

# Close connection
vehicle.close()
```

### MAVSDK (C++/Python/Other)

Modern, asynchronous MAVLink library:

```python
import asyncio
from mavsdk import System

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    # Wait for connection
    async for state in drone.core.connection_state():
        if state.is_connected:
            break

    # Arm and takeoff
    await drone.action.arm()
    await drone.action.takeoff()

    await asyncio.sleep(10)

    # Land
    await drone.action.land()

asyncio.run(run())
```

## Custom MAVLink Messages

### Creating Custom Messages

For specialized payloads or custom behaviors, define custom messages.

**Steps:**
1. Define message in XML (MAVLink message definitions)
2. Generate code using MAVLink generator
3. Implement in flight controller firmware
4. Update ground station to parse messages

**Example XML Definition:**
```xml
<message id="12345" name="CUSTOM_SENSOR">
  <description>Custom sensor reading</description>
  <field type="uint64_t" name="time_usec">Timestamp (microseconds)</field>
  <field type="float" name="temperature">Temperature (Celsius)</field>
  <field type="float" name="pressure">Pressure (Pa)</field>
  <field type="uint8_t" name="sensor_id">Sensor identifier</field>
</message>
```

### Educational Project: Custom Telemetry

**Objective:** Add environmental sensor to vehicle and display data in ground station.

**Hardware:**
- BME280 sensor (temperature, pressure, humidity)
- Companion computer
- I2C connection

**Software:**
1. Read sensor on companion computer
2. Package as MAVLink message
3. Send to ground station
4. Display in custom widget

## Debugging MAVLink

### MAVLink Inspector (QGroundControl)
View all MAVLink messages in real-time:

1. Open QGroundControl
2. Click "Analyze Tools"
3. Select "MAVLink Inspector"
4. See all message types and rates

### Wireshark with MAVLink Plugin
Capture and analyze MAVLink traffic:

1. Install Wireshark
2. Add MAVLink dissector plugin
3. Capture on serial or network interface
4. Filter by message types

### MAVLink Console (MAVProxy)
Command-line message monitoring:

```bash
mavproxy.py --master=/dev/ttyUSB0
MAV> status
MAV> watch ATTITUDE
```

## Common MAVLink Issues

### No Telemetry Received
**Troubleshooting:**

- [ ] Check physical connections (TX↔RX, GND)
- [ ] Verify baud rates match on both ends
- [ ] Confirm SERIAL port protocol set to MAVLink
- [ ] Check radio link if wireless
- [ ] Use LED indicators to confirm data transmission
- [ ] Try different USB cable/port

### Intermittent Connection
**Causes:**

- Poor radio signal strength
- Electrical interference
- Loose connections
- Insufficient power supply
- Buffer overruns

**Solutions:**

- Improve antenna placement and orientation
- Add shielding or ferrite beads
- Secure all connectors
- Use adequate power supply
- Reduce telemetry stream rates

### Parameter Upload Failures
**Causes:**

- Weak connection during transfer
- Buffer limitations
- Incompatible parameter values

**Solutions:**

- Retry closer to vehicle
- Upload parameters individually
- Check value ranges in documentation
- Use ground connection (USB) for bulk changes

## Learning Activities

### Activity 1: MAVLink Message Analysis
**Duration:** 1 hour
**Objectives:** Understand message structure and frequency
**Materials:** Connected vehicle, ground station with MAVLink inspector

1. Connect to vehicle
2. Open MAVLink inspector
3. Identify 10 different message types
4. Record message rates
5. Document message contents
6. Explain purpose of each

**Assessment:** Completeness of documentation, understanding of message purposes

### Activity 2: Custom Telemetry Display
**Duration:** 2-3 hours
**Objectives:** Create custom ground station display
**Materials:** Ground station software with scripting, vehicle

1. Choose 5 telemetry parameters
2. Create dashboard layout
3. Implement using ground station scripting (Python, Lua)
4. Add alerts for critical conditions
5. Test with real vehicle data

**Assessment:** Functionality, usability, appropriate alerts

### Activity 3: Companion Computer Communication
**Duration:** 3-4 hours
**Objectives:** Establish MAVLink communication from companion computer
**Materials:** Raspberry Pi, flight controller, connecting cables

1. Wire Pi to flight controller
2. Configure serial port on flight controller
3. Install DroneKit or MAVSDK on Pi
4. Write script to read telemetry
5. Display on Pi console or LCD
6. Optionally: Send simple command

**Assessment:** Successful communication, script functionality

## Assessment Rubric

| Skill | Novice | Developing | Proficient | Expert |
|-------|--------|-----------|-----------|--------|
| Protocol Knowledge | Can't explain structure | Understands basics | Explains message flow | Implements custom messages |
| Connection Setup | Needs step-by-step help | Connects with reference | Independent setup | Troubleshoots complex issues |
| Telemetry Interpretation | Doesn't understand values | Recognizes key parameters | Analyzes trends | Identifies anomalies proactively |
| Programming | Can't modify examples | Runs existing scripts | Writes basic scripts | Creates robust applications |

## Safety Considerations

!!! warning "MAVLink Security"
    - MAVLink 1.0 is **not encrypted** - anyone can intercept and send commands
    - Use MAVLink 2.0 with message signing for critical applications
    - Secure WiFi connections with WPA2 at minimum
    - Consider geofencing and operator authorization for classroom environments
    - Disable remote arming in multi-user environments

## Next Steps

- Apply MAVLink knowledge to [Autonomous Control](autonomous-control.md) programming
- Learn [Advanced Control](advanced-control.md) parameter tuning via MAVLink
- Build custom telemetry for [Curriculum Projects](../curriculum-integration/lesson-plans/autonomous-algorithms.md)

## Additional Resources

- **MAVLink Developer Guide**: Complete protocol specification
- **ArduPilot MAVLink Interface**: Flight controller implementation details
- **DroneKit Documentation**: Python library tutorials and API reference
- **MAVSDK Guide**: Modern asynchronous MAVLink programming
- **MAVLink Message Definitions**: XML files defining all standard messages
