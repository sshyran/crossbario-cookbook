import os
import argparse
import six
import txaio
import time
import random
import sys
import Adafruit_DHT
import pause
from gpiozero import LED
led = LED(17)
led.on()

try:
    import asyncio
except ImportError:
    import trollius as asyncio

from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

class ClientSession(ApplicationSession):
    """
    Our WAMP session class .. place your app code here!
    """

    def onConnect(self):
        self.log.info("Client connected")
        self.join(self.config.realm, [u'anonymous'])

    def onChallenge(self, challenge):
        self.log.info("Challenge for method {authmethod} received", authmethod=challenge.method)
        raise Exception("We haven't asked for authentication!")

    def onJoin(self, details):
        self.log.info("Client session joined {details}", details=details)
	i=5
        # your main app code goes here! eg register procedures, subscribe to topics, etc
	while i<10 :
	#	while True:

            	yield led.on()
           	print 'on'
            	yield pause.seconds(1.5)
            	yield led.off()
           	print 'off'     
           	yield pause.seconds(1.0)


	#	humidity, temperature = Adafruit_DHT.read_retry(11, 4)
	#	print i, humidity,temperature
	#	if humidity is not None and temperature is not None:
    	#	    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
	#	else:
    	#	    print('Failed to get reading. Try again!')
    	#	    sys.exit(1)
	#
	 #   	x = random.randint(30, 50)

	#	print x
	#	yield self.publish('server.local.cpu', x)
		i=i+1

	#	time.sleep(1)
        self.leave()

    def onLeave(self, details):
        self.log.info("Router session closed ({details})", details=details)
        self.disconnect()

    def onDisconnect(self):
        self.log.info("Router connection closed")
        try:
            asyncio.get_event_loop().stop()
        except:
            pass


if __name__ == '__main__':

    # Crossbar.io connection configuration
    url = os.environ.get('CBURL', u'ws://localhost:8080/ws')
    realm = os.environ.get('CBREALM', u'realm1')

    # parse command line parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug output.')
    parser.add_argument('--url', dest='url', type=six.text_type, default=u'ws://104.199.76.81:8080/ws', help='The router URL (default: "ws://localhost:8080/ws").')
#    parser.add_argument('--router', type=six.text_type,default=u'ws://104.199.76.81:8080/ws',help='WAMP router URL.')
 
#    parser.add_argument('--realm',type=six.text_type, default='realm1',help='WAMP router realm.')
    parser.add_argument('--realm', dest='realm', type=six.text_type, default='realm1', help='The realm to join (default: "realm1").')

    args = parser.parse_args()

    # start logging
    if args.debug:
        txaio.start_logging(level='debug')
    else:
        txaio.start_logging(level='info')

    # any extra info we want to forward to our ClientSession (in self.config.extra)
    extra = {
        u'foobar': u'A custom value'
    }

    # now actually run a WAMP client using our session class ClientSession
    runner = ApplicationRunner(url=args.url, realm=args.realm, extra=extra)
    runner.run(ClientSession)
