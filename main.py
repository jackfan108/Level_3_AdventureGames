
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
from clock import *
from weapon import *
from caterpillar import *
from butterfly import *
from quest import *
from dumbledore import *

REVERSE = {
    'north' : 'south',
    'east' : 'west',
    'south' : 'north',
    'west' : 'east',
    'up' : 'down',
    'down' : 'up'
}

# start the clock
Clock(0)

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
    Weapon('trinity force', cscar, 2000, 'You throw the mighty trinity force!','tons of damage')
    Weapon('baseball bat', easth, 1, 'Bonk!','A Louisville Slugger')
    MobileThing('prox card', oval, 'Reads, \'Riccardo Pucella\'.')
    MobileThing('poro', endw, 'it\'s so fluffy!')
    Caterpillar('caterpillar', oval, 'it\'s a big fat worm')

    Computer('hal-9000', ac113, 'sinister')
    Computer('johnny-5', easth, 'boop boop beep')

    Professor('Riccardo',mh353,random.randint(2,5),2,'Scary!')
    Wizard('Dumbledore', endw, random.randint(2,5),2,'Very very old......')
    Badninja('Shredder',random.choice(Room.rooms), random.randint(2,5),'Even scarier than Riccardo!')
    Trollhunter('Harry Potter', random.choice(Room.rooms), random.randint(2,5), 'You can tell he dislikes trolls right away')

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
            random.randint(2,5),
            random.randint(2,5),
            student) #reuse name as description

    trolls = ['Polyphemus',
              'Gollum',
              'Krug',
              'Elder Lizard Troll',
              'Ancient Golem Troll',
              'Super Troll',
              'God Troll',
              'Umbridge']

    for troll in trolls:
      Troll(troll,
            # random.choice(Room.rooms),
            random.choice(Room.rooms),
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
    'down' : Direction('down'),
    'quest' : PrintQuest()
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
    Clock.clocks[0].register(0,print_tick_action,0)
    Quest('Troll Hunting', 'Maybe you will get a quest soon?')
    while True:
        response = read_player_input ()
        print
        if response[0] in VERBS:
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                Clock.clocks[0].tick()
                Player.me.look_around()
        else:
            print 'What??'
        if Clock.clocks[0]._current == 3:
            Quest.quests[0]._instruction = 'Go find Harry Potter, the troll hunter for further instructions :D'
            print Quest.quests[0]._instruction
            Clock.clocks[0].register(4,Quest.quests[0].TrollHunterInRoom,Quest.quests[0]._id)

if __name__ == '__main__':
    main()
