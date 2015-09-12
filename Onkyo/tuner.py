#!/usr/bin/env python

import eiscp
def test():
	receiver = eiscp.eISCP('192.168.2.114')
	#receiver.command('zone2.power=on')
	receiver.command('zone2.power=standby')

	receiver.disconnect()

if __name__=='__main__':
	test()

