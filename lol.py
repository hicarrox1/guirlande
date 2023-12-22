import microbit as mb

import neopixel

from random import randint

l = [(60,60,60),(60,0,0),(0,60,0),(0,0,60)]

np = neopixel.NeoPixel(mb.pin0, 30)
np1 = neopixel.NeoPixel(mb.pin1, 30)
np2 = neopixel.NeoPixel(mb.pin2, 30)
np.show()

def allume_all_led(rgb: tuple, led: neopixel):

    for i in range(30):

        led[i] = rgb
    led.show()

def stroboscope(led: neopixel):

    for i in range(30):

        led[i] = l[randint(0,3)]
    led.show()


def percent(percent: float, led: neopixel):

    if percent > 1:
        percent = 1
    
    for i in range(round(30*percent)):

        led[i] = (60,60,60)
    led.show()

while True:
    stroboscope(np)
    stroboscope(np1)
    stroboscope(np2)
    mp.sleep(150)
