import soy
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

#Texture Import
wood = soy.textures.Texture('./images/wood.jpg')
brick = soy.textures.Texture('./images/brick.jpeg')
concrete = soy.textures.Texture('./images/concrete.jpeg')

#Cube Setup
room1['cube1'] = soy.bodies.Box(soy.atoms.Position((-1, 1, -1)))
room1['cube1'].radius = 0.1
room1['cube1'].material = soy.materials.Textured(colormap = wood)
room1['cube1'].addForce(0, 160, 160)

room1['cube2'] = soy.bodies.Box(soy.atoms.Position((1, -1, 1)))
room1['cube2'].radius = 0.1
room1['cube2'].material = soy.materials.Textured(colormap = brick)
room1['cube2'].addForce(160, 0, 160)

room1['cube3'] = soy.bodies.Box(soy.atoms.Position((-1, 1, 1)))
room1['cube3'].radius = 0.1
room1['cube3'].material = soy.materials.Textured(colormap = concrete)
room1['cube3'].addForce(160, 160, 0)

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

# Actions (applies a force on camera)
move_right = soy.actions.Thrust(room1['cam'], force_right)
move_left = soy.actions.Thrust(room1['cam'], force_left)
move_forward = soy.actions.Thrust(room1['cam'],force_forward)
move_backward = soy.actions.Thrust(room1['cam'], force_backward)

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
