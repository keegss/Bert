import RPi.GPIO as GPIO
import sys, tty, termios, time

print("do we get in")

mode = GPIO.getmode()

# define GPIO pins
motor1_p = 37
motor1_n = 38
motor2_p = 35
motor2_n = 36

# GPIO write setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1_p, GPIO.OUT)
GPIO.setup(motor1_n, GPIO.OUT)
GPIO.setup(motor2_p, GPIO.OUT)
GPIO.setup(motor2_n, GPIO.OUT)

# determine which key was pressed by the user
def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

#GPIO functions
def forward():
	GPIO.output(motor1_p, GPIO.HIGH)
	GPIO.output(motor2_p, GPIO.HIGH)
	GPIO.output(motor1_n, GPIO.LOW)
	GPIO.output(motor2_n, GPIO.LOW)

def reverse():
	GPIO.output(motor1_p, GPIO.LOW)
	GPIO.output(motor2_p, GPIO.LOW)
	GPIO.output(motor1_n, GPIO.HIGH)
	GPIO.output(motor2_n, GPIO.HIGH)


def left():
	GPIO.output(motor1_p, GPIO.LOW)
	GPIO.output(motor2_p, GPIO.HIGH)
	GPIO.output(motor1_n, GPIO.LOW)
	GPIO.output(motor2_n, GPIO.LOW)

def right():
	GPIO.output(motor1_p, GPIO.HIGH)
	GPIO.output(motor2_p, GPIO.LOW)
	GPIO.output(motor1_n, GPIO.LOW)
	GPIO.output(motor2_n, GPIO.LOW)

def stop():
	GPIO.output(motor1_p, GPIO.LOW)
	GPIO.output(motor2_p, GPIO.LOW)
	GPIO.output(motor1_n, GPIO.LOW)
	GPIO.output(motor2_n, GPIO.LOW)


GPIO.output(motor1_p, False)
GPIO.output(motor1_n, False)
GPIO.output(motor2_p, False)
GPIO.output(motor2_n, False)

print("Use the following keys to control the robot: ")
print("W: Forward S: Reverse")
print("A: Left D: Right")
print("Q: Exit program")

while True:
    char = getch()

    if(char == "w"):
        forward()
    if(char == "s"):
        reverse()
    if(char == "a"):
        left()
    if(char == "d"):
        right()
    if(char == "q"):
        print("Exiting...")
        break

    char = ""

GPIO.cleanup()
