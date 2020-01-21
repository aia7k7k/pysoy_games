import soy
from time import sleep
from random import randint

started = False
in_game = False
client = soy.Client()
room1 = soy.scenes.Room(soy.atoms.Size((20.0,10.0,40.0)),1.0,0.0,0.0,0.0)

def checkT(t1,t2):
        return sorted(t1) == sorted(t2)

def win_or_lose():
    global room1
    global in_game
    correct = (1.000000, 0.000000, 0.000000, 0.000000)
    rot = room1['player'].rotation
    print(rot)
    if checkT(rot, correct):
        print('all good')
    else:
        in_game = False
        #main()
        print('game restarted')
    #in_game = False


def game():

    global client
    global room1

    #-----Room Setup-----
    room1.material = soy.materials.Colored('green')
    room1['light'] = soy.bodies.Light((-9, 4, -9.5))
    room1['light2'] = soy.bodies.Light((9, 4, -9.5))

    camera = soy.bodies.Camera((0,1,15.5))
    room1['cam'] = camera
    room1['cam'].position = soy.atoms.Position((0,4,18))
    room1['cam'].rotation = soy.atoms.Rotation((0,0,0.25))
    client.window.append(soy.widgets.Projector(room1['cam']))

    #Texture Import
    wood = soy.textures.Texture('./images/wood.jpg')
    brick = soy.textures.Texture('./images/brick.jpeg')
    concrete = soy.textures.Texture('./images/concrete.jpeg')
    player = soy.textures.Texture('./images/player.png')

    #Cube Setup
    wood_pos = randint(-2, 0)
    room1['wood1'] = soy.bodies.Box(soy.atoms.Position((wood_pos, 0, wood_pos)))
    room1['wood1'].radius = 0.1
    room1['wood1'].material = soy.materials.Textured(colormap = wood)
    room1['wood2'] = soy.bodies.Box(soy.atoms.Position((0, wood_pos, wood_pos)))
    room1['wood2'].radius = 0.1
    room1['wood2'].material = soy.materials.Textured(colormap = wood)

    brick_pos = randint(-2, 0)
    room1['brick1'] = soy.bodies.Box(soy.atoms.Position((brick_pos, 2, brick_pos)))
    room1['brick1'].radius = 0.1
    room1['brick1'].material = soy.materials.Textured(colormap = brick)
    room1['brick2'] = soy.bodies.Box(soy.atoms.Position((brick_pos, brick_pos, -2)))
    room1['brick2'].radius = 0.1
    room1['brick2'].material = soy.materials.Textured(colormap = brick)

    concrete_pos = randint(-2, 0)
    room1['concrete1'] = soy.bodies.Box(soy.atoms.Position((1, concrete_pos, concrete_pos)))
    room1['concrete1'].radius = 0.1
    room1['concrete1'].material = soy.materials.Textured(colormap = concrete)
    room1['concrete2'] = soy.bodies.Box(soy.atoms.Position((concrete_pos, concrete_pos, -1)))
    room1['concrete2'].radius = 0.1
    room1['concrete2'].material = soy.materials.Textured(colormap = concrete)

    room1['player'] = soy.bodies.Box(soy.atoms.Position((0, 0, 12)))
    room1['player'].radius = 0.1
    room1['player'].material = soy.materials.Textured(colormap = player)

    sleep(5)

    room1['wood1'].addForce(randint(-500, 500),
                            randint(-500, 500),
                            randint(-500, 500))
    room1['wood2'].addForce(randint(-500, 500),
                            randint(-500, 500),
                            randint(-500, 500))
    room1['brick1'].addForce(randint(-300, 300),
                            randint(-300, 300),
                            randint(-300, 300))
    room1['brick2'].addForce(randint(-300, 300),
                            randint(-300, 300),
                            randint(-300, 300))
    room1['concrete1'].addForce(randint(-200, 200),
                            randint(-200, 200),
                            randint(-200, 200))
    room1['concrete2'].addForce(randint(-200, 200),
                            randint(-200, 200),
                            randint(-200, 200))

    #-----Reset-----
    room1['cam'].position = soy.atoms.Position((0,4,18))
    room1['cam'].rotation = soy.atoms.Rotation((0,0,0.25))
    room1['player'].position = soy.atoms.Position((0, 0, 12))
    room1['player'].rotation = soy.atoms.Rotation((0,0,0))


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
    rotate_right = soy.atoms.Vector((0, -50, 0))
    rotate_left = soy.atoms.Vector((0, 50, 0))


    # Actions (applies a force on camera)
    move_right = soy.actions.Thrust(room1['player'], force_right)
    move_left = soy.actions.Thrust(room1['player'], force_left)
    move_forward = soy.actions.Thrust(room1['player'],force_forward)
    move_backward = soy.actions.Thrust(room1['player'], force_backward)

    #look_forward = soy.actions.Thrust(room1['cam'],force_forward)
    #look_backward = soy.actions.Thrust(room1['cam'], force_backward)


    # Events (calls an action on KeyPress/KeyRelease
    soy.events.KeyPress.addAction("D", move_right)
    soy.events.KeyRelease.addAction("D", move_left)
    soy.events.KeyPress.addAction("A", move_left)
    soy.events.KeyRelease.addAction("A", move_right)
    soy.events.KeyPress.addAction("W", move_forward)
    soy.events.KeyRelease.addAction("W", move_backward)
    soy.events.KeyPress.addAction("S", move_backward)
    soy.events.KeyRelease.addAction("S", move_forward)

    #soy.events.KeyPress.addAction("W", look_forward)
    #soy.events.KeyRelease.addAction("W", look_backward)
    #soy.events.KeyPress.addAction("S", look_backward)
    #soy.events.KeyRelease.addAction("S", look_forward)

def menu():
    global in_game
    title = soy.textures.Texture('./images/title.jpeg')
    title.size = soy.atoms.Size((200,200))
    canvas = soy.widgets.Canvas(title)
    #projector = soy.widgets.Projector()
    client.window.append(canvas)
    sleep(2)
    in_game = True
    print('game started')




if __name__ == '__main__':
    while client.window:
        if in_game is True and started is False:
            started = True
            game()
        elif in_game is False:
            started = False
            menu()
        else:
            sleep(.1)
