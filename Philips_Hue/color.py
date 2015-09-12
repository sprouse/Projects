#!/usr/bin/python

from phue import Bridge
import time

b = Bridge('192.168.1.80')

light = 'Bedroom'

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
#b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

# Prints if light 1 is on or not
print b.get_light(1, 'on')
print b.get_light(2, 'on')
print b.get_light(3, 'on')

b.set_light('Bedroom', 'on', True)
b.set_light('Bedroom', 'bri', 254)
for i in range(0,10):
	for j in xrange(20,4000,300):
		b.set_light('Bedroom', 'hue', j)
		time.sleep(2)
		print j
	for j in xrange(4000,20,-300):
		b.set_light('Bedroom', 'hue', j)
		time.sleep(2)
		print j

