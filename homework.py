from mobile import *


class Homework (MobileThing):

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)
        self._done = False

    def do_homework (self):
    	self._done = True
    	self._name = 'done-' + self._name
    	print self._done

    def is_homework (self):
        return True

    def is_done (self):
    	return self._done
    # FIX ME
