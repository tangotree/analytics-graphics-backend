import time
import random

from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession


class AppSession(ApplicationSession):
    @inlineCallbacks
    def onJoin(self, details):
        print("session attached")
        while True:
            value = random.uniform(1, 600)
            timestamp = int(time.time()*1000)
            yield self.publish('com.myapp.test', [timestamp, value])
            yield sleep(1)
