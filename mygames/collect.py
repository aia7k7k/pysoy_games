import soy
from time import sleep

client = soy.Client()
room = soy.scenes.Room(soy.atoms.Size((20.0,10.0,30.0)))
room.material = soy.materials.Colored('yellow')
room['cam'] = soy.bodies.Camera()
client.window.append(soy.widgets.Projector(room['cam']))

room['light1'] = soy.bodies.Light((-9,5,-3))
room['light2'] = soy.bodies.Light((9,6,-3))

soy.events.KeyPress.init()
soy.events.KeyRelease.init()
soy.events.Motion.init()

#Force Values (determines how fast you will go in the direction)
Lforce = soy.atoms.Vector((-100,0,0))
Rforce = soy.atoms.Vector((100,0,0))
Fforce = soy.atoms.Vector((0,0,-100))
Bforce = soy.atoms.Vector((0,0,100))
UForce = soy.atoms.Vector((0,100,0))
DForce = soy.atoms.Vector((0,-100,0))

#applies the force values onto the camera
RT = soy.actions.Thrust(room['cam'], Rforce)
LT = soy.actions.Thrust(room['cam'], Lforce)
FT = soy.actions.Thrust(room['cam'], Fforce)
BT = soy.actions.Thrust(room['cam'], Bforce)
UT = soy.actions.Thrust(room['cam'], UForce)
DT = soy.actions.Thrust(room['cam'], DForce)

#action events
soy.events.KeyPress.addAction("D", RT)
soy.events.KeyRelease.addAction("D", LT)
soy.events.KeyPress.addAction("A", LT)
soy.events.KeyRelease.addAction("A", RT)
soy.events.KeyPress.addAction("W", FT)
soy.events.KeyRelease.addAction("W", BT)
soy.events.KeyPress.addAction("S", BT)
soy.events.KeyRelease.addAction("S", FT)
soy.events.KeyPress.addAction("O", UT)
soy.events.KeyRelease.addAction("O", DT)
soy.events.KeyPress.addAction("L", DT)
soy.events.KeyRelease.addAction("L", UT)

grav = soy.fields.Accelerate(soy.atoms.Vector((0,-9.8,0)))
room.addField('key', grav)


room['cube1'] = soy.bodies.Box(soy.atoms.Position((1,0.2,1)))
room['cube1'].material = soy.materials.Colored('blue')

'''cube_x = cube_pos[0]
cube_y = cube_pos[1]
cube_z = cube_pos[2]

cube_y = cube_y+1
cube_z = cube_z+2

room['cam'].position.x = cube_x
room['cam'].position.y = cube_y
room['cam'].position.z = cube_z'''

while True:

    cube_pos = room['cube1'].position
    cube_x = cube_pos[0]
    cube_y = cube_pos[1]
    cube_z = cube_pos[2]

    cube_y = cube_y+2
    cube_z = cube_z+4

    room['cam'].position.x = cube_x
    room['cam'].position.y = cube_y
    room['cam'].position.z = cube_z

    room['cube1'].addForce(0, 0, 0.1)

if __name__ == '__main__':
    while client:
        sleep(.1)
