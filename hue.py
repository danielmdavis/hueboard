import phue
from phue import Bridge
from pynput.keyboard import Listener

b = phue.Bridge('192.168.2.100')
b.connect()

b.get_api()

off = {'transitiontime' : 0, 'on' : False}
on = {'transitiontime' : 0, 'bri': 255, 'on' : True}

def on_press(key):
    # floor lamp
    if key.char == '7':
        b.set_light(6, off)
    if key.char == '8':
        b.set_light(5, off)
    if key.char == '9':
        b.set_light(9, off)

    # low lamp
    if key.char == '4':
        b.set_light(7, off)

    # under bed
    if key.char == '5':
        b.set_light(8, off)

    # behind monitor
    if key.char == '6':
        b.set_light(10, off)

def on_release(key):
    # floor lamp
    if key.char == '7':
        b.set_light(6, on)
    if key.char == '8':
        b.set_light(5, on)
    if key.char == '9':
        b.set_light(9, on)

    # low lamp
    if key.char == '4':
        b.set_light(7, on)

    # under bed
    if key.char == '5':
        b.set_light(8, on)

    # behind monitor
    if key.char == '6':
        b.set_light(10, on)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()