import soy
from time import sleep
import time
from random import randint
import pymouse
#from PyUserInput import pymouse, pykeyboard
#import pyuserinput
#Tasks
# 1. jump
# 2. camera foll
# 3. menu


class MainGame():

    def __init__(self):

        self.load_client()
        self.menu()
        self.load_scene()
        self.load_player()
        self.load_mouse()
        self.load_camera()
        self.load_gameobject()
        self.load_keyboard()

    def start(self):
        while self.client.window:
            self.update_mouse()
            self.update_camera()
            self.room['player_cam'].rotation = soy.atoms.Rotation((0,0,0))
            self.room['player_cam'].position = soy.atoms.Position((0,-5.5,2))

            #self.room['player_cam'].position = soy.atoms.Position((0, 0, count))

    def load_client(self):

        self.client = soy.Client()
        self.client.window.title = "Avoid Cubes V3"

    def load_scene(self):

        self.room = soy.scenes.Room(soy.atoms.Size((20.0,20.0,20.0)),1.0,0.0,0.0,0.0)
        self.room.material = soy.materials.Colored('yellow')
        self.room['light_L1'] = soy.bodies.Light((-9, 4, -9.5))
        self.room['light_R1'] = soy.bodies.Light((9, 4, -9.5))

        self.room['light_L2'] = soy.bodies.Light((-9, 4, 9.5))
        self.room['light_R2'] = soy.bodies.Light((9, 4, 9.5))

        self.gravity = soy.fields.Accelerate(soy.atoms.Vector((0,-9.8,0)))
        self.room.addField('gravity', self.gravity)

    def load_gameobject(self):

        self.wood = soy.textures.Texture('./images/wood.jpg')
        self.room['wood1'] = soy.bodies.Box(soy.atoms.Position((2, -5.5, 0)))
        self.room['wood1'].radius = 0.1
        self.room['wood1'].material = soy.materials.Textured(colormap = self.wood)
        self.room['wood1'].addForce(30,0,50)

    def load_player(self):

        player = soy.textures.Texture('./images/player.png')
        self.room['player'] = soy.bodies.Box(soy.atoms.Position((0, -5.5, 2)))
        self.room['player'].radius = 0.1
        self.room['player'].material = soy.materials.Textured(colormap = player)
        self.room['player'].density = 0.1
        self.player_x = 0
        self.player_y = 0
        self.player_z = 0


    def load_camera(self):

        self.room['player_cam'] = soy.bodies.Camera((0,0,0),5)

        self.client.window.append(soy.widgets.Projector(self.room['player_cam']))
        self.room['player_cam'].rotation = soy.atoms.Rotation((0,0,0))
        self.room['player_cam'].position = soy.atoms.Position((0,-5.5,2))

        self.room['vplayer'] = soy.bodies.Box(soy.atoms.Position((0, -5.5, -4)))
        self.room['vplayer'].radius = 0.1
        self.room['vplayer'].material = soy.materials.Colored('green')
        self.room['vplayer'].density = 0.1
        self.room['vplayer'].toggleField()




    def load_keyboard(self):

        soy.events.KeyPress.init()
        soy.events.KeyRelease.init()
        soy.events.Motion.init()

        force_right = soy.atoms.Vector((20, 0, 0))
        force_left = soy.atoms.Vector((-20, 0, 0))
        force_forward = soy.atoms.Vector((0, 0, -20))
        force_backward = soy.atoms.Vector((0, 0, 20))
        force_downward = soy.atoms.Vector((0, -50, 0))
        force_upward = soy.atoms.Vector((0, 50, 0))
        rotate_right = soy.atoms.Vector((0, -50, 0))
        rotate_left = soy.atoms.Vector((0, 50, 0))

        self.move_right = soy.actions.Thrust(self.room['player'], force_right)
        self.move_left = soy.actions.Thrust(self.room['player'], force_left)
        self.move_forward = soy.actions.Thrust(self.room['player'],force_forward)
        self.move_backward = soy.actions.Thrust(self.room['player'], force_backward)
        self.jump = soy.actions.Thrust(self.room['player'], force_upward)
        self.fall = soy.actions.Thrust(self.room['player'], force_downward)


        # Events (calls an action on KeyPress/KeyRelease
        soy.events.KeyPress.addAction("D", self.move_right)
        soy.events.KeyRelease.addAction("D", self.move_left)
        soy.events.KeyPress.addAction("A", self.move_left)
        soy.events.KeyRelease.addAction("A", self.move_right)
        soy.events.KeyPress.addAction("W", self.move_forward)
        soy.events.KeyRelease.addAction("W", self.move_backward)
        soy.events.KeyPress.addAction("S", self.move_backward)
        soy.events.KeyRelease.addAction("S", self.move_forward)

        soy.events.KeyPress.addAction("X", self.jump)
        soy.events.KeyRelease.addAction("X", self.fall)

    def update_camera(self):

        self.player_pos = self.room['player'].position
        self.pos_difference = (abs(self.player_x - self.player_pos[0]) +
                               abs(self.player_x - self.player_pos[1]) +
                               abs(self.player_x - self.player_pos[2]))
        if self.pos_difference <= 5:
            return
        else:
            self.player_x = self.player_pos[0]
            self.player_y = self.player_pos[1] + 5
            self.player_z = self.player_pos[2]
            #self.room['player_cam'].position.x = self.player_x
            #self.room['player_cam'].position.y = self.player_y
            #self.room['player_cam'].position.z = self.player_z
            ##self.room['player_cam'].rotation.y = self.room['player_cam'].rotation.y + (-self.mouse_x/1000)
            #self.room['player_cam'].rotation.x = self.room['player_cam'].rotation.x + (self.mouse_y/1000)
            #self.room['player'].rotation.y = self.room['player'].rotation.y + (-self.mouse_x/1000)
            #self.room['player_cam'].rotation.y = self.room['player'].rotation.y


            #self.room['vplayer'].position.x = self.player_x
            #self.room['vplayer'].position.y = self.player_y
            #self.room['vplayer'].position.z = self.player_z
            self.room['vplayer'].rotation.y = self.room['vplayer'].rotation.y + (-self.mouse_x/1000)
            self.room['vplayer'].rotation.x = self.room['vplayer'].rotation.x + (self.mouse_y/1000)

    def load_mouse(self):

        self.mouse = pymouse.PyMouse()
        self.mouse.move(550,350)
        self.mouse_pos = self.mouse.position()

    def update_mouse(self):

        self.mouse_x = self.mouse.position()[0] - self.mouse_pos[0]
        self.mouse_y = self.mouse_pos[1] - self.mouse.position()[1]
        print(str(self.mouse_x) + ' ' + str(self.mouse_y))
        #self.mouse.move(550,350)
        self.mouse_pos = self.mouse.position()

    def menu(self):

        self.title = soy.textures.Texture('./images/title.jpeg')
        self.canvas = soy.widgets.Canvas(self.title)
        self.canvas.keep_aspect = True
        self.client.window.append(self.canvas)
        sleep(2)

if __name__ == '__main__':

        game = MainGame()
        game.start()
