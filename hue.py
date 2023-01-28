import phue
from phue import Bridge

b = phue.Bridge('192.168.2.100')
b.connect()

b.get_api()

b.set_light(6, 'off', True)