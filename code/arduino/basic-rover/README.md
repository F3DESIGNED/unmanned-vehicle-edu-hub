# Basic Autonomous Rover - Obstacle Avoidance

A simple autonomous rover that drives forward and avoids obstacles using an ultrasonic sensor.

## Hardware Requirements

### Essential Components
- **Arduino Uno or Nano** (1×)
- **L298N Motor Driver** or equivalent H-bridge (1×)
- **DC Gear Motors** 6V with wheels (2×)
- **HC-SR04 Ultrasonic Sensor** (1×)
- **Battery Pack**: 2S LiPo (7.4V) or 6× AA batteries
- **Chassis**: Robot chassis kit or DIY platform
- **Jumper Wires** and **Breadboard** (for prototyping)

### Optional Components
- LED indicators (for status)
- Switch (for easy power control)
- Voltage regulator (if using higher voltage battery)

## Wiring Diagram

```
Arduino          Motor Driver (L298N)
-------          -------------------
Pin 5    →       IN1 (Left Motor +)
Pin 6    →       IN2 (Left Motor -)
Pin 9    →       IN3 (Right Motor +)
Pin 10   →       IN4 (Right Motor -)
Pin 3    →       ENA (Left Enable/Speed)
Pin 11   →       ENB (Right Enable/Speed)

Arduino          Ultrasonic Sensor (HC-SR04)
-------          --------------------------
Pin 12   →       TRIG
Pin 13   →       ECHO
5V       →       VCC
GND      →       GND

Power Connections:
- Battery + → Motor Driver +12V (or appropriate voltage input)
- Battery - → Motor Driver GND AND Arduino GND (common ground!)
- Motor Driver +5V → Arduino VIN (if not USB powered)
- Motors → Motor Driver OUT1/OUT2 (left) and OUT3/OUT4 (right)
```

## Installation

### 1. Arduino IDE Setup
1. Download and install [Arduino IDE](https://www.arduino.cc/en/software)
2. Connect Arduino via USB
3. Select **Tools → Board → Arduino Uno** (or your board)
4. Select **Tools → Port → COM# (Your Arduino)**

### 2. Upload Code
1. Open `basic_rover.ino` in Arduino IDE
2. Click **Verify** (checkmark icon) to compile
3. Click **Upload** (arrow icon) to flash to Arduino
4. Open **Serial Monitor** (magnifying glass icon) at 9600 baud

### 3. Assembly
1. Mount motors to chassis
2. Connect motor driver to motors and Arduino (follow wiring diagram)
3. Mount ultrasonic sensor on front of chassis (clear view forward)
4. Secure Arduino and motor driver to chassis
5. Connect battery (ensure proper polarity!)

## Usage

### Safety First!
1. **Test with wheels off ground** (on blocks)
2. **Ensure adequate space** for movement (2m × 2m minimum)
3. **Keep emergency stop ready** (power switch or unplug battery)

### First Test
1. Place rover on blocks (wheels off ground)
2. Power on
3. Verify motors spin correctly (check serial monitor output)
4. Place hand in front of sensor (<20cm)
5. Verify motors stop and reverse

### Autonomous Operation
1. Ensure open area with obstacles (boxes, books, etc.)
2. Place rover on ground
3. Power on (3 second startup delay)
4. Rover will drive forward until obstacle detected
5. Rover backs up, turns, and continues

### Troubleshooting

**Rover doesn't move**:
- Check battery voltage (should be >6V under load)
- Verify motor driver connections
- Check motor driver enable jumpers (ENA/ENB)

**Motors spin wrong direction**:
- Swap IN1↔IN2 for left motor or IN3↔IN4 for right motor in code
- OR physically swap motor wires

**Doesn't detect obstacles**:
- Verify ultrasonic sensor wiring
- Check serial monitor for distance readings
- Ensure sensor faces forward with clear view

**Rover gets stuck in corners**:
- Increase TURN_TIME constant (more rotation)
- Improve random turn selection logic

## Customization

### Adjust Behavior
Edit constants in code:

```cpp
const int OBSTACLE_DISTANCE_CM = 20;  // Detection distance (cm)
const int BASE_SPEED = 150;           // Forward speed (0-255)
const int TURN_SPEED = 180;           // Turn speed
const int BACKUP_TIME = 800;          // Backup duration (ms)
const int TURN_TIME = 600;            // Turn duration (ms)
```

### Add Features
- **Multiple Sensors**: Add left/right ultrasonic sensors
- **Speed Control**: Add potentiometer for speed adjustment
- **LED Indicators**: Show status (forward=green, avoiding=red)
- **Line Following**: Add IR sensors underneath

## Learning Activities

### Beginner Experiments
1. **Tune Parameters**: Adjust speeds and times, observe behavior
2. **Measure Performance**: Count obstacles avoided in 5 minutes
3. **Distance Calibration**: Verify ultrasonic accuracy with ruler

### Intermediate Projects
4. **Smart Turning**: Turn toward more open space (add side sensors)
5. **Escape Routine**: Detect if stuck, execute special maneuver
6. **Speed Adaptation**: Slow down near obstacles, speed up in open space

### Advanced Challenges
7. **Maze Solving**: Implement wall-following algorithm
8. **Mapping**: Log positions and obstacles (requires encoders or GPS)
9. **Multi-Sensor Fusion**: Combine ultrasonic, IR, and bump sensors

## Code Explanation

### Main Loop Logic
```
1. Measure distance to obstacle
2. IF obstacle within 20cm:
     a. Stop
     b. Back up
     c. Turn (random direction)
3. ELSE:
     Drive forward
4. Repeat
```

### Key Functions
- `measureDistance()`: Uses ultrasonic sensor via pulseIn()
- `driveForward/Backward()`: Sets motor directions and speeds
- `turnLeft/Right()`: Differential drive (opposite motor directions)
- `stopMotors()`: Stops all motors safely

## Safety Notes

⚠️ **Important Safety Considerations**:
- Never touch rotating parts while powered
- Ensure battery cannot short circuit
- Supervise autonomous operation at all times
- Test in safe, contained environment first
- Use appropriate battery type (LiPo requires special care)

## Resources

### Hardware Suppliers
- **Arduino**: Official Arduino store, Amazon, Adafruit, SparkFun
- **Motors & Chassis**: Pololu, ServoCity, AliExpress
- **Sensors**: Adafruit, SparkFun, Amazon

### Further Learning
- [Arduino Reference](https://www.arduino.cc/reference/en/)
- [Motor Control Basics](https://learn.adafruit.com/adafruit-arduino-lesson-15-dc-motor-reversing)
- [Ultrasonic Sensor Tutorial](https://randomnerdtutorials.com/complete-guide-for-ultrasonic-sensor-hc-sr04/)

### Related Projects
- Line Follower (coming soon)
- GPS Navigator
- Bluetooth Remote Control

## License

MIT License - Free to use and modify for educational purposes.

## Support

Questions or issues? Open an issue on our [GitHub repository](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub).

---

**Back to**: [Arduino Programming Guide](../../../docs/programming/arduino-programming/) | [Code Examples](../)
