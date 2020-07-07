#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

BeepPin   = 26    # set pin 26 as buzzer pin on Raspberry Pi
timer     = 0
timePassed= 0
beepTime  = 5
startTime = 0
endTime   = 0

def setup():
        GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
        GPIO.setup(BeepPin, GPIO.OUT)   # Set BeepPin's mode is output
	GPIO.output(BeepPin, GPIO.HIGH) # Set BeepPin high(+3.3V) to off beep

# beep warning for smoke and flame indication
def beep():
	ResetTimer()
	while(IsTimeUp() != True):
		On()
                time.sleep(duration)
                Off()
                time.sleep(duration)

# beep alarm for smoke and flame indication
def alarm(ThereIsDanger):
	while(ThereIsDanger):
		On()

# beep on
def On():
        GPIO.output(BeepPin, GPIO.LOW)

# beep off
def Off():
        GPIO.output(BeepPin, GPIO.HIGH)

# check time if it is ok to switch off buzzer
def SwitchOff():
	endTime    = time.time()
        timePassed = startTime - endTime
        if (beepTime > timePassed):
		ResetTimer()
        return (beepTime > timePassed)

# check time if it is ok to switch off buzzer
def Reset():
        ResetTimer()
	Off()
        return (beepTime > timePassed)

# reset timer
def ResetTimer():
        timePassed = 0
        startTime  = 0
        endTime    = 0

# clear all definitions and initialization for pins
def destroy():
        GPIO.cleanup()                  # release resource
        time.sleep(0.2)
