from microbit import *
import random

def lcdWrite(cmd, data):
   pin8.write_digital(0)
   pin7.write_digital(cmd)
   spi.write( bytearray([data]) )
   pin8.write_digital(1)
   #print("wrote:", data)

def lcdWrite2(cmd, data):
   pin8.write_digital(0)
   pin7.write_digital(cmd)
   spi.write( bytearray(data) )
   pin8.write_digital(1)
   #print("wrote:", data)

def lcdinit():
    #pin8.write_digital(0) # start serial
    #pin7.write_digital(0) # send commands
    #spi.write( bytearray( [0b00100001, 0b10010000, 0b00100000, 0b00001100, 0b10000000, 0b00001101] ) )
    #spi.write( bytearray([ 0x21, 0xB0, 0x04, 0x14, 0x20, 0x0c]))
    lcdWrite2(0, [ 0x21, 0xB0, 0x04, 0x14, 0x20, 0x0c])
    #pin8.write_digital(1)
    #lcdWrite(0, 0x21)
    #lcdWrite(0, 0xB0)
    #lcdWrite(0, 0x04)
    #lcdWrite(0, 0x14)
    #lcdWrite(0, 0x20)
    #lcdWrite(0, 0x0c)
    print("init")

def lcdwrite():
    for x in range(0,500):
      lcdWrite(1, random.randint(0, 255))
      #lcdWrite(1, 0b00011111)
      #lcdWrite(1, 0b11011011)
    #pin8.write_digital(0) # start serial
    #pin7.write_digital(1) # send data
    #spi.write( bytearray( [0b00011111, 0b00000101] ) )
    #spi.write( bytearray( [0b00011111, 0b00000101] ) )
    #spi.write( bytearray( [0b00011111, 0b00000101] ) )
    #spi.write( bytearray( [0b00011111, 0b00000101] ) )
    #pin8.write_digital(1)
    print("wrote data")

#spi.init(baudrate=9600, bits=8,  mode=0, sclk=pin13, mosi=pin15)
spi.init(baudrate=100000, bits=8,  mode=0, sclk=pin13, mosi=pin15)
pin6.write_digital(0)
pin6.write_digital(1)
print("Ready")
lcdinit()

while True:
  lcdwrite()
  #sleep(500)

"""
while True:
    display.show(Image.ARROW_W)
    if button_b.was_pressed():
        display.show(Image.MEH)
        print("writing data")
        lcdwrite()
	sleep(2000)

    if button_a.was_pressed():
        display.show(Image.MEH)
        lcdinit()
	sleep(2000)
"""
