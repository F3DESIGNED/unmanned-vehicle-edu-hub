# GPIO Motor Control - Raspberry Pi

Basic motor control example demonstrating PWM speed control and directional control of DC motors using Raspberry Pi GPIO.

## Hardware Requirements

- Raspberry Pi (any model with 40-pin GPIO)
- L298N Motor Driver or equivalent
- 2× DC gear motors (6-12V)
- External battery (6-12V, 2A+ capacity)
- Jumper wires
- Robot chassis (optional but recommended)

## Installation

### 1. Enable GPIO (if needed)
```bash
# Update system
sudo apt update && sudo apt upgrade

# Install RPi.GPIO library (usually pre-installed)
sudo apt install python3-rpi.gpio
```

### 2. Clone or Download Code
```bash
git clone https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub.git
cd unmanned-vehicle-edu-hub/code/raspberry-pi/python-examples/gpio-motor-control/
```

### 3. Test Installation
```bash
python3 motor_control.py
```

## Wiring Diagram

```
Motor Driver (L298N)    Raspberry Pi GPIO
--------------------    -----------------
IN1                 →   GPIO 17 (Pin 11)
IN2                 →   GPIO 18 (Pin 12)
IN3                 →   GPIO 22 (Pin 15)
IN4                 →   GPIO 23 (Pin 16)
ENA                 →   GPIO 12 (Pin 32)
ENB                 →   GPIO 13 (Pin 33)
GND                 →   GND (Pin 6, 9, 14, 20, 25, 30, 34, 39)

Power:
External Battery + → Motor Driver +12V input
External Battery - → Motor Driver GND AND Pi GND (CRITICAL: common ground!)
Motors → Motor Driver OUT1/OUT2 (left), OUT3/OUT4 (right)

IMPORTANT: Do NOT power motors from Pi GPIO! Use external battery for motors.
```

## Usage

### Basic Test Sequence
```bash
python3 motor_control.py
```

This runs a test sequence:
1. Forward for 2 seconds
2. Stop for 1 second
3. Backward for 2 seconds
4. Stop for 1 second
5. Turn left for 1.5 seconds
6. Stop for 1 second
7. Turn right for 1.5 seconds
8. Stop

### Use in Your Own Code

```python
from motor_control import MotorController
import time

# Initialize controller
motors = MotorController()

try:
    # Drive forward at 60% speed
    motors.forward(speed=60)
    time.sleep(3)

    # Turn right
    motors.turn_right(speed=50)
    time.sleep(1)

    # Stop
    motors.stop()

finally:
    # Always cleanup
    motors.cleanup()
```

## API Reference

### MotorController Class

#### `__init__()`
Initializes GPIO pins and PWM.

#### `forward(speed=50)`
Drive forward.
- **speed**: Integer 0-100 (percentage)

#### `backward(speed=50)`
Drive backward.
- **speed**: Integer 0-100 (percentage)

#### `turn_left(speed=50)`
Turn left (left motors reverse, right forward).
- **speed**: Integer 0-100 (percentage)

#### `turn_right(speed=50)`
Turn right (left motors forward, right reverse).
- **speed**: Integer 0-100 (percentage)

#### `stop()`
Stop all motors.

#### `cleanup()`
Clean up GPIO resources. Always call when done!

## Troubleshooting

### Motors Don't Spin
- **Check battery voltage**: Should be 6-12V with sufficient current (2A+)
- **Verify wiring**: Ensure all connections secure, check continuity
- **Common ground**: Pi GND MUST connect to motor driver GND
- **Enable jumpers**: Some L298N boards require jumpers on ENA/ENB

### Motors Spin Wrong Direction
Swap the two wires going to that motor OR swap IN1↔IN2 (left) or IN3↔IN4 (right) in code:
```python
LEFT_MOTOR_FORWARD = 18  # Swapped
LEFT_MOTOR_REVERSE = 17  # Swapped
```

### Permission Denied Error
```bash
# Run with sudo (or add user to gpio group)
sudo python3 motor_control.py

# OR add user to gpio group (permanent, requires logout/login)
sudo usermod -a -G gpio $USER
```

### PWM Not Working
- Ensure using hardware PWM pins (GPIO 12, 13, 18, 19)
- Check `/boot/config.txt` for `dtoverlay=pwm` if issues persist

## Safety Notes

⚠️ **Critical Safety Points**:
1. **Common Ground**: Always connect Pi GND to motor driver GND
2. **Separate Power**: NEVER power motors from Pi's 5V/3.3V pins
3. **Test Safely**: Run first test with motors on blocks (wheels off ground)
4. **Battery Safety**: Use appropriate battery type, follow charging guidelines
5. **Supervision**: Never leave running unattended

## Learning Activities

### Beginner
1. Change speeds, observe motor behavior
2. Create square pattern (forward, turn, repeat)
3. Add time delays for smooth acceleration/deceleration

### Intermediate
4. Add ultrasonic sensor for obstacle avoidance
5. Implement keyboard control (arrow keys)
6. Create figure-8 pattern

### Advanced
7. Add encoders, implement PID speed control
8. GPS integration for waypoint navigation
9. Computer vision object tracking

## Dependencies

- `RPi.GPIO`: GPIO control library
- Python 3.6+

Install dependencies:
```bash
pip3 install RPi.GPIO
```

## Related Examples

- Ultrasonic Obstacle Avoidance (coming soon)
- GPS Waypoint Navigation
- OpenCV Object Tracking

## License

MIT License - Free to use and modify.

## Support

Issues? Questions? Open an issue on [GitHub](https://github.com/F3DESIGNED/unmanned-vehicle-edu-hub/issues).

---

**Back to**: [Raspberry Pi Programming](../../../../docs/programming/raspberry-pi-programming/) | [Python Examples](../)
