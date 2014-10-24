README
Tom Chen
Jack Fan

As far as we know, the game is bug free (hopefully you won't prove us wrong).
One quirk is that if multiple items with the same name are present and you only posess some of them, the game will look at the ones you dont have first (preventing you from giving, for example).

Tom: I really enjoyed the project and the framework looks helpful if I wanted to write my own adventure games.
Jack: I thought it was a good project overall and really helpful to my understanding of object-oriented programming.

Part 3 extension:
We added a quest (new class, object like clock) which enables itself three rounds into the game.
The quest instructions will update themselves as you complete objectives.
You may have to wait or move a round to update the quest if you complete multiple objectives simultaneously.
You must find Harry-Potter, the troll hunter, and be in the room with him at the start of the round. 
You must then find a weapon (new class derived from mobilething) to fight trolls with.
You can attack surrounding trolls with 'use [WEAPON]'.
Once you have the weapon, you must kill trolls until they drop certain items, then hand them in to the wizard Dumbledore (new class similar to professor).
If you hand in all the troll items, it's an alternative way to win the game.

We also tweaked the behavior of NPCs to be less restless (so you can catch up to them) and gave more health to all persons (player, NPCs, trolls) since we added several more trolls to the game.