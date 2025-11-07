/*
 * Basic Autonomous Rover with Obstacle Avoidance
 *
 * Hardware:
 *  - Arduino Uno/Nano
 *  - L298N Motor Driver or similar
 *  - 2x DC Motors (left and right)
 *  - HC-SR04 Ultrasonic Sensor
 *  - 2S LiPo or 6x AA battery pack
 *
 * Wiring:
 *  Motor Driver:
 *    - IN1 → Pin 5 (Left Motor Forward)
 *    - IN2 → Pin 6 (Left Motor Reverse)
 *    - IN3 → Pin 9 (Right Motor Forward)
 *    - IN4 → Pin 10 (Right Motor Reverse)
 *    - ENA → Pin 3 (Left Motor Speed PWM)
 *    - ENB → Pin 11 (Right Motor Speed PWM)
 *
 *  Ultrasonic Sensor:
 *    - TRIG → Pin 12
 *    - ECHO → Pin 13
 *    - VCC → 5V
 *    - GND → GND
 *
 * Behavior:
 *  - Drive forward
 *  - If obstacle detected within 20cm, back up and turn
 *  - Resume forward motion
 *
 * Safety:
 *  - Test on blocks first (wheels off ground)
 *  - Ensure adequate space for movement
 *  - Have emergency stop ready (unplug power)
 *
 * Author: Unmanned Vehicle Edu Hub
 * License: MIT
 */

// Motor Driver Pin Definitions
#define LEFT_MOTOR_FORWARD   5    // IN1
#define LEFT_MOTOR_REVERSE   6    // IN2
#define RIGHT_MOTOR_FORWARD  9    // IN3
#define RIGHT_MOTOR_REVERSE  10   // IN4
#define LEFT_MOTOR_SPEED     3    // ENA (PWM)
#define RIGHT_MOTOR_SPEED    11   // ENB (PWM)

// Ultrasonic Sensor Pins
#define TRIG_PIN 12
#define ECHO_PIN 13

// Constants
const int OBSTACLE_DISTANCE_CM = 20;  // Stop if obstacle within 20cm
const int BASE_SPEED = 150;           // Motor speed (0-255)
const int TURN_SPEED = 180;           // Speed during turns (slightly faster)
const int BACKUP_TIME = 800;          // Milliseconds to back up
const int TURN_TIME = 600;            // Milliseconds to turn

// Function prototypes
void setup();
void loop();
void stopMotors();
void driveForward(int speed);
void driveBackward(int speed);
void turnLeft(int speed);
void turnRight(int speed);
long measureDistance();

void setup() {
  // Initialize Serial for debugging
  Serial.begin(9600);
  Serial.println("Basic Rover Starting...");

  // Configure motor pins as outputs
  pinMode(LEFT_MOTOR_FORWARD, OUTPUT);
  pinMode(LEFT_MOTOR_REVERSE, OUTPUT);
  pinMode(RIGHT_MOTOR_FORWARD, OUTPUT);
  pinMode(RIGHT_MOTOR_REVERSE, OUTPUT);
  pinMode(LEFT_MOTOR_SPEED, OUTPUT);
  pinMode(RIGHT_MOTOR_SPEED, OUTPUT);

  // Configure ultrasonic sensor pins
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  // Ensure motors start stopped
  stopMotors();

  // Startup delay (allows time to place rover)
  Serial.println("Starting in 3 seconds...");
  delay(3000);
  Serial.println("GO!");
}

void loop() {
  // Measure distance to obstacle
  long distance = measureDistance();

  // Debug output
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Decision logic
  if (distance < OBSTACLE_DISTANCE_CM && distance > 0) {
    // Obstacle detected!
    Serial.println("Obstacle detected! Avoiding...");

    // Stop
    stopMotors();
    delay(300);

    // Back up
    Serial.println("Backing up...");
    driveBackward(BASE_SPEED);
    delay(BACKUP_TIME);

    // Stop
    stopMotors();
    delay(200);

    // Turn (randomly left or right for variety)
    if (random(0, 2) == 0) {
      Serial.println("Turning left...");
      turnLeft(TURN_SPEED);
    } else {
      Serial.println("Turning right...");
      turnRight(TURN_SPEED);
    }
    delay(TURN_TIME);

    // Stop after turn
    stopMotors();
    delay(200);

  } else {
    // Path is clear, drive forward
    Serial.println("Path clear, driving forward...");
    driveForward(BASE_SPEED);
  }

  // Small delay to avoid overwhelming sensor
  delay(100);
}

