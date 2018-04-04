from Automodule import *

#positive degree = clockwise
#negative degree = COUNTERclockwise
mystepper = Stepper()

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

    
        answer = raw_input("what would you like to do:")
    
        if answer =='park':
                forward()
                if D2 <= 40:
                        stop()

        elif answer == 'stop':
                print "Ok!"
                PWM.stop("P8_13")
                PWM.stop("P8_19")
                PWM.cleanup()
        
                GPIO.output("P8_7", GPIO.LOW)
                GPIO.output("P8_8", GPIO.LOW)
                GPIO.output("P8_9", GPIO.LOW)
                GPIO.output("P8_10", GPIO.LOW)
                GPIO.output("P8_13", GPIO.LOW)
                GPIO.output("P8_14", GPIO.LOW)
                GPIO.output("P8_15", GPIO.LOW)
                GPIO.output("P8_16", GPIO.LOW)
                GPIO.output("P9_41",GPIO.LOW)
                GPIO.cleanup()
                break

        elif answer == 'ppark':
                forward()
                time.sleep(2)
                stop()

        
        elif answer == 'scan':
                scanread()

        elif answer =='turn':
                rightforward()  
                leftback()
                time.sleep(10)
          
        elif answer =='Move':
                Move()