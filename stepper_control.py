# stepper_control.py
"""Moves the Stepper motor to the desired degree out of 360
usage is either by itself via command line or via import
you choose the axis to move it and then the degrees either direction eg 
example: 
move_to_position("x", 180)
moves x 180 degrees right or if was -180 it would move left
or
move_to_position("y", 360)"""
import RPi.GPIO as GPIO
import time
import sys

FAST = 0.00075
MEDIUM = 0.002
SLOW = 0.001

SELECTED_SPEED = MEDIUM


def move_to_position(axis, target_angle):
    target_angle = float(target_angle)
    print("Moving to position: " + str(target_angle) + " degrees")
    if axis == 'x':
        # Pins on GPIO
        in1 = 17
        in2 = 18
        in3 = 27
        in4 = 22
    elif axis == "y":
        in1 = 5
        in2 = 6
        in3 = 13
        in4 = 19

    # Careful lowering this; at some point, you run into the mechanical limitation of how quickly your motor can move
    step_sleep = SELECTED_SPEED

    # Steps per revolution with 1/64 microstepping
    steps_per_revolution = 64 * 64

    # Calculate the number of steps needed to reach the target position
    target_steps = int((target_angle / 360) * steps_per_revolution)

    # Direction: True for clockwise, False for counter-clockwise
    direction = target_steps > 0

    # Ensure the direction is correct
    target_steps = abs(target_steps)

    # Defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
    step_sequence = [
        [1, 0, 0, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1]
    ]

    # Setting up GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)

    # Initializing GPIO
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

    motor_pins = [in1, in2, in3, in4]
    motor_step_counter = 0

    def cleanup():
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        GPIO.cleanup()

    # The main part
    try:
        for _ in range(target_steps):
            for pin in range(len(motor_pins)):
                GPIO.output(motor_pins[pin],
                            step_sequence[motor_step_counter][pin])

            if direction:
                motor_step_counter = (motor_step_counter - 1) % 8
            else:
                motor_step_counter = (motor_step_counter + 1) % 8

            time.sleep(step_sleep)

    except KeyboardInterrupt:
        cleanup()
#        exit(1)

    cleanup()
 #   exit(0)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_angle = float(sys.argv[2])
        axis = sys.argv[1]
        move_to_position(axis, target_angle)
    else:
        print("Usage: python stepper_control.py <target_angle>")
