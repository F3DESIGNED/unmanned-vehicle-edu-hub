# Software & Configuration Troubleshooting

Problems with firmware, configuration, parameters, and software setup. This guide helps resolve software-related issues.

## Connection Issues {#connection-issues}

### Can't Connect to Flight Controller

**Symptoms:**
- Configurator shows "Not connected"
- COM port not detected
- Connection timeout errors

**Solutions by Platform:**

#### USB Connection

1. **Check Cable**
   - Use data cable (not charging-only)
   - Try different cable
   - Some cheap cables are power-only

2. **Driver Installation**
   ```
   Windows:
   - CP210x driver (most common)
   - FTDI driver (some FCs)
   - STM32 VCP driver (DFU mode)

   Mac/Linux:
   - Usually built-in
   - Check dmesg for device detection
   ```

3. **COM Port Selection**
   - Correct port selected in configurator
   - Disconnect other USB devices
   - Check Device Manager (Windows)

4. **Boot/DFU Mode**
   - Some FCs need boot button pressed
   - Hold while connecting USB
   - Required for firmware recovery

#### Wireless/Telemetry Connection

1. **Radio Configuration**
   ```
   Check:
   - Both radios powered
   - Antenna connected
   - Same firmware version
   - Matched net ID/frequency
   - Correct baud rate
   ```

2. **MAVLink Settings**
   ```
   ArduPilot:
   SERIAL1_PROTOCOL = 2 (MAVLink 2)
   SERIAL1_BAUD = 57600 or 115200

   Check system ID matches ground station
   ```

3. **Network/WiFi**
   ```
   Verify:
   - Correct IP address
   - Port number (14550 default)
   - No firewall blocking
   - Same network/subnet
   ```

### Connection Drops During Operation

**Causes:**

| Issue | Symptom | Solution |
|-------|---------|----------|
| USB Cable | Random disconnects | Replace cable, avoid movement |
| Power Noise | Disconnects under throttle | Add filtering, powered USB hub |
| Radio Interference | Drops at distance/near obstacles | Better antennas, higher power |
| Software Conflict | Specific operations cause drop | Update software, close other programs |

## Firmware Problems {#firmware-problems}

### Firmware Won't Upload

**Common Errors:**

**"Failed to open COM port"**
- Close all programs using the port
- Disconnect and reconnect
- Try different USB port
- Reboot computer

**"No response from bootloader"**
- Enter DFU mode (boot button + power)
- Use correct firmware for FC
- Flash with full chip erase
- FC may be bricked (recovery mode needed)

**"Verification failed"**
- Bad flash (retry)
- Wrong firmware file
- Hardware issue with flash memory
- Try older firmware version first

### Wrong Firmware Flashed

**Symptoms:**
- FC doesn't boot
- Configurator won't connect
- Erratic behavior

**Recovery:**

1. **Identify Correct Firmware**
   - Check FC model and target
   - Betaflight: Correct target (e.g., STM32F411)
   - ArduPilot: Correct board type

2. **Enter Bootloader/DFU**
   - Hold boot button
   - Connect USB while holding
   - Should appear as DFU device

3. **Flash Correct Firmware**
   - Select exact target
   - Use "Full Chip Erase" option
   - Flash latest stable version

4. **Restore Defaults**
   - Don't restore old settings if different firmware
   - Reconfigure from scratch

### Firmware Version Incompatibilities

**Issues:**
- New features not working
- Old configuration won't load
- ESC protocol errors
- Sensor not detected

**Solutions:**

1. **Check Compatibility**
   ```
   Betaflight: Version 4.x changed many things from 3.x
   ArduPilot: Check release notes for breaking changes
   ESC Firmware: BLHeli vs BLHeli_32 compatibility
   ```

2. **Update Systematically**
   - Backup current configuration
   - Read release notes
   - Update firmware
   - Reconfigure as needed
   - Test before flight

3. **Rollback if Needed**
   - Flash previous version
   - Restore backup configuration
   - Report issues to developers

## Configuration Problems

### Settings Won't Save

**Causes:**

1. **Not Clicking Save**
   - Many configurators require explicit save
   - Look for save button
   - Wait for confirmation

2. **Flash Memory Full**
   - Too many parameters
   - Corrupted EEPROM
   - Solution: Full chip erase and reconfigure

3. **USB Disconnect During Save**
   - Use stable connection
   - Don't move cable during save
   - Verify save completed

4. **Parameter Out of Range**
   - Some values have limits
   - Check min/max in documentation
   - Error may not be obvious

### Configuration Resets After Power Cycle

**Possible Causes:**

