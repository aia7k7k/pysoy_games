#AvoidCubes
##Game Idea
The idea behind this game is very simple. The goal is to try to avoid being hit by the cubes that are flying around.
##Controls
WASD to move.
##Current Stage
Right now, most of the basic features have been implemented, but they all need improvement. For movement, the ability to move up and down, and to look around as well. For the cubes, in the future their movements will be randomized. 
##Difficulties with development
One of the major challenges was that, when the player controls an object (cube, camera, etc.) to touch another rigid body, the object will be applied a constant force going in the opposite direction. The problem is that this force doesn't stop until the object touches another rigid body, therefore the player will lose control of the object. I believe this is caused by some collision mechanism in PySoy. 



