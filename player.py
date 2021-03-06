from person import *
from clock import *

import sys

class Player (Person):

    # static field representing the player
    me = None
    # static field recording god_mode
    god_mode = False

    def __init__ (self,name,loc,desc):
        Person.__init__(self,name,loc,desc)
        Player.me = self

    # Grab any kind of thing from player's location, 
    # given its name.  The thing may be in the possession of
    # the place, or in the possession of a person at the place.
   
    def thing_named (self,name):
        for x in self.location().contents():
            if x.name() == name:
                return x
        for x in self.list_contents():
            if x.name() == name:
                return x
        for x in self.contents():
            if x.name() == name:
                return x
        return None

    def look_around (self):
        def names (lst):
            return ', '.join([x.name() for x in lst])

        loc = self.location()
        desc = loc.desc
        exits = loc.exits()
        people = self.people_around()
        all_stuff = self.stuff_around()
        contents = self.contents()

        print '------------------------------------------------------------'
        print 'You are in', loc.name(), ':', desc

        if all_stuff:
            print 'You see:', names(all_stuff)
        else: 
            print 'The room is empty'

        if people:
            print 'You see:', names(people)
        else:
            print 'You see no one around'
        if contents:
            print 'You have:', names(contents)

        if exits:
            print 'Exits:', ', '.join([x for x in exits])
        else:
            print 'There are no exits'
        print 'You have', self._health, 'health.'

    def die (self):
        self.say('I am slain!')
        Person.die(self)
        print 'This game for you is now over...'
        sys.exit(0)

    def is_player (self):
        return True