1. **EEPROM/Flash Issues**
   - Hardware problem with FC
   - Reflash firmware with full erase
   - May need FC replacement

2. **Parameter Format Changed**
   - Firmware update changed storage
   - Reconfigure manually
   - Don't restore old backups across major versions

3. **Brownout During Boot**
   - Insufficient power
   - Add capacitor
   - Better power supply

### Wrong Configuration Loaded

**Symptoms:**
- Unexpected behavior
- Different settings than expected
- Wrong PID values

**Solutions:**

1. **Verify Target**
   - Correct board selected
   - Betaflight: Check target name
   - ArduPilot: Check SYSID_THISMAV

2. **Load Correct Profile**
   - Multiple PID profiles available
   - Rate profiles separate
   - Check active profile number

3. **Reset to Defaults**
   - Start fresh if confused
   - Load known-good configuration
   - Document working setup

## Parameter Issues

### Can't Find Parameter

**Common Reasons:**

1. **Different Firmware Version**
   - Parameter renamed or removed
   - Check release notes
   - Look for equivalent in new version

2. **Feature Not Compiled In**
   - Some builds omit features
   - ArduPilot: Check build type
   - May need different firmware

3. **Search Method**
   - Use search function in configurator
   - Check parameter documentation
   - Parameters are case-sensitive

### Parameter Change Breaks System

**If system breaks after parameter change:**

1. **Immediate Revert**
   - Change back to previous value
   - Save and reboot
   - Verify system works

2. **Identify Incompatible Settings**
   - Some parameters interact
   - Check documentation for dependencies
   - Example: Changing SERIAL protocol requires matching baud

3. **Reset Category**
   - Reset just related parameters
   - Don't reset everything if not needed

### Parameters Reset Unexpectedly

**Causes:**
- Firmware update
- Full chip erase
- EEPROM failure
- Manual reset command

**Prevention:**
- Backup parameters regularly
- Save to file before firmware updates
- Keep documentation of critical settings

**Recovery:**
- Restore from backup
- Reconfigure manually
- Use community-shared configs as reference

## Compilation/Build Issues

### Arduino/PlatformIO Won't Compile

**For students building custom firmware:**

**Common Errors:**

1. **Missing Libraries**
   ```
   Error: Library not found
   Solution:
   - Install required libraries
   - Check platformio.ini or library dependencies
   - Update library manager
   ```

2. **Version Mismatch**
   ```
   Error: Incompatible versions
   Solution:
   - Match Arduino IDE version to project requirements
   - Update board definitions
   - Check platform version
   ```

3. **Path Issues**
   ```
   Error: File not found
   Solution:
   - No spaces in project path
   - Use short paths on Windows
   - Check file permissions on Linux/Mac
   ```

4. **Board Selection**
   ```
   Error: Board not supported
   Solution:
   - Select correct board type
   - Install board definitions
   - Check processor speed setting
   ```

### Custom Code Won't Upload

**Debugging Steps:**

1. **Syntax Errors**
   - Read compiler error messages carefully
   - Line numbers indicate problem location
   - Common: missing semicolons, brackets

2. **Memory Overflow**
   ```
   Error: Sketch too big
   Solution:
   - Remove debug code
   - Optimize code size
   - Disable unused features
   - Use smaller libraries
   ```

3. **Upload Settings**
   - Correct COM port
   - Right bootloader for board
   - Proper upload speed
   - Try slower baud rate

## Ground Control Station Issues

### Mission Planner Problems

**Won't Start:**
- Install .NET Framework (required)
- Run as administrator
- Check antivirus isn't blocking
- Reinstall if corrupted

**Connection Issues:**
- Correct COM port and baud rate
- Click "Connect" button
- Check telemetry radio link
- Verify MAVLink protocol

**Mission Upload Fails:**
- Strong telemetry link required
- Upload near vehicle
- Check mission for errors
- Reduce mission size

### QGroundControl Issues

**Video Not Showing:**
- GStreamer installed (Windows)
- Correct video stream URL
- Network firewall allowing UDP
- Check video format compatibility

**Parameters Won't Load:**
- Wait for full download (slow)
- Strong connection required
- Retry if interrupted
- Check vehicle has parameters

**App Crashes:**
- Update to latest version
- Clear settings and restart
- Check system requirements
- Report bug with logs

## Protocol/Communication Issues

### PWM vs OneShot vs DShot

**Symptoms:**
- Motors don't respond
- Erratic motor behavior
- ESC won't configure

**Matching Protocol:**

| Setting | FC Output | ESC Configuration |
|---------|-----------|-------------------|
| PWM | Standard PWM | Standard/PWM mode |
| Oneshot125 | Oneshot125 | Oneshot mode |
| Oneshot42 | Oneshot42 | Oneshot mode |
| Multishot | Multishot | Multishot mode |
| DShot150/300/600 | DShot | BLHeli_32/BLHeli_S DShot |

**Configuration:**
1. Choose protocol (DShot recommended)
2. Configure in FC (motor protocol setting)
3. Configure ESC if needed (BLHeli configurator)
4. Reboot FC and ESCs
5. Test motor direction

### SBUS/PPM/IBUS Configuration

**Receiver Protocol Setup:**

**SBUS:**
```
FC Setting: SBUS
Physical: Single wire to SBUS/RX pad
Inverted: Most FCs handle automatically
Baud: 100000
```

**PPM:**
```
FC Setting: PPM
Physical: Single wire to PPM pad
Channels: Up to 8 typically
More universal but older
```

**IBUS:**
```
FC Setting: IBUS (or FLYSKY)
Physical: Single wire to RX pad
Baud: 115200
Used by FlySky receivers
```

**Troubleshooting:**
- Check wire on correct pad
- Verify protocol setting
- Test receiver with servo
- Check receiver binding

### MAVLink Communication Errors

**Common Issues:**

1. **Version Mismatch**
   ```
   Problem: MAVLink 1 vs MAVLink 2
   Solution: Set protocol to 2 on both ends
   Parameter: SERIALx_PROTOCOL = 2
   ```

2. **System ID Conflicts**
   ```
   Problem: Multiple vehicles same ID
   Solution: Set unique SYSID_THISMAV for each vehicle
   ```

3. **Baud Rate Mismatch**
   ```
   Common rates: 57600, 115200, 921600
   Must match on both FC and ground station
   ```

4. **Message Overload**
   ```
   Too many messages causing packet loss
   Reduce stream rates in GCS
   ArduPilot: SRx_* parameters
   ```

## Sensor Configuration Issues

### GPS Not Detected

**Configuration Checklist:**

```
ArduPilot:
[ ] GPS_TYPE set (1 = Auto, 2 = UBLOX, etc.)
[ ] SERIALx_PROTOCOL = 5 (GPS)
[ ] Correct UART selected
[ ] Baud rate correct (usually auto)
[ ] GPS module powered (3.3V or 5V)
[ ] TX->RX and RX->TX connected

Betaflight/INAV:
[ ] GPS UART configured in Ports tab
[ ] GPS protocol set (UBLOX, NMEA)
[ ] Auto-baud enabled or correct baud
```

### Compass Configuration

**Multiple Compass Priority:**

```
ArduPilot:
COMPASS_USE = 1 (first compass, usually internal)
COMPASS_USE2 = 1 (second compass, usually external)
COMPASS_USE3 = 0 (disable third if not present)

COMPASS_PRIMARY = 0 (auto) or specific compass
COMPASS_EXTERNAL = 1 (if using external GPS/compass)
```

**Orientation:**

```
COMPASS_ORIENT = 0 (if mounted standard)
If rotated, use appropriate rotation (0-42)
Test all orientations if unsure
```

### Barometer/Rangefinder

**Configuration:**

```
Barometer:
- Usually auto-detected
- Check BARO_OPTIONS if issues
- Ensure not physically blocked

Rangefinder:
RNGFND_TYPE = specific sensor type
RNGFND_ORIENT = 25 (downward facing)
RNGFND_MIN_CM = minimum range (10cm typical)
RNGFND_MAX_CM = maximum range (400cm for sonar, etc.)
```

## Calibration Issues

### Accelerometer Calibration Fails

**Requirements:**
- Completely level surface
- Vehicle stationary
- No vibration
- Complete all positions

**Common Problems:**

| Issue | Cause | Solution |
|-------|-------|----------|
| "Move to next position" doesn't advance | Position not detected | Ensure face is truly level/vertical |
| Calibration fails at end | Too much movement | Keep completely still |
| Values way off | Sensor damaged | Replace FC |
| Can't complete | Timeout | Start over, work faster |

### Compass Calibration Issues

**Proper Procedure:**
1. Outdoors, away from metal
2. Rotate 360° on all 3 axes
3. Complete full sphere pattern
4. Accept when sufficient samples collected

**Problems:**

- **Inconsistent/High Offsets**: Magnetic interference during calibration
  - Move further from metal
  - Turn off other electronics
  - Some vehicle components cause interference

- **Won't Complete**: Insufficient coverage
  - Need full 3D rotation
  - Some areas missed
  - Rotate more thoroughly

- **Fails Immediately After**: Compass moving relative to FC
  - Secure GPS/compass module
  - Don't use on metal table

### ESC Calibration

