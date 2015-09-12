#!/usr/bin/python

from phue import Bridge
import time

b = Bridge('192.168.1.80')

#light = ['Livingroom','Bedroom']
#light = ['Bedroom']
light = ['Livingroom']

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
#b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

# Prints if light 1 is on or not
def status(light_list):
	for light in light_list:
		print light
		print '\t',b.get_light(light, 'on')
		print '\t',b.get_light(light, 'hue')
		print '\t',b.get_light(light, 'bri')

status(light)
if True:
	b.set_light(light, 'on', True)
	b.set_light(light, 'bri', 255)
	b.set_light(light, 'hue', 17000)
	b.set_light(light, 'sat', 176)
status(light)
