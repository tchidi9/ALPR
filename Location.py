import RPi.GPIO as GPIO
import serial
import time, sys
import datetime

SERIAL_PORT = "/dev/ttyS0"    # Rasp 3 UART Port

ser = serial.Serial(SERIAL_PORT, baudrate = 115200, timeout = 5)


"""
When this class is called, it captures video for the number of seconds specified and
saves it to a remote location accessible by the program 
# captureDuration - The duration in seconds of the video captured
"""
def getLocationDateTime():
	'''
	AT+CGATT =1 # to attach GPRS.

	AT+SAPBR =3,1,"CONTYPE","GPRS" # activate bearer profile.

	AT+SAPBR =3,1,"APN","RCMNET"

	AT+SAPBR=1,1

	AT+SAPBR=2,1

	AT+CIPGSMLOC=1,1 # to get gsm location, time and date.

	AT+SAPBR =0,1 # to deactivate bearer profile.
	'''
	# prepare SIM module to start receiving GPRS information
        ser.write("AT+CGATT =1 \r") # to attach GPRS
        time.sleep(1)
        reply = ser.read(ser.inWaiting()) # Clean buf
	print reply
        ser.write("AT+SAPBR =3,1,'CONTYPE','GPRS' \r") # activate bearer profile
        time.sleep(1)
        reply = ser.read(ser.inWaiting()) # Clean buf
	print reply
        ser.write("AT+SAPBR =3,1,'APN','RCMNET' \r")
        time.sleep(1)
        reply = ser.read(ser.inWaiting()) # Clean buf
	print reply
        ser.write("AT+SAPBR=1,1 \r")
        time.sleep(1)
        reply = ser.read(ser.inWaiting()) # Clean buf
	print reply
        ser.write("AT+SAPBR=2,1 \r")
        time.sleep(1)
        reply = ser.read(ser.inWaiting()) # Clean buf
	print reply
        time.sleep(1)
        print "Listening for GPS information"

	while True:
	    reply = ser.read(ser.inWaiting())
	    if reply == "OK":
		ser.write("AT+CIPGSMLOC=1,1\r")
		time.sleep(1)
		reply = ser.read(ser.inWaiting())
		print "Location info received. Content:"
		print reply
		time.sleep(.500)
		ser.write("AT+CMGDA='DEL ALL'\r") # delete all
		time.sleep(.500)
		ser.read(ser.inWaiting()) # Clear buffer
		time.sleep(.500)
		break
	return reply
