#!/usr/bin/env python3
"""
Basic Motor Control with Raspberry Pi GPIO

Hardware:
 - Raspberry Pi (any model with GPIO)
 - L298N Motor Driver or similar
 - 2x DC Motors
 - External battery (6-12V for motors)

Wiring:
 Motor Driver → Raspberry Pi
 IN1 → GPIO 17 (Pin 11)
 IN2 → GPIO 18 (Pin 12)
 IN3 → GPIO 22 (Pin 15)
 IN4 → GPIO 23 (Pin 16)
 ENA → GPIO 12 (Pin 32, PWM)
 ENB → GPIO 13 (Pin 33, PWM)

Safety:
 - Common ground between Pi and motor driver
 - DO NOT power motors from Pi GPIO (use external battery)
 - Test with motors on blocks first

Author: Unmanned Vehicle Edu Hub
License: MIT
"""

import RPi.GPIO as GPIO
import time

# Pin definitions
LEFT_MOTOR_FORWARD = 17  # IN1
LEFT_MOTOR_REVERSE = 18  # IN2
RIGHT_MOTOR_FORWARD = 22  # IN3
RIGHT_MOTOR_REVERSE = 23  # IN4
LEFT_MOTOR_SPEED = 12  # ENA (PWM)
RIGHT_MOTOR_SPEED = 13  # ENB (PWM)

# PWM Frequency (Hz)
PWM_FREQ = 1000


class MotorController:
    """Controls two DC motors via L298N H-bridge"""

    def __init__(self):
        """Initialize GPIO pins and PWM"""
        # Set GPIO mode (BCM numbering)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Configure pins as outputs
        GPIO.setup(LEFT_MOTOR_FORWARD, GPIO.OUT)
        GPIO.setup(LEFT_MOTOR_REVERSE, GPIO.OUT)
        GPIO.setup(RIGHT_MOTOR_FORWARD, GPIO.OUT)
        GPIO.setup(RIGHT_MOTOR_REVERSE, GPIO.OUT)
        GPIO.setup(LEFT_MOTOR_SPEED, GPIO.OUT)
        GPIO.setup(RIGHT_MOTOR_SPEED, GPIO.OUT)

        # Setup PWM for speed control
        self.left_pwm = GPIO.PWM(LEFT_MOTOR_SPEED, PWM_FREQ)
        self.right_pwm = GPIO.PWM(RIGHT_MOTOR_SPEED, PWM_FREQ)

        # Start PWM with 0% duty cycle (stopped)
        self.left_pwm.start(0)
        self.right_pwm.start(0)

        print("Motor Controller Initialized")

    def stop(self):
        """Stop both motors"""
        GPIO.output(LEFT_MOTOR_FORWARD, GPIO.LOW)
        GPIO.output(LEFT_MOTOR_REVERSE, GPIO.LOW)
        GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.LOW)
        GPIO.output(RIGHT_MOTOR_REVERSE, GPIO.LOW)
        self.left_pwm.ChangeDutyCycle(0)
        self.right_pwm.ChangeDutyCycle(0)
        print("Motors stopped")

    def forward(self, speed=50):
        """
        Drive forward
        Args:
            speed: Speed percentage (0-100)
        """
        speed = max(0, min(100, speed))  # Clamp to 0-100
        GPIO.output(LEFT_MOTOR_FORWARD, GPIO.HIGH)
        GPIO.output(LEFT_MOTOR_REVERSE, GPIO.LOW)
        GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.HIGH)
        GPIO.output(RIGHT_MOTOR_REVERSE, GPIO.LOW)
        self.left_pwm.ChangeDutyCycle(speed)
        self.right_pwm.ChangeDutyCycle(speed)
        print(f"Driving forward at {speed}% speed")

    def backward(self, speed=50):
        """
        Drive backward
        Args:
            speed: Speed percentage (0-100)
        """
        speed = max(0, min(100, speed))
        GPIO.output(LEFT_MOTOR_FORWARD, GPIO.LOW)
        GPIO.output(LEFT_MOTOR_REVERSE, GPIO.HIGH)
        GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.LOW)
        GPIO.output(RIGHT_MOTOR_REVERSE, GPIO.HIGH)
        self.left_pwm.ChangeDutyCycle(speed)
        self.right_pwm.ChangeDutyCycle(speed)
        print(f"Driving backward at {speed}% speed")

    def turn_left(self, speed=50):
        """
        Turn left (left reverse, right forward)
        Args:
            speed: Speed percentage (0-100)
        """
        speed = max(0, min(100, speed))
        GPIO.output(LEFT_MOTOR_FORWARD, GPIO.LOW)
        GPIO.output(LEFT_MOTOR_REVERSE, GPIO.HIGH)
        GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.HIGH)
        GPIO.output(RIGHT_MOTOR_REVERSE, GPIO.LOW)
        self.left_pwm.ChangeDutyCycle(speed)
        self.right_pwm.ChangeDutyCycle(speed)
        print(f"Turning left at {speed}% speed")

    def turn_right(self, speed=50):
        """
        Turn right (left forward, right reverse)
        Args:
            speed: Speed percentage (0-100)
        """
        speed = max(0, min(100, speed))
        GPIO.output(LEFT_MOTOR_FORWARD, GPIO.HIGH)
        GPIO.output(LEFT_MOTOR_REVERSE, GPIO.LOW)
        GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.LOW)
        GPIO.output(RIGHT_MOTOR_REVERSE, GPIO.HIGH)
        self.left_pwm.ChangeDutyCycle(speed)
        self.right_pwm.ChangeDutyCycle(speed)
        print(f"Turning right at {speed}% speed")

    def cleanup(self):
        """Clean up GPIO resources"""
        self.stop()
        self.left_pwm.stop()
        self.right_pwm.stop()
        GPIO.cleanup()
        print("GPIO cleaned up")


def test_sequence():
    """Test motor controller with basic sequence"""
    motors = MotorController()

    try:
        print("\n=== Motor Test Sequence ===")
        print("Ensure motors are on blocks (wheels off ground)!\n")
        input("Press Enter to start test...")

        # Forward
        motors.forward(speed=40)
        time.sleep(2)
        motors.stop()
        time.sleep(1)

        # Backward
        motors.backward(speed=40)
        time.sleep(2)
        motors.stop()
        time.sleep(1)

        # Turn left
        motors.turn_left(speed=50)
        time.sleep(1.5)
        motors.stop()
        time.sleep(1)

        # Turn right
        motors.turn_right(speed=50)
        time.sleep(1.5)
        motors.stop()

        print("\nTest complete!")

    except KeyboardInterrupt:
        print("\nTest interrupted")

    finally:
        motors.cleanup()


if __name__ == "__main__":
    print(__doc__)
    test_sequence()
