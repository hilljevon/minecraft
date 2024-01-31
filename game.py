from ursina import *
# pre defined class to create first person character
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/punch_sound', loop = False, autoplay = False)
block_pick = 1


def update():
    global block_pick
    if held_keys['1']:block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['z']:
        if person.gravity:
            person.gravity = False
        else:
            person.gravity = True
    if held_keys['space']:
        person.jump
    # we use left mouse instead of left mouse down when inside the update function
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else: 
        hand.passive()

# class for creating new blocks via user click inoput
class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            # block created in blender
            model = 'assets/block',
            # height in 3d space of our cube
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9, 1)),
            scale = 0.5
                         )
    # if we are hoved over the specific voxel button
    def input(self, key):
        if self.hovered:
            
            # we need to check if the left click is being pressed
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture=brick_texture)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture=dirt_texture)
            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True 
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            # camera ui is 2d space of our camera; user viewport
            parent = camera.ui,
            model = 'assets/arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.6)
        )
    def active(self):
        self.position = Vec2(0.3, -0.5)
    def passive(self):
        self.position = Vec2(0.4, -0.6)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x, 0, z))
person = FirstPersonController()
person.cursor.color = color.white
person.cursor.model = 'sphere'
person.cursor.scale = 0.00015
sky = Sky()
hand = Hand()
app.run()
