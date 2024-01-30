from ursina import *
from ursina import Default, camera
class Test_cube(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(
            add_to_scene_entities, 
            **kwargs,
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45, 45, 45)
            )
# WE USE A CLASS TO CREATE OUR BUTTONS. NOTE THAT WE HAVE TO INCLUDE ENTITY BUTTON IN THE ARGUMENT
class Test_button(Button):
    def __init__(self,):
        # OUR SUPER INIT IS GOING TO HAVE ALL THE BEGINNING PARAMETERS OF OUR BUTTON. SEE ARGUMENTS FOR HOW WE CAN CUSTOMIZE EVENTS
        super().__init__(
            parent=scene,
            model = 'cube',
            texture = 'brick',
            color = color.blue,
            highlight_color = color.red,
            pressed_color = color.green
        )
        # METHOD RECOGNIZES KEY AS THE KEY PRESSING THE BUTTON. THEN WE CAN SPECIFY THE KEY TYPE AND CARRY OUT PARTICULAR FUNCTIONS IF SO
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print('BUTTON PRESSED')
# WHEN DEFINING A FUNCTION ALONE, THAT FUNCTION CONTINUES TO RENDER THROUGHOUT EACH FRAME. THINK OF EACH DEFINED FUNCTION AS ALREADY BEING CALLED WITHIN THE INFINITE GAME WHILE LOOP
def update():
    if held_keys['a']:
        # time.dt represents the time between different frames. this will essentially increment our time to a really small number
        test_square.x -=4 * time.dt
    if held_keys['w']:
        test_square.y +=4 * time.dt

# RUNS OUR INTIAL GAME
app = Ursina()
# WE DEFINE NEW OBJECTS AS ENTITIES. HERE WE MAY DEFINE INIT PROPERTIES
test_square = Entity(model='quad', color = color.red, scale = (1,2), position = (1,1))
# WE CAN PRE DEFINE TEXTURES FOR CONSISTENCY AND READABILITY
sans_texture = load_texture('assets/Sans.png')
# QUAD IS OUR CUBE 
sans = Entity(model = 'quad', texture = sans_texture)

test_cube = Test_button()

app.run() 