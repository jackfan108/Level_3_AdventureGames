from mobile import *
import random

class Person (MobileThing):    # Container...

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)
        self._max_health = random.randint(15,20)
        self._health = self._max_health
        self._contents = []

    def health (self):
        return self._health

    def reset_health (self):
        self._health = self._maxHealth

    def say (self,msg):
        loc = self.location()
        loc.report(self.name()+' says -- '+msg)

    def have_fit (self):
        self.say('Yaaaaah! I am upset!')

    def people_around (self):
        return [x for x in self.location().contents()
                    if x.is_person() and x is not self]

    def stuff_around (self):
        return [x for x in self.location().contents() if not x.is_person()]


    # this function should return everything that everyone in the
    # same location as this person are holding/carrying

    def peek_around (self):
        people = self.people_around()
        people_contents = []
        for person in people:
            for content in person.contents():
                person.say('I have ' + content.name() + '. You want it? haha!')
                people_contents.append(content)
        if(people_contents == []):
          print "No one is carrying anything."
        return people_contents

    # silent version of peek
    def list_contents (self):
        people = self.people_around()
        people_contents = []
        for person in people:
            for content in person.contents():
                people_contents.append(content)
        return people_contents

    def lose (self,t,loseto):
        self.say('I lose ' + t.name())
        self.have_fit()
        t.move(loseto)
    
    def go (self,direction):
        loc = self.location()
        exits = loc.exits()
        if direction in exits:
            t = exits[direction]
            self.leave_room()
            loc.report(self.name()+' moves from '+ loc.name()+' to '+t.name())
            self.move(t)
            self.enter_room()
            return True
        else:
            print 'No exit in direction', direction
            return False


    def suffer (self,hits):
        self.say('Ouch! '+str(hits)+' hits is more than I want!')
        self._health -= hits
        if (self.health() < 1):
            self.die()
        else:
            self.say('My health is now '+str(self.health()))

    def die (self):
        self.location().broadcast('An earth-shattering, soul-piercing scream is heard...')
        for item in self.contents():
          item.move(self.location())
        self.destroy()
        

    def enter_room (self):
        people = self.people_around()
        if people:
            self.say('Hi ' + ', '.join([x.name() for x in people]))

    def leave_room (self):
        pass   # do nothing to reduce verbiage

    def take (self,actor):
        actor.say('I am not strong enough to just take '+self.name())

    def drop (self,actor):
        print actor.name(),'is not carrying',self.name()

    def give (self,actor,target):
        print actor.name(),'is not carrying',self.name()
        
    def accept (self,obj,source):
        self.say('Thanks, ' + source.name())
        obj.move(self)

    def is_person (self):
        return True

    def have_thing (self,t):
        for c in self.contents():
            if c is t:
                return True
        return False

    def add_thing (self,t):
        self._contents.append(t)

    def del_thing (self,t):
        self._contents = [x for x in self._contents if x is not t]

    def contents (self):
        return self._contents

    def is_troll (self):
      return False