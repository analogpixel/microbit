#!/usr/bin/env python
# https://microbit-micropython.readthedocs.io/en/latest/index.html

from microbit import *


while True:
    display.scroll('Matt!')
    display.show(Image.HEART)
    print("out to serial")
    sleep(2000)
