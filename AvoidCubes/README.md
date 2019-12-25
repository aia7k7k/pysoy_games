# AvoidCubes
### Game Idea
The idea behind this game is very simple. The goal is to try to avoid being hit by the cubes that are flying around.
### Controls
WASD to move.
### Current Stage
Right now, most of the basic features have been implemented, but they all need improvement. For movement, the ability to move up and down, and to look around as well. For the cubes, in the future their movements will be randomized. Also, the ability to detect collision need to be added, to determine if the player has failed or not.
### Difficulties with development
One of the major challenges was that, when the player controls an object (cube, camera, etc.) to touch another rigid body, the object will be applied a constant force going in the opposite direction. The problem is that this force doesn't stop until the object touches another rigid body, therefore the player will lose control of the object. I believe this is caused by some collision mechanism in PySoy. 

I had trouble trying to use Cubemap. I tried to assign a Cubemap as the colormap of a material of a cube, however the result was that the cube was rendered completly black for some reason. 

I also had some trouble trying to use Bumpmap. I couldn't get sufficient information from help() to allow me to use it properly. I tried to assign some textures to Bumpmap, but there seems to be no effect on the cube. 



