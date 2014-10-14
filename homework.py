from mobile import *


class Homework (MobileThing):

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)

    def is_homework (self):
        return True

    # FIX ME
