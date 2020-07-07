import RPi.GPIO as GPIO
import time
import signal
import sys


import RPi.GPIO as GPIO
import time

LEDPin_Red   = 19    # set pin  9 as red   led pin on Raspberry Pi
LEDPin_Amber = 21    # set pin 10 as amber led pin on Raspberry Pi
LEDPin_Green = 23    # set pin 11 as green led pin on Raspberry Pi

ledPins = [LEDPin_Red, LEDPin_Amber, LEDPin_Green]

TrafficOnTime   = 55		# Green LED On for 1 minute
TrafficReadyTime= 5		# Time (5s) between switching the LEDs from one to another
TrafficOffTime	= 25		# RED Led On for 30 seconds

# Setup
def setup():
        #GPIO.setmode(GPIO.BCM)			# Numbers GPIOs by physical location
        #GPIO.setmode(GPIO.BOARD)		# Numbers GPIOs by GPIO pin location
	GPIO.setwarnings(False)
        GPIO.setup(LEDPin_Red,   GPIO.OUT)	# Set red's   mode as output
        GPIO.setup(LEDPin_Amber, GPIO.OUT)	# Set amber's mode as output
        GPIO.setup(LEDPin_Green,  GPIO.OUT)	# Set green's mode as output
	GPIO.output(LEDPin_Red,  GPIO.LOW)	# Set red   pin high(+3.3V) to off led
	GPIO.output(LEDPin_Amber,GPIO.LOW)	# Set amber pin high(+3.3V) to off led
	GPIO.output(LEDPin_Green,GPIO.LOW)	# Set green pin high(+3.3V) to off led

# Turn off all street lights when at the end of the program
def allLightsOff():
	for led in ledPins:
	    GPIO.output(led, 0)		# switch all LEDs off
	delay(1)

# Switch On an LED on the street light
def lightOn(led):
	GPIO.output(led, True)

# Switch Off an LED on the street light
def lightOff(led):
	GPIO.output(led, False)	

# Turn off all street lights when at the end of the program
def halt():
	allLightsOff()
	GPIO.cleanup()
	sys.exit(0)

# Delay time
def delay(t):
	time.sleep(t)

signal.signal(signal.SIGINT, allLightsOff)

def start():
	# Loop forever
	while True:
			# Stop!  - light On: Red
		GPIO.output(LEDPin_Red, True)
		delay(TrafficOffTime)

		# Ready! - light On: Red and Amber
		GPIO.output(LEDPin_Amber, True)
		delay(TrafficReadyTime)
	
		# Move!  - light On: Green
		allLightsOff()
		lightOn(LEDPin_Green)
		delay(TrafficOnTime)
		
		# Amber On
		lightOff(LEDPin_Green)
		lightOn(LEDPin_Amber)
		delay(TrafficReadyTime)
	
		# Amber off (Red comes "On" at top of loop)
		lightOff(LEDPin_Amber)
