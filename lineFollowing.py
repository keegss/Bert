import numpy as np
import wiringpi as wp
import cv2
import RPi.GPIO as GPIO
import sys
import time

# gpio setup

mode = GPIO.getmode()

flag = 1;
f1 = 37
b1 = 38
f2 = 35
b2 = 36

GPIO.setmode(GPIO.BOARD)
GPIO.setup(f1, GPIO.OUT)
GPIO.setup(b1, GPIO.OUT)
GPIO.setup(f2, GPIO.OUT)
GPIO.setup(b2, GPIO.OUT)

#GPIO functions
def forward():
	GPIO.output(f1, GPIO.HIGH)
	GPIO.output(f2, GPIO.HIGH)

def left():
	GPIO.output(f1, GPIO.HIGH)
	GPIO.output(f2, GPIO.LOW)

def right():
	GPIO.output(f1, GPIO.LOW)
	GPIO.output(f2, GPIO.HIGH)

def stop():
	GPIO.output(f1, GPIO.LOW)
	GPIO.output(f2, GPIO.LOW)

video_capture = cv2.VideoCapture(-1)
video_capture.set(3, 160)
video_capture.set(4, 120)

while(True):

    # Capture the frames
    ret, frame = video_capture.read()

    # Crop the image
    crop_img = frame[60:120, 0:160]

    # Convert to grayscale
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    # Gaussian blur
    blur = cv2.GaussianBlur(gray,(5,5),0)

    # Color thresholding
    ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)

    # Find the contours of the frame
    contours, hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

    # Find the biggest contour (if detected)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)

        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),1)
        cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)

        if cx >= 120:
          left()

        if cx < 120 and cx > 50:
          forward()

        if cx <= 50:
          right()
 
    else:
      left()


 
