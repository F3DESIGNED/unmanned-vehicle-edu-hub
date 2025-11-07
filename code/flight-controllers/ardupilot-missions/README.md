# ArduPilot Mission Scripts

Python scripts for autonomous UAV missions using DroneKit and MAVLink.

## Prerequisites

### Software
```bash
# Install DroneKit
pip3 install dronekit dronekit-sitl

# Optional: MAVProxy for advanced control
pip3 install MAVProxy
```

### Hardware
- ArduPilot flight controller (Pixhawk, Cube, Matek, etc.)
- Telemetry radio or USB connection
- Fully configured and tested quadcopter

## Scripts

### simple_takeoff.py
Basic autonomous takeoff, hover, and land.

**Usage**:
```bash
# Serial connection (telemetry or USB)
python3 simple_takeoff.py --connect /dev/ttyUSB0 --altitude 10

# UDP connection (SITL simulator or WiFi)
python3 simple_takeoff.py --connect udp:127.0.0.1:14550 --altitude 5

# TCP connection
python3 simple_takeoff.py --connect tcp:192.168.1.100:5760
```

**Arguments**:
- `--connect`: Connection string (serial port, UDP, TCP)
- `--altitude`: Target altitude in meters (default: 10)
- `--hover-time`: Hover duration in seconds (default: 10)

## Testing in Simulator (SITL)

ArduPilot Software-In-The-Loop (SITL) allows safe testing without hardware.

### 1. Start SITL Simulator
```bash
# Install dronekit-sitl (if not already)
pip3 install dronekit-sitl

# Start simulator
dronekit-sitl copter --home=-35.363261,149.165230,584,353
```

### 2. Connect MAVProxy (Optional)
```bash
# In new terminal
mavproxy.py --master tcp:127.0.0.1:5760 --out udp:127.0.0.1:14550
```

### 3. Run Script
```bash
# In another terminal
python3 simple_takeoff.py --connect udp:127.0.0.1:14550 --altitude 20
```

## Safety Checklist

Before flying real hardware:

- [ ] Test script in SITL simulator first
- [ ] Test with propellers OFF (motor test only)
- [ ] Verify GPS lock (10+ satellites)
- [ ] Check battery voltage (>14V for 4S, >11V for 3S)
- [ ] Ensure failsafes configured (low battery, RC loss)
- [ ] Have manual control ready (RC transmitter)
- [ ] Fly in open area, no obstacles/people
- [ ] Start with low altitude (3-5m) for first real test

## Connection Strings

### Serial/USB
```python
--connect /dev/ttyUSB0         # Linux
--connect /dev/ttyACM0         # Linux (direct USB)
--connect COM3                 # Windows
--connect /dev/tty.usbserial-* # macOS
```

### Network
```python
--connect udp:127.0.0.1:14550  # UDP (SITL default)
--connect tcp:192.168.1.100:5760  # TCP
--connect udpin:0.0.0.0:14550  # UDP listen mode
```

### Baud Rates
- **Telemetry Radio**: 57600 (default)
- **USB**: 115200 (common)
- Specify with `:baud=XXXX` if needed: `--connect /dev/ttyUSB0:baud=115200`

## Troubleshooting

### Can't Connect
- **Check port**: `ls /dev/tty*` (Linux), Device Manager (Windows)
- **Permissions**: `sudo usermod -a -G dialout $USER` (Linux, requires logout)
- **Baud rate**: Match flight controller setting (usually 57600)

### Vehicle Won't Arm
- **GPS Lock**: Need 10+ satellites for GUIDED mode
- **Pre-arm Checks**: Check Mission Planner/QGC for errors
- **Mode**: Must be in GUIDED mode for DroneKit arming

### Script Errors
- **ImportError**: Install dronekit: `pip3 install dronekit`
- **Timeout**: Increase timeout in `connect()` call
- **AttributeError**: Ensure vehicle fully initialized with `wait_ready=True`

## Learning Activities

### Beginner
1. Modify hover time and altitude
2. Add print statements to show more vehicle state
3. Implement pre-flight safety checks

### Intermediate
4. Add waypoint navigation (fly to GPS coordinates)
5. Implement battery monitoring and auto-land
6. Create square/circle flight pattern

### Advanced
7. Multi-vehicle coordination
8. Precision landing with vision
9. Obstacle avoidance integration

## Additional Resources

- [DroneKit Documentation](https://dronekit-python.readthedocs.io/)
- [ArduPilot Developer Guide](https://ardupilot.org/dev/)
- [MAVLink Protocol](https://mavlink.io/en/)

## License

MIT License - Free to use and modify.

---

**Back to**: [Flight Controller Programming](../../../docs/programming/flight-controller-programming/) | [Code Examples](../../)