**Purpose:** Teach ESCs min/max throttle range

**Procedure:**
1. Disconnect battery
2. Props OFF
3. Raise throttle to maximum
4. Connect battery
5. ESCs beep
6. Lower throttle to minimum
7. ESCs beep confirmation
8. Done

**Problems:**
- **ESCs don't beep**: Wrong protocol (can't calibrate DShot)
- **Motors spin during**: Dangerous! Props must be OFF
- **Still wrong range**: Check protocol settings
- **Only some ESCs**: 4-in-1 ESCs don't need calibration

## Mode Configuration Issues

### Flight Modes Not Switching

**Betaflight/INAV:**
1. Check Modes tab
2. Assign mode to switch/channel
3. Move switch and verify colored bar moves
4. Set ranges for each position
5. Save

**ArduPilot:**
```
FLTMODEx parameters (x = 1-6)
FLTMODE_CH = 5 (typical, channel 5)

Example:
FLTMODE1 = 0 (Stabilize)
FLTMODE2 = 2 (AltHold)
FLTMODE3 = 3 (Auto)
```

**Common Issues:**
- Channel not mapped
- Switch not bound
- Ranges overlap
- Wrong channel selected

### Arming Switch Not Working

**Check:**
1. Arming configured on correct channel
2. Switch throws to required position
3. Pre-arm checks passing
4. Not in auto-disarm timeout
5. Correct arm/disarm sequence for FC

**Betaflight:**
- Arming disabled in CLI by default for safety
- Must enable explicitly
- Can use stick arming or switch

**ArduPilot:**
- ARMING_CHECK = 1 (all checks) or selective
- Some modes can't arm (check mode list)

## Feature-Specific Issues

### OSD Not Showing

**Check:**
1. OSD feature enabled
2. Video connection: Camera → FC → VTX
3. Correct video standard (NTSC/PAL)
4. Sufficient contrast on elements
5. FC OSD chip working

**Betaflight:**
- Configuration tab: OSD enabled
- OSD tab: Elements positioned
- Video system correct

### Blackbox Not Recording

**Requirements:**
- Flash chip on FC or SD card
- Blackbox feature enabled
- Sufficient logging rate configured
- Free space available

**Enable:**
```
Betaflight: Configuration tab → Blackbox device
ArduPilot: LOG_BACKEND_TYPE and LOG_BITMASK
```

### LED Strip Not Working

**Configuration:**
1. LED strip resource assigned
2. LED count set correctly
3. LED protocol matches (WS2812)
4. Wire on correct pad
5. Powered adequately (5V)

**Common:**
- First LED working but not others: Wire break
- No LEDs: Wrong protocol or no power
- Flickering: Insufficient power/voltage drop

## Software Update Issues

### Update Breaks System

**Prevention:**
1. Backup all settings
2. Read changelog
3. Note breaking changes
4. Test on bench before flying

**Recovery:**
1. Revert to previous version
2. Restore settings backup
3. Address issues one at a time
4. Consider staying on older stable version

### Lost Settings After Update

**Restoration:**
1. Load saved configuration file
2. Manually re-enter critical parameters
3. Recalibrate sensors
4. Test thoroughly

## Best Practices

### Configuration Management

**Do:**
- Save configurations regularly
- Name backups descriptively (date, version, notes)
- Document custom changes
- Test changes on bench first
- Keep firmware version notes

**Don't:**
- Restore old configs to new firmware blindly
- Change multiple things without testing
- Skip reading documentation
- Ignore warning messages

### Systematic Troubleshooting

1. **Document Baseline**
   - What was working configuration?
   - What changed recently?

2. **Change One Thing**
   - Isolate variable
   - Test immediately
   - Document result

3. **Verify Fix**
   - Don't assume
   - Test thoroughly
   - Check for side effects

4. **Share Solution**
   - Help community
   - Document for yourself
   - Contribute to docs

## Getting Help

### Information to Provide

When asking for help with software issues:

1. **System Info**
   - FC model and processor
   - Firmware type and version
   - Configurator version
   - Operating system

2. **Problem Description**
   - Specific error messages
   - When it occurs
   - What you've tried

3. **Screenshots**
   - Configuration screens
   - Error messages
   - Parameter settings

4. **Files**
   - Configuration dump (CLI)
   - Blackbox/dataflash log
   - Parameter list

## Next Steps

- [Hardware Issues](hardware-issues.md) - Physical problems
- [Flight Operation Issues](flight-operation-issues.md) - Flying problems
- [Log Analysis](log-analysis.md) - Understanding logs
- [Diagnostic Flowcharts](diagnostic-flowcharts.md) - Visual guides
