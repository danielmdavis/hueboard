import phue
from phue import Bridge
import random
from pynput.keyboard import Listener

bridge = phue.Bridge('192.168.2.100')
bridge.connect()

bridge.get_api()

off = {'transitiontime' : 0, 'on' : False}
on = {'transitiontime' : 0, 'bri': 255, 'on' : True}
onColor = {'transitiontime' : 0, 'on' : True, 'bri': 255, 'xy': [random.random(), 1]}

aHeld = False



def on_press(key):
    if key.char == 'a':
        global aHeld
        aHeld = True

    # floor lamp
    if key.char == '7':
        bridge.set_light(6, off)
    if key.char == '8':
        bridge.set_light(5, off)
    if key.char == '9':
        bridge.set_light(9, off)
    # low lamp
    if key.char == '4':
        bridge.set_light(7, off)
    # under bed
    if key.char == '5':
        bridge.set_light(8, off)
    # behind monitor
    if key.char == '6':
        bridge.set_light(10, off)

def on_release(key):
    if key.char == 'a':
        global aHeld
        aHeld = False

    # floor lamp
    if key.char == '7':
        if aHeld == True:
            bridge.set_light(6, {'transitiontime' : 0, 'on' : True, 'bri': 255, 'xy': [random.random(), random.random()]})
        else:
            bridge.set_light(6, on)
    if key.char == '8':
        if aHeld == True:
            bridge.set_light(5, {'transitiontime' : 0, 'on' : True, 'bri': 255, 'xy': [random.random(), random.random()]})
        else:
            bridge.set_light(5, on)
    if key.char == '9':
        if aHeld == True:
            bridge.set_light(9, {'transitiontime' : 0, 'on' : True, 'bri': 255, 'xy': [random.random(), random.random()]})
        else:
            bridge.set_light(9, on)
    # low lamp
    if key.char == '4':
        if aHeld == True:
            bridge.set_light(7, {'transitiontime' : 0, 'on' : True, 'bri': 255, 'xy': [random.random(), random.random()]})
        else:
            bridge.set_light(7, on)
    # under bed
    if key.char == '5':
        if aHeld == True:
            bridge.set_light(8, {'transitiontime' : 0, 'on' : True, 'bri': 255, 'xy': [random.random(), random.random()]})
        else:
            bridge.set_light(8, on)
    # behind monitor
    if key.char == '6':
        if aHeld == True:
            bridge.set_light(10, {'transitiontime' : 0, 'on' : True, 'bri': 255, 'xy': [random.random(), random.random()]})
        else:
            bridge.set_light(10, on)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

