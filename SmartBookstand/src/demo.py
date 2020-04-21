import smartBookstand

def readAmbientLight(adc):
    print("This is the Ambient Light Reading Function.")
    data = adc.read(0)
    print(data)

def readPotentiometer(adc, channel):
    print('This is the Potentiometer Reading Function')
    print("Channel" , channel)
    data = adc.read(channel)
    print(data)

def main():
    adc = smartBookstand.MCP3008()

    #Initialize Shift Registers
    red = smartBookstand.ShiftRegister()
    green = smartBookstand.ShiftRegister()
    blue = smartBookstand.ShiftRegister()
    
    smartBookstand.info()

    readAmbientLight(adc)
    
    readPotentiometer(adc, 1)
    readPotentiometer(adc, 2)
    readPotentiometer(adc, 3)
    readPotentiometer(adc, 4)
    
    #LED 1/8
    red.turnOnLED(1)
    red.turnOffLED()
    blue.turnOnLED(1)
    blue.turnOffLED()
    green.turnOnLED(1)
    green.turnOffLED()

    #LED 2/8
    red.turnOnLED(2)
    red.turnOffLED()
    blue.turnOnLED(2)
    blue.turnOffLED()
    green.turnOnLED(2)
    green.turnOffLED()

if __name__ == "__main__":
    main()