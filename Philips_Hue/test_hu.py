#!/usr/bin/python

from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.1.80'}, user={'name':'12345'})
resource = {'which':'all', 'verbose':True}
bridge.light.get(resource)


