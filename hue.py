
# lightbulb api control
import phue
bridge = phue.Bridge('192.168.2.100')
bridge.connect()
bridge.get_api()

# keystroke event listener
from pynput.keyboard import Listener

# convert normal to exotic color math
from rgbxy import Converter
from rgbxy import GamutC
converter = Converter(GamutC)

import random

off = {'transitiontime' : 0, 'on' : False}
on = {'transitiontime' : 0, 'bri': 255, 'on' : True}
on_red = {'transitiontime' : 0, 'bri': 255, 'on' : True, 'xy': converter.rgb_to_xy(255, 0, 0)}
on_green = {'transitiontime' : 0, 'bri': 255, 'on' : True, 'xy': converter.rgb_to_xy(0, 255, 0)}
on_blue = {'transitiontime' : 0, 'bri': 255, 'on' : True, 'xy': converter.rgb_to_xy(0, 0, 255)}

Q_held = False

A_held = False
O_held = False
E_held = False


def parse_color_press(key):
    if key.char == 'a':
        global A_held
        A_held = True
    if key.char == 'o':
        global O_held
        O_held = True
    if key.char == 'e':
        global E_held
        E_held = True

    if key.char == 'q':
        global Q_held
        Q_held = True

def parse_color_release(key):
    if key.char == 'a':
        global A_held
        A_held = False
    if key.char == 'o':
        global O_held
        O_held = False
    if key.char == 'e':
        global E_held
        E_held = False

    if key.char == 'q':
        global Q_held
        Q_held = False        

def parse_light_release(key):

    light_id = {
        '7': 6, # lamp tree top
        '8': 5, # lamp tree mid
        '9': 9, # lamp tree bottom
        '4': 7, # low lamp
        '5': 8, # under bed
        '6': 10 # behind monitor
    }

    if A_held == True:
        bridge.set_light(light_id[key.char], on_red)
    elif O_held == True:
        bridge.set_light(light_id[key.char], on_green)
    elif E_held == True:
        bridge.set_light(light_id[key.char], on_blue)
    elif Q_held == True:
        bridge.set_light(light_id[key.char], {'transitiontime' : 0, 'on' : True, 'bri': 255, 'xy': [random.random(), random.random()]})
    else:
        bridge.set_light(light_id[key.char], on)

def on_press(key):

    parse_color_press(key)

    # floor lamp, descending
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
    
    if key.char == 'a' or key.char == 'o' or key.char == 'e' or key.char == 'q':
        parse_color_release(key)

    if key.char == '7' or key.char == '8' or key.char == '9' or key.char == '4' or key.char == '5' or key.char == '6':
        parse_light_release(key)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

