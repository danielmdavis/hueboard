import phue
from phue import Bridge
from pynput.keyboard import Listener

b = phue.Bridge('192.168.2.100')
b.connect()

b.get_api()

off = {'transitiontime' : 0, 'on' : False}
on = {'transitiontime' : 0, 'bri': 255, 'on' : True}

def on_press(key):
    # print('foo')
    b.set_light(10, off)

def on_release(key):
    b.set_light(10, on)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()