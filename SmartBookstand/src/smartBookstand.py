
#turn on LED to specific color

import RPi.GPIO as GPIO
import time
import sys
import spidev

def info():
    print("This is Soo's library")

# Initialize MCP3008 - we can call read() to read the data. 
class MCP3008:
    def __init__(self, bus = 0, device = 0):
        self.bus, self.device = bus, device
        self.spi = spidev.SpiDev()
        self.open()
 
    def open(self):
        self.spi.open(self.bus, self.device)
        # Run SPI bus at low speed so we can capture everything in piscope
        self.spi.max_speed_hz = 7629
    
    def read(self, channel = 0):
        # Send these bytes on the MOSI line and read the MISO line
        resp = self.spi.xfer2([0b00000001, 0b10000000 + (channel << 4), 0b00000000])
        
        counter = 0
        number1 = 0
        number2 = 0
        for b in resp:
            #print(format(b, '#010b'))
            if (counter == 0):
                pass
            elif (counter == 1):
                number1 = b << 8
            else: #counter == 2
                number2 = b
            counter += 1
        number = number1 + number2
        return number

            
    def close(self):
        self.spi.close()

###### Source: https://tutorials-raspberrypi.com/photoresistor-brightness-light-sensor-with-raspberry-pi/
###### Functions taken from adc.py from lab 4.1.3
###### Source: https://github.com/adafruit/Adafruit_Python_MCP3008

class ShiftRegister:
    def __init__(self, device = 0):
        self.bus = 1
        self.device = device
        self.spi = spidev.SpiDev()
        self.open()

    def open(self):
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = 7629

    def turnOnLED(self, ledNUM):
        self.spi.xfer2([0x3F]) # turn off before
        time.sleep(0.005)
        self.spi.xfer2([ledNUM])
    
    def turnOffLED(self):
        self.spi.xfer2([0x00])

### source: https://raspberrypi.stackexchange.com/questions/73346/how-to-enable-spi1-and-spi0-at-the-same-time
### source: https://pinout.xyz/pinout/spi
