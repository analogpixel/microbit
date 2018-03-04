from microbit import *

start = 0x08
end = 0x77

# 6 rst
# reset the lcd

def setContrast(c):
    lcdwrite(0, bytearray(0x21) )
    lcdwrite(0, bytearray(0x80 | c))
    lcdwrite(0, bytearray(0x20))

def gotoXY(x,y):
    lcdwrite(0, bytearray(0x80 | x))
    lcdwrite(0, bytearray(0x40 | y))

def lcdwrite(data_or_command, data):
    # dcPin
    pin7.write_digital(data_or_command)


    # scePin
    pin8.write_digital(0)
    spi.write(data)

    # scePin
    pin8.write_digital(1)

spi.init(baudrate=1000000, bits=8, mode=0, sclk=pin13, mosi=pin15, miso=pin14)


def reset():
    pin6.write_digital(0)
    pin6.write_digital(1)
    lcdwrite(0, bytearray(0x21) )
    lcdwrite(0, bytearray(0xB0) )
    lcdwrite(0, bytearray(0x04) )
    lcdwrite(0, bytearray(0x14) )
    lcdwrite(0, bytearray(0x20) )
    lcdwrite(0, bytearray(0x0C) )


# set contrast 


print("Ready")


while True:
    display.show(Image.ARROW_W)
    if button_b.was_pressed():
        reset()
        print("writing data")
        setContrast(50)
        gotoXY(0,0)
        for  i in range(0, int(84*54/8)):
            lcdwrite(1, bytearray(0xFF))

    if button_a.was_pressed():
        display.show(Image.MEH)
        print("Scanning I2C bus...")
        for i in range(start, end + 1):
            try:
                i2c.read(i, 1)
            except OSError:
                pass
            else:
                print("Found:  [%s]" % hex(i))
        print("Scanning complete")
        print("Magnetometer [0x0e] Accelerometer [0x1d]")
    sleep(10)
