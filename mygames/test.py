import soy
import random
from time import sleep


#-----Room Setup-----

room1 = soy.scenes.Room(soy.atoms.Size((20.0,10.0,40.0)),1.0,0.0,0.0,0.0)
room1.material = soy.materials.Colored('green')
room1['light'] = soy.bodies.Light((-9, 4, -9.5))
room1['light2'] = soy.bodies.Light((9, 4, -9.5))

camera = soy.bodies.Camera((0,1,15.5))
room1['cam'] = camera
room1['light'] = soy.bodies.Light(soy.atoms.Position((-2, 3, 5)))
client = soy.Client()
client.window.append(soy.widgets.Projector(room1['cam']))

#-----GameObject Setup-----
blue = soy.materials.Colored('blue')
gold = soy.materials.Colored('gold')
red = soy.materials.Colored('red')

room1['cube1'] = soy.bodies.Box(soy.atoms.Position((-1, 1, -1)), material=blue)
room1['cube1'].radius = 0.1
room1['cube1'].addForce(0, 80, 80)

room1['cube2'] = soy.bodies.Box(soy.atoms.Position((1, -1, 1)), material=gold)
room1['cube2'].radius = 0.1
room1['cube2'].addForce(80, 0, 80)

room1['cube3'] = soy.bodies.Box(soy.atoms.Position((-1, 1, 1)), material=red)
room1['cube3'].radius = 0.1
room1['cube3'].addForce(80, 80, 0)

#-----Movement Section -----

#Initialize
soy.events.KeyPress.init()
soy.events.KeyRelease.init()
soy.events.Motion.init()

#Forces
force_right = soy.atoms.Vector((200, 0, 0))
force_left = soy.atoms.Vector((-200, 0, 0))
force_forward = soy.atoms.Vector((0, 0, -200))
force_backward = soy.atoms.Vector((0, 0, 200))
force_up = soy.atoms.Vector((0, 200, 0))
force_down = soy.atoms.Vector((0, -200, 0))

# Actions (applies a force on camera)
move_right = soy.actions.Thrust(room1['cam'], force_right)
move_left = soy.actions.Thrust(room1['cam'], force_left)
move_forward = soy.actions.Thrust(room1['cam'],force_forward)
move_backward = soy.actions.Thrust(room1['cam'], force_backward)
move_up = soy.actions.Thrust(room1['cam'], force_up)
move_down = soy.actions.Thrust(room1['cam'], force_down)

# Events (calls an action on KeyPress/KeyRelease)
soy.events.KeyPress.addAction("D", move_right)
soy.events.KeyRelease.addAction("D", move_left)
soy.events.KeyPress.addAction("A", move_left)
soy.events.KeyRelease.addAction("A", move_right)
soy.events.KeyPress.addAction("W", move_forward)
soy.events.KeyRelease.addAction("W", move_backward)
soy.events.KeyPress.addAction("S", move_backward)
soy.events.KeyRelease.addAction("S", move_forward)


if __name__ == '__main__':
    while client:
        sleep(.1)
