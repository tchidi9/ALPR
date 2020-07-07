import RPi.GPIO as GPIO
import time
import signal
import sys
import TrafficLight as Light
import Capture
import API as Remote
import Buzzer
import IntrutionDetection as Detect
import IntrutionIdentification as Identify
import Location as Pos
import API
import cv2 as vCapture

# replace with /etc/lightsApp/
SAVE_PATH = "/home/pi/Desktop/"

# capture time
CAPTURE_TIME = 20

# display video in screen
DISPLAY_VIDEO = False

# pin points on raspberry pi
Detect.DT =13
Detect.SCK=11
#Detect.DT =27
#Detect.SCK=17

HIGH=1
LOW =0

m1=12
m2=16

Detect.intruderDetected = True

sample=0
val=0

#time.sleep(3)
#sample= readCount()
#flag=0
#status = True


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    Light.setup()
    Detect.setup()

# Initialize Raspberry Pi board
#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
#Light.setup()
#Detect.setup()

setup()
# Initialize traffic light
Light.start()


while(1):
    if GPIO.input(Light.LEDPin_Red) == True:
	Detect.start(True)
	if(Detect.intruderDetected):
		Detect.status = False
		# capture video and save to remote path
		fileName = Capture.video(self, CAPTURE_TIME, SAVE_PATH, DISPLAY_VIDEO)

		# alarm buzzer
		Buzzer.On()

		# capture location of intrution and send SMS
		location = Pos.getLocationDateTime()

		# split video to picture frames
		capture = videoCapture.VideoCapture(fileName)
		success,image = capture.read()
		count = 0
		success = True
		while success:
		  videoCapture.imwrite("%s_Cam1_%s.jpg" % (SAVE_PATH, (__date__)), image)     # save frame as JPEG file
		  success,image = capture.read()
		  count += 1
		# for all pictures in video frames (fps), analyse to get plate numbers

		# get violator's plate number
		plateNo = API.getPlateNo()
		delay(2)

		# get location date and time info
		longLat = Pos.getLocationDateTime()
		delay(2)

		# post result to selected API
		API.post(plateNo, pictureURL, videoURL, longLat)
		delay(5)
    else:
	delay(5)
	Buzzer.Off()
