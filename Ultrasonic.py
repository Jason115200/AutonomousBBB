import Adafruit_BBIO.ADC as ADC
import time


ADC.setup()
value = ADC.read("P9_40")
rawv = ADC.read_raw("P9_40")
voltage = value * 3.3#1.8V

D = voltage/0.00699

while 1:
    value = ADC.read("P9_40")
    rawv = ADC.read_raw("P9_40")
    voltage = value * 1.8 #1.8V
    D = voltage/0.00699 #.00699

    
    print(rawv,voltage,D)
    time.sleep(1)
    
#Yellow=GND White=Power Red=Data
