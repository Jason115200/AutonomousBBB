import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
import math
from bbpystepper import Stepper
from subprocess import call
import os

count = 0

voice = "rms"

#out1 is redwire to motor out2 is black wire to motor out3 is red to other motor
ADC.setup()

value = ADC.read("P9_40")
rawv = ADC.read_raw("P9_40")
voltage = value * 1.8 #1.8V

value2 = ADC.read("P9_36")
rawv2 = ADC.read_raw("P9_36")
voltage2 = value * 1.8 #1.8V

value3 = ADC.read("P9_38")
rawv3 = ADC.read_raw("P9_38")
voltage3 = value3 * 1.8 #1.8V

D3 = voltage3/0.00699

D2 = voltage2/0.00699

D = voltage/0.00699
# indictorpin
GPIO.setup("P8_9", GPIO.OUT)
#leftmotor LOOK AT FROM FRONT
GPIO.setup("P8_7", GPIO.OUT)#in1
GPIO.setup("P8_8", GPIO.OUT)#in2
PWM.start("P8_13",0)#ena

#rightmotor
GPIO.setup("P8_9", GPIO.OUT)#in3
GPIO.setup("P8_10", GPIO.OUT)#in4
PWM.start("P8_19",0)#enb
duty = 100

#Steering Wheel
GPIO.setup("P8_13", GPIO.OUT)#in1
GPIO.setup("P8_14", GPIO.OUT)#in2
GPIO.setup("P8_15", GPIO.OUT)#in3
GPIO.setup("P8_16", GPIO.OUT)#in4

#rang 100ms
GPIO.setup("P9_41", GPIO.OUT)


def speak(output):
    print "[R.A.S.U.L]: " + output #name and what ever it is saying
    call(["flite", "-voice" , voice, "-t", output ]) #the voice tech it use (idk how it works jsut keep it here)

def steer():
    mystepper.rotate(45, 15)
    time.sleep(2)
    mystepper.rotate(-90, 15)
    time.sleep(2)
    mystepper.rotate(45, 15)

def HiLoUl():
    while G:
        GPIO.output("P9_41",GPIO.LOW)
        time.sleep(1)
        GPIO.output("P9_41",GPIO.HIGH)
        time.sleep(1)

def forward():
    GPIO.output("P8_7",GPIO.HIGH)
    GPIO.output("P8_9",GPIO.HIGH)
    GPIO.output("P8_8",GPIO.LOW)
    GPIO.output("P8_10",GPIO.LOW)
    PWM.set_duty_cycle("P8_13",duty)
    PWM.set_duty_cycle("P8_19",duty)
    
def stop():
    GPIO.output("P8_7",GPIO.HIGH)
    GPIO.output("P8_8",GPIO.HIGH)
    GPIO.output("P8_9",GPIO.LOW)
    GPIO.output("P8_10",GPIO.LOW)
    PWM.set_duty_cycle("P8_13",0)
    PWM.set_duty_cycle("P8_19",0)

def back():
    GPIO.output("P8_7",GPIO.LOW)
    GPIO.output("P8_9",GPIO.LOW)
    GPIO.output("P8_8",GPIO.HIGH)
    GPIO.output("P8_10",GPIO.HIGH)
    PWM.set_duty_cycle("P8_13",duty)
    PWM.set_duty_cycle("P8_19",duty)

def leftforward():
    GPIO.output("P8_7",GPIO.HIGH)
    GPIO.output("P8_8",GPIO.LOW)
    PWM.set_duty_cycle("P8_13",duty)

def leftback():
    GPIO.output("P8_7",GPIO.LOW)
    GPIO.output("P8_8",GPIO.HIGH)
    PWM.set_duty_cycle("P8_13",duty)

def rightforward():
    GPIO.output("P8_9",GPIO.HIGH)
    GPIO.output("P8_10",GPIO.LOW)
    PWM.set_duty_cycle("P8_19",duty)

def rightback():
    GPIO.output("P8_9",GPIO.LOW)
    GPIO.output("P8_10",GPIO.HIGH)
    PWM.set_duty_cycle("P8_19",duty)    

def Value():
    while 1:
        GPIO.output("P9_41",GPIO.HIGH)
        time.sleep(1)

        value = ADC.read("P9_40")
        rawv = ADC.read_raw("P9_40")
        voltage = value * 1.8 #1.8V
        D = voltage/0.00699 #.00699
        #41
    
        value2 = ADC.read("P9_36")
        rawv2 = ADC.read_raw("P9_36")
        voltage2 = value * 1.8 #1.8V
        D2 = voltage2/0.00699
        #27

        value3 = ADC.read("P9_38")
        rawv3 = ADC.read_raw("P9_38")
        voltage3 = value3 * 1.8 #1.8V
        D3 = voltage3/0.00699
        #15

def scanread():
    
    for count in range(5):
        GPIO.output("P9_41",GPIO.HIGH)
        time.sleep(1)

        value = ADC.read("P9_40")
        rawv = ADC.read_raw("P9_40")
        voltage = value * 1.8 #1.8V
        D = voltage/0.00699 #.00699
        #41
    
        value2 = ADC.read("P9_36")
        rawv2 = ADC.read_raw("P9_36")
        voltage2 = value * 1.8 #1.8V
        D2 = voltage2/0.00699
        #27

        value3 = ADC.read("P9_38")
        rawv3 = ADC.read_raw("P9_38")
        voltage3 = value3 * 1.8 #1.8V
        D3 = voltage3/0.00699
        #15
        
        print(D,D3)
    
        time.sleep(1)
        
        GPIO.output("P9_41",GPIO.LOW)
        time.sleep(1)
            
def ReadValue():
    
    while 1:
        forward()
        GPIO.output("P9_41",GPIO.HIGH)
        time.sleep(1)

        value = ADC.read("P9_40")
        rawv = ADC.read_raw("P9_40")
        voltage = value * 1.8 #1.8V
        D = voltage/0.00699 #.00699
        
    
        value2 = ADC.read("P9_36")
        rawv2 = ADC.read_raw("P9_36")
        voltage2 = value * 1.8 #1.8V
        D2 = voltage2/0.00699
        

        value3 = ADC.read("P9_38")
        rawv3 = ADC.read_raw("P9_38")
        voltage3 = value3 * 1.8 #1.8V
        D3 = voltage3/0.00699
        
        GPIO.output("P9_41",GPIO.LOW)
        time.sleep(1)
        
        if D and D3 >= 25:
            stop()
            print "Done!" #change this to turn on LED or buzzer
            break

def Move():
    while 1:
        value = ADC.read("P9_40")
        rawv = ADC.read_raw("P9_40")
        voltage = value * 1.8 #1.8V
        D = voltage/0.00699 #.00699
    
        if D <= 50:
            speak('Move bitch get out the way')
            print('Move')