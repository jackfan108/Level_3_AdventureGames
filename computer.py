from thing import *


class Computer (Thing):
    def __init__ (self,name,loc,desc):
        Thing.__init__(self,name,loc,desc)

    def use(self,actor):
    	for stuff in actor.contents():
    		if stuff.is_homework():
    			stuff.do_homework()

    # FIX ME
