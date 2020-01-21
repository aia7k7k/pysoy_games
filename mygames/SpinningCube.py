import soy

room = soy.scenes.Room(soy.atoms.Size((2,2,2)))



if __name__ == '__main__':
	from time import sleep
	client = soy.Client()
	client.window.background = soy.atoms.Color('white')
	client.window.title = "PySoy Primer Part 1"

	gold = soy.atoms.Color('gold')	
	firebrick = soy.atoms.Color('firebrick')
	cubemap = soy.textures.Cubemap("checkered", [gold, firebrick], 1,1,1)
	
	room['cube'] = soy.bodies.Box()
	room['cube'].position = soy.atoms.Position((-1,0,0))
	room['cube'].material = soy.materials.Textured()
	room['cube'].material.colormap = cubemap
	room['cube'].size = soy.atoms.Size((2,2,2))
	room['cube'].radius = 0.1
	
	room['cam'] = soy.bodies.Camera(soy.atoms.Position((0,0,15)))
	room['light'] = soy.bodies.Light(soy.atoms.Position((-2,3,5)))
	client.window.append(soy.widgets.Projector(room['cam']))
	
	cubemap2 = soy.textures.Cubemap("checkered")
	room['sphere'] = soy.bodies.Sphere()
	room['sphere'].radius = 1.0
	room['sphere'].position = soy.atoms.Position((1,0,0))
	room['sphere'].material = soy.materials.Textured()
	room['sphere'].material.colormap = cubemap2
	
	room['cube'].addTorque(1,1,1)
	room['sphere'].addTorque(1,1,1)
	room['cube'].addForce(1, 0, 0)
	room['sphere'].addForce(-1, 0, 0)

	while client.window :
		sleep(.1)

		
		



