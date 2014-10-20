
import random

from room import *
from verbs import *
from player import *
from npc import *
from radar import *
from troll import *
from professor import *
from homework import *
from computer import *
from badninja import *
from trollhunter import *

REVERSE = {
    'north' : 'south',
    'east' : 'west',
    'south' : 'north',
    'west' : 'east',
    'up' : 'down',
    'down' : 'up'
}


# add an exit in 'fr' toward 'to' in direction 'dir'
def connect (fr,dir,to):
    fr.exits()[dir] = to

# add an exit in 'fr' toward 'to' in direction 'dir'
# and an exit the other way, in 'to' toward 'fr' in the reverse direction
def biconnect (fr,dir,to):
    connect(fr,dir,to)
    connect(to,REVERSE[dir],fr)



def create_world ():

    mh353 = Room('Riccardo Office', 'A dark and gloomy place.')
    mh3rd = Room('Milas Hall Third Floor', 'The entrance is boarded up.')
    mh2nd = Room('Milas Hall Second Floor', 'Can we play the piano yet?')
    mh1st = Room('Milas Hall First Floor', 'The lobby... of doom!')
    oval = Room('Oval','The center of the college.')
    ac1st = Room('Academic Center First Floor','I can see my house from here!')
    ac113 = Room('Academic Center 113','Where dreams go to die.')
    cc1st = Room('Campus Center First Floor','The food sucks.')
    westh = Room('West Hall','Not the best hall.')
    easth = Room('East Hall','The best hall.')
    babson = Room('Babson College','A strange and magical realm.')
    portal = Room('Magic Portal','A swirling rift to some other dimension.')
    srift = Room('Summoner\'s Rift','A forest with a river running through the middle.')
    ttree = Room('Twisted Treeline','Spooky.')
    cscar = Room('Crystal Scar','Real men have these.')
    endw = Room('End of the world','Is it really the end?')
    habyss = Room('Howling Abyss','It looks back.')

    biconnect(mh353, 'east',  mh3rd)
    biconnect(mh3rd, 'down',  mh2nd)
    biconnect(mh2nd, 'down',  mh1st)
    biconnect(mh1st, 'north',  oval)
    biconnect(oval, 'east',  cc1st)
    biconnect(cc1st, 'east',  westh)
    biconnect(westh, 'east',  easth)
    biconnect(oval, 'north',  babson)
    biconnect(oval, 'west',  ac1st)
    biconnect(ac1st, 'north',  ac113)
    biconnect(babson, 'north', portal)
    biconnect(portal,'north', srift)
    biconnect(srift, 'west', ttree)
    biconnect(srift, 'east', cscar)
    biconnect(srift, 'north', endw)
    biconnect(endw, 'north', habyss)

    # The player is the first 'thing' that has to be created

    Player('Blubbering-Fool', oval, 'an unlikely hero.')

    Radar('handy-radar',mh353, 'beep boop bop.') 
    Thing('blackboard', ac113, 'not a whiteboard.')
    Thing('lovely-trees', oval, 'subjectively lovely.')
    MobileThing('cs-book', oval, 'the title is: \"Introduction to First-Person Shooter Games\"')
    MobileThing('math-book', oval, 'math is hard.')
    MobileThing('chalice', srift, 'the mana never seems to run out')
    MobileThing('lantern', ttree, 'it\'s wriggly.')
    MobileThing('trinity force', cscar, 'tons of damage')
    MobileThing('prox card', oval, 'Reads, \'Riccardo Pucella\'.')
    MobileThing('poro', endw, 'it\'s so fluffy!')

    Computer('hal-9000', ac113, 'sinister')
    Computer('johnny-5', easth, 'boop boop beep')

    Professor('Riccardo',mh353,random.randint(1,5),2,'Scary!')
    shredder = Badninja('Shredder',oval, random.randint(1,5),'Even scarier than Riccardo!')
    Player.me.clock.register(1,shredder.steal_homework)
    potter = Trollhunter('Harry Potter', oval, random.randint(1,5), 'You can tell he dislikes trolls right away')
    Player.me.clock.register(1,potter.look_for_trolls)
    Player.me.clock.register(2,potter.move_somewhere)

    homeworks = ['hw-1', 
                 'hw-2',
                 'hw-3',
                 'hw-4',
                 'hw-5',
                 'hw-6']
    
    for homework in homeworks:
        Homework(homework,
                 random.choice(Room.rooms),
                 homework) #reuse name as description

    students = ['Frankie Freshman',
                'Joe Junior',
                'Sophie Sophomore',
                'Cedric Senior']

    for student in students:
        NPC(student,
            random.choice(Room.rooms),
            random.randint(1,5),
            random.randint(1,5),
            student) #reuse name as description

    trolls = ['Polyphemus',
              'Gollum']

    for troll in trolls:
      Troll(troll,
            # random.choice(Room.rooms),
            oval,
            random.randint(1,3),
            random.randint(1,3),
            troll) #reuse name as description


VERBS = {
    'quit' : Quit(),
    'look' : Look(),
    'peek' : Peek(),
    'wait' : Wait(),
    'take' : Take(),
    'drop' : Drop(),
    'give' : Give(),
    'god'  : God(),
    'use'  : Use(),
    'north' : Direction('north'),
    'south' : Direction('south'),
    'east' : Direction('east'),
    'west' : Direction('west'),
    'up'   : Direction('up'),
    'down' : Direction('down')
}
  

def print_tick_action (t):
    Player.me.location().report('The clock ticks '+str(t))


def read_player_input ():
    while True:
        response = raw_input('\nWhat is thy bidding? ')
        if len(response)>0:
            return response.split()


SAME_ROUND = 1
NEXT_ROUND = 2  
  
def main ():
    
    print 'Olinland, version 1.4 (Fall 2014)\n'

    # Create the world
    create_world()
    Player.me.look_around()
    Player.me.clock.register(0,print_tick_action)
    for i in range(len(NPC.npcs)):
        Player.me.clock.register(1,NPC.npcs[i].move_and_take_stuff)
    for i in range(len(Professor.faculty)):
        Player.me.clock.register(2,Professor.faculty[i].lecture)
    for i in range(len(Troll.trolls)):
        Player.me.clock.register(3,Troll.trolls[i].eat_people)


    while True:
        response = read_player_input ()
        print
        if response[0] in VERBS:
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                Player.me.clock.tick()
                Player.me.look_around()
        else:
            print 'What??'
            

if __name__ == '__main__':
    main()
