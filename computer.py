from thing import *


class Computer (Thing):
    def __init__ (self,name,loc,desc):
        Thing.__init__(self,name,loc,desc)

    def use(self,actor):
        for stuff in actor.contents():
            if (stuff.is_homework()):
              if not(stuff.is_done()):
                print('You have finished ' + stuff.name())
                stuff.do_homework()
              else:
                print('You already did ' + stuff.name())