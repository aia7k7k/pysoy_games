#!/usr/bin/env python3

import soy
from time import sleep
from math import sqrt

room = soy.scenes.Room(soy.atoms.Size((18.0,18.0,10.0)))
room['cam'] = soy.bodies.Camera(soy.atoms.Position((0, 0, 20)))
room['light'] = soy.bodies.Light(soy.atoms.Position((-5, 5, 8)))

client = soy.Client()
client.window.append(soy.widgets.Projector(room['cam']))

firebrick = soy.atoms.Color('firebrick')
goldenrod = soy.atoms.Color('goldenrod')

cubemap = soy.textures.Cubemap("checkered",
                               [firebrick, goldenrod], 1,2,3)

#fields
gravity = soy.fields.Accelerate(soy.atoms.Vector((0,-9.8,0)))

buoyancy = soy.fields.Buoyancy(gravity)
buoyancy.addRegion(-9,9,-100,0,-100,100) # defining region
buoyancy.density = 1                   # density of the fluid

wind = soy.fields.Wind(.2,soy.atoms.Vector((0,0,0)))  #wind providing viscuos force
wind.addRegion(-9,9,0,100,-100,100)                   #adding region

#adding fields to the scene
room.addField('buoyancy',buoyancy)
room.addField('gravity',gravity)
room.addField('wind',wind)

room['liquid'] = soy.bodies.Box(soy.atoms.Position((0, -5, 7)),
                               material=soy.materials.Colored('blue'))
room['liquid'].size = soy.atoms.Size((20, 10, 4))
room['liquid'].toggleField();

room['cylinder'] = soy.bodies.Cylinder()
room['cylinder'].position = soy.atoms.Position((-3,6,0))
room['cylinder'].length =3
room['cylinder'].density = .8
room['cylinder'].rotation = soy.atoms.Rotation((1,81,1))
room['cylinder'].addTorque(0,0,0)


room['sphere'] = soy.bodies.Sphere()
room['sphere'].material = soy.materials.Colored('cornflowerblue')
room['sphere'].radius = 1
room['sphere'].density = .9
room['sphere'].position  = soy.atoms.Position((7,3,0))


room['cube3'] = soy.bodies.Box(soy.atoms.Position((3, -0.25, 0)),
                               material=soy.materials.Textured())
room['cube3'].material.colormap = cubemap
room['cube3'].addForce(0, 0, 0)
room['cube3'].rotation = soy.atoms.Rotation((1,2,0))
room['cube3'].size = soy.atoms.Size((1.5, 1.5, 1.5))
room['cube3'].position = soy.atoms.Position((-7,7,0))
room['cube3'].radius = 0.1
room['cube3'].density = .7

m1 = soy.materials.Colored("red")
m2 = soy.materials.Colored("green")
m3 = soy.materials.Colored("blue")
m4 = soy.materials.Colored("yellow")

a = 1/sqrt(3)
b = sqrt(2/3)
z = 1/sqrt(2)

v1 = soy.atoms.Vertex(soy.atoms.Position((1,0,-z)),soy.atoms.Vector((a,0,b)),
                      soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
v2 = soy.atoms.Vertex(soy.atoms.Position((0,1,z)),soy.atoms.Vector((a,0,b)),
                      soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
v3 = soy.atoms.Vertex(soy.atoms.Position((0,-1,z)),soy.atoms.Vector((a,0,b)),
                      soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))

v4 = soy.atoms.Vertex(soy.atoms.Position((-1,0,-z)),soy.atoms.Vector((-a,0,b)),
                      soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
v5 = soy.atoms.Vertex(soy.atoms.Position((0,-1,z)),soy.atoms.Vector((-a,0,b)),
                      soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
v6 = soy.atoms.Vertex(soy.atoms.Position((0,1,z)),soy.atoms.Vector((-a,0,b)),
                      soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))

v7 = soy.atoms.Vertex(soy.atoms.Position((1,0,-z)),soy.atoms.Vector((0,a,-b)),
                      soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
v8 = soy.atoms.Vertex(soy.atoms.Position((-1,0,-z)),soy.atoms.Vector((0,a,-b)),
                      soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
v9 = soy.atoms.Vertex(soy.atoms.Position((0,1,z)),soy.atoms.Vector((0,a,-b)),
                      soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))

v10 = soy.atoms.Vertex(soy.atoms.Position((1,0,-z)),soy.atoms.Vector((0,-a,-b)),
                       soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
v11 = soy.atoms.Vertex(soy.atoms.Position((0,-1,z)),soy.atoms.Vector((0,-a,-b)),
                       soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
v12 = soy.atoms.Vertex(soy.atoms.Position((-1,0,-z)),soy.atoms.Vector((0,-a,-b))
                      ,soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))

f1 = soy.atoms.Face(v1,v2,v3,m1)
f2 = soy.atoms.Face(v4,v5,v6,m2)
f3 = soy.atoms.Face(v7,v8,v9,m3)
f4 = soy.atoms.Face(v10,v11,v12,m4)

room['mesh'] = soy.bodies.Mesh()
room['mesh'].append(f1)
room['mesh'].append(f2)
room['mesh'].append(f3)
room['mesh'].append(f4)

room['mesh'].density = .7
room['mesh'].position = soy.atoms.Position((0.5,7,0))
room['mesh'].rotation = soy.atoms.Rotation((2,2,2))

if __name__ == '__main__':
    while client:
        sleep(.1)
