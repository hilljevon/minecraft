from ursina import *
# pre defined class to create first person character
from ursina.prefabs.first_person_controller import FirstPersonController
class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            # height in 3d space of our cube
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.color(0,0,random.uniform(0.9, 1)),
            highlight_color = color.lime
                         )
    # if we are hoved over the specific voxel button
    def input(self, key):
        if self.hovered:
            # we need to check if the left click is being pressed
            if key == 'left mouse down':
                voxel = Voxel(position = self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)
app = Ursina()

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x, 0, z))
person = FirstPersonController()
person.cursor.color = color.white
person.cursor.scale = 0.00015
app.run()
