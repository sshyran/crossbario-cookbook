###############################################################################
#
# Copyright (C) 2014, Tavendo GmbH and/or collaborators. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
###############################################################################

from twisted.internet.defer import inlineCallbacks
from twisted.logger import Logger

from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.wamp import ApplicationRunner
from autobahn.wamp.exception import ApplicationError
import six
import argparse
import glob
import random
import serial
import datetime
import time
import psutil
import sys

class Zaehler(ApplicationSession):

    log = Logger()

    @inlineCallbacks
    def onJoin(self, details):
 
        def oncpu(msg):
            self.log.info("event for 'oncpu' received: {msg}", msg=msg)

        yield self.subscribe(oncpu, 'server.local.oncpu')
        self.log.info("subscribed to topic 'oncpu'")

        i=0
        while i<10:               
		x = random.randint(30, 50)

               	print x
               	yield self.publish('server.local.cpu', x)


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--router', type=six.text_type,
            default=u'ws://104.199.76.81:8080/ws',help='WAMP router URL.')
 
    parser.add_argument(
        '--realm',type=six.text_type, default=u'realm1',help='WAMP router realm.')
    parser.add_argument('--trace', action='store_true',
        default=False, help='Trace WAMP message traffic.')

    args = parser.parse_args()
    extra = {}
    runner = ApplicationRunner(url=args.router, realm=args.realm, extra=extra)
    runner.run(Zaehler)