/**
 * Stop all motors
 */
void stopMotors() {
  digitalWrite(LEFT_MOTOR_FORWARD, LOW);
  digitalWrite(LEFT_MOTOR_REVERSE, LOW);
  digitalWrite(RIGHT_MOTOR_FORWARD, LOW);
  digitalWrite(RIGHT_MOTOR_REVERSE, LOW);
  analogWrite(LEFT_MOTOR_SPEED, 0);
  analogWrite(RIGHT_MOTOR_SPEED, 0);
}

/**
 * Drive forward at specified speed
 * @param speed Motor speed (0-255)
 */
void driveForward(int speed) {
  digitalWrite(LEFT_MOTOR_FORWARD, HIGH);
  digitalWrite(LEFT_MOTOR_REVERSE, LOW);
  digitalWrite(RIGHT_MOTOR_FORWARD, HIGH);
  digitalWrite(RIGHT_MOTOR_REVERSE, LOW);
  analogWrite(LEFT_MOTOR_SPEED, speed);
  analogWrite(RIGHT_MOTOR_SPEED, speed);
}

/**
 * Drive backward at specified speed
 * @param speed Motor speed (0-255)
 */
void driveBackward(int speed) {
  digitalWrite(LEFT_MOTOR_FORWARD, LOW);
  digitalWrite(LEFT_MOTOR_REVERSE, HIGH);
  digitalWrite(RIGHT_MOTOR_FORWARD, LOW);
  digitalWrite(RIGHT_MOTOR_REVERSE, HIGH);
  analogWrite(LEFT_MOTOR_SPEED, speed);
  analogWrite(RIGHT_MOTOR_SPEED, speed);
}

/**
 * Turn left (left motor reverse, right motor forward)
 * @param speed Motor speed (0-255)
 */
void turnLeft(int speed) {
  digitalWrite(LEFT_MOTOR_FORWARD, LOW);
  digitalWrite(LEFT_MOTOR_REVERSE, HIGH);
  digitalWrite(RIGHT_MOTOR_FORWARD, HIGH);
  digitalWrite(RIGHT_MOTOR_REVERSE, LOW);
  analogWrite(LEFT_MOTOR_SPEED, speed);
  analogWrite(RIGHT_MOTOR_SPEED, speed);
}

/**
 * Turn right (left motor forward, right motor reverse)
 * @param speed Motor speed (0-255)
 */
void turnRight(int speed) {
  digitalWrite(LEFT_MOTOR_FORWARD, HIGH);
  digitalWrite(LEFT_MOTOR_REVERSE, LOW);
  digitalWrite(RIGHT_MOTOR_FORWARD, LOW);
  digitalWrite(RIGHT_MOTOR_REVERSE, HIGH);
  analogWrite(LEFT_MOTOR_SPEED, speed);
  analogWrite(RIGHT_MOTOR_SPEED, speed);
}

/**
 * Measure distance using ultrasonic sensor
 * @return Distance in centimeters (0 if out of range or error)
 */
long measureDistance() {
  // Send ultrasonic pulse
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Measure echo pulse duration
  long duration = pulseIn(ECHO_PIN, HIGH, 30000);  // Timeout after 30ms

  // Calculate distance (speed of sound = 343 m/s = 0.0343 cm/µs)
  // Distance = (duration / 2) * 0.0343
  long distance = duration * 0.0343 / 2;

  // Validate range (HC-SR04 range: 2cm - 400cm)
  if (distance < 2 || distance > 400) {
    return 0;  // Out of range or error
  }

  return distance;
}
