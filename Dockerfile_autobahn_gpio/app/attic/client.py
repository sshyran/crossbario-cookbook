import os
import argparse
import six
import txaio

import random
import serial
import datetime
import time
# import psutil
import sys

from twisted.internet import reactor
from twisted.internet.error import ReactorNotRunning
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


class ClientSession(ApplicationSession):
    """
    Our WAMP session class .. place your app code here!
    """

    def onConnect(self):
        self.log.info("Client connected")
        self.join(self.config.realm, [u'anonymous'])
	
 	print 'hier'
#        def onhello(msg):
#            self.log.info("event for 'onhello' received: {msg}", msg=msg)

#        def oncpu(msg):
#            self.log.info("event for 'oncpu' received: {msg}", msg=msg)
#        yield self.subscribe(oncpu, 'server.local.oncpu')
#        self.log.info("subscribed to topic 'oncpu'")

        ts=0

        while True:               
#            tx = psutil.cpu_percent()
#            yield self.publish('server.local.counter', ts)
            yield self.publish('server.local.oncpu', ts)
            ts = ts + 1
            print ts,tx
            yield sleep(1)


    def onChallenge(self, challenge):
        self.log.info("Challenge for method {authmethod} received", authmethod=challenge.method)
        raise Exception("We haven't asked for authentication!")

    def onJoin(self, details):
        self.log.info("Client session joined {details}", details=details)

        # your main app code goes here! eg register procedures, subscribe to topics, etc

        self.leave()

    def onLeave(self, details):
        self.log.info("Router session closed ({details})", details=details)
        self.disconnect()

    def onDisconnect(self):
        self.log.info("Router connection closed")
        try:
            reactor.stop()
        except ReactorNotRunning:
            pass


if __name__ == '__main__':

    # Crossbar.io connection configuration
    url = os.environ.get(u'ws://104.199.76.81:8080/ws')
    realm = os.environ.get(u'realm1')
    print "hiers ", url,realm 	
    # parse command line parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug output.')
    parser.add_argument('--url', dest='url', type=six.text_type, default=u'ws://104.199.76.81:8080/ws', help='The router URL (default: "ws://localhost:8080/ws").')
    parser.add_argument('--realm', dest='realm', type=six.text_type, default=u'realm1', help='The realm to join (default: "realm1").')

    args = parser.parse_args()
    print args
    # start logging
    if args.debug:
	self.log.info("los gehts debug ")
        txaio.start_logging(level='debug')
    else:
	print "los gehts "
        txaio.start_logging(level='info')

    # any extra info we want to forward to our ClientSession (in self.config.extra)
    extra = {
        u'foobar': u'A custom value'
    }

    # now actually run a WAMP client using our session class ClientSession
    runner = ApplicationRunner(url=args.url, realm=args.realm, extra=extra)
    runner.run(ClientSession, auto_reconnect=True)
