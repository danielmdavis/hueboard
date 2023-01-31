
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
on_orange = {'transitiontime' : 0, 'bri': 255, 'on' : True, 'xy': converter.rgb_to_xy(255, 127, 0)}
on_yellow = {'transitiontime' : 0, 'bri': 255, 'on' : True, 'xy': converter.rgb_to_xy(255, 255, 0)}
on_green = {'transitiontime' : 0, 'bri': 255, 'on' : True, 'xy': converter.rgb_to_xy(0, 255, 0)}
on_blue = {'transitiontime' : 0, 'bri': 255, 'on' : True, 'xy': converter.rgb_to_xy(0, 100, 100)}
on_indigo = {'transitiontime' : 0, 'bri': 255, 'on' : True, 'xy': converter.rgb_to_xy(0, 0, 255)}
on_violet = {'transitiontime' : 0, 'bri': 255, 'on' : True, 'xy': converter.rgb_to_xy(143, 0, 255)}

# color setters: ROYGBIV and other
A_held, O_held, E_held, U_held, I_held, D_held, H_held = False, False, False, False, False, False, False
Q_held = False

global light_id
light_id = {
    '7': 6, # lamp tree top
    '8': 5, # lamp tree mid
    '9': 9, # lamp tree bottom
    '4': 7, # low lamp
    '5': 8, # under bed
    '6': 10 # behind monitor
}

def parse_light_press(key):
    bridge.set_light(light_id[key.char], off)

def parse_light_release(key):
    if A_held == True:
        bridge.set_light(light_id[key.char], on_red)
    elif O_held == True:
        bridge.set_light(light_id[key.char], on_orange)
    elif E_held == True:
        bridge.set_light(light_id[key.char], on_yellow)
    elif U_held == True:
        bridge.set_light(light_id[key.char], on_green)
    elif I_held == True:
        bridge.set_light(light_id[key.char], on_blue)
    elif D_held == True:
        bridge.set_light(light_id[key.char], on_indigo)
    elif H_held == True:
        bridge.set_light(light_id[key.char], on_violet)
    elif Q_held == True:
        bridge.set_light(light_id[key.char], {'transitiontime' : 0, 'on' : True, 'bri': 255, 'xy': [random.random(), random.random()]})
    else:
        bridge.set_light(light_id[key.char], on)



def parse_color_press(key):
    global A_held, O_held, E_held, U_held, I_held, D_held, H_held
    global Q_held

    if key.char == 'a': A_held = True
    if key.char == 'o': O_held = True
    if key.char == 'e': E_held = True
    if key.char == 'u': U_held = True
    if key.char == 'i': I_held = True
    if key.char == 'd': D_held = True
    if key.char == 'h': H_held = True

    if key.char == 'q': Q_held = True

def parse_color_release(key):
    global A_held, O_held, E_held, U_held, I_held, D_held, H_held
    global Q_held

    if key.char == 'a': A_held = False
    if key.char == 'o': O_held = False
    if key.char == 'e': E_held = False
    if key.char == 'u': U_held = False
    if key.char == 'i': I_held = False
    if key.char == 'd': D_held = False
    if key.char == 'h': H_held = False

    if key.char == 'q': Q_held = False    

 # talks to the listener
def on_press(key):
    if key.char == 'a' or key.char == 'o' or key.char == 'e' or key.char == 'u' or key.char == 'i' or key.char == 'd' or key.char == 'h' or key.char == 'q':
        parse_color_press(key)
    if key.char == '7' or key.char == '8' or key.char == '9' or key.char == '4' or key.char == '5' or key.char == '6':
        parse_light_press(key)

def on_release(key):
    if key.char == 'a' or key.char == 'o' or key.char == 'e' or key.char == 'u' or key.char == 'i' or key.char == 'd' or key.char == 'h' or key.char == 'q':
        parse_color_release(key)
    if key.char == '7' or key.char == '8' or key.char == '9' or key.char == '4' or key.char == '5' or key.char == '6':
        parse_light_release(key)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

