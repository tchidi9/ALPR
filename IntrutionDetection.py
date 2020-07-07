import RPi.GPIO as GPIO
import time

DT  = 13
#DT  = 27
SCK = 11
#SCK = 17

def setup():
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setwarnings(False)
    GPIO.setup(SCK, GPIO.OUT)
    time.sleep(3)
    sample= readCount()
    flag=0
    status = True


# set pin numbers on DT and SCK
def readCount():
  i=0
  Count=0
 # print Count
 # time.sleep(0.001)
  GPIO.setup(DT, GPIO.OUT)
  GPIO.output(DT,1)
  GPIO.output(SCK,0)
  GPIO.setup(DT, GPIO.IN)

  while GPIO.input(DT) == 1:
      i=0
  for i in range(24):
        GPIO.output(SCK,1)
        Count=Count<<1

        GPIO.output(SCK,0)
        #time.sleep(0.001)
        if GPIO.input(DT) == 0:
            Count=Count+1
            #print Count

  GPIO.output(SCK,1)
  Count = Count^0x800000
  #time.sleep(0.001)
  GPIO.output(SCK,0)
  return Count

#time.sleep(3)
#sample= readCount()
#flag=0
#status = True

def start(status):
   while status:
      count= readCount()
      w=0
      w=(count-sample)/106
      print w,"g"
      # if weight detected is greater than or equals 10kg
      if w>10000:  
        if flag == 0:
          intruderDetected = True
          time.sleep(1.5)
          flag=1;
      # if weight detected is less than 10kg
      elif w<10000:
        if flag==1:
          intruderDetected = False
          time.sleep(2)
          flag=0
      time.sleep(0.5)

