from microbit import *


def lcdwrite():
    # reset
    pin6.write_digital(0)
    sleep(50)
    pin6.write_digital(1)


    # send commands
    pin7.write_digital(0)

    pin8.write_digital(0) # start serial
    spi.write( bytearray(b'\x21\xBF\x04\x14\x0C\x20\x0C') )
    sleep(50)
    
    """
    sleep(50)
    spi.write( bytearray( 0b00100001 ) )
    sleep(50)
    spi.write( bytearray( 0b10010000 ) )
    sleep(50)
    spi.write( bytearray( 0b00100000 ) )
    sleep(50)
    spi.write( bytearray( 0b00001100 ) )
    sleep(50)
    spi.write( bytearray( 0b00001101 ) ) # inverse video?
    sleep(50)
    pin8.write_digital(1)
    sleep(50)

    # reset
    pin6.write_digital(0)
    sleep(50)
    pin6.write_digital(1)
    sleep(50)
    """

    # send data
    pin7.write_digital(1)
    sleep(50)
    pin8.write_digital(0)
    sleep(50)
    spi.write( bytearray( 0b00011111 ) )
    sleep(50)
    spi.write( bytearray( 0b00000101 ) )
    sleep(50)
    pin8.write_digital(1)
    print("finished")

#spi.init(baudrate=1000000, bits=8, mode=0, sclk=pin13, mosi=pin15, miso=pin14)
spi.init(baudrate = 328125, sclk = pin13, mosi = pin15, firstbit=spi.MSB)
print("Ready")


while True:
    display.show(Image.ARROW_W)
    if button_b.was_pressed():
        print("writing data")
        lcdwrite()

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
