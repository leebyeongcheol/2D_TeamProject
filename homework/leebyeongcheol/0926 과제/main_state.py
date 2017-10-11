from pico2d import *
import title_state
import game_framework
import random

class Grass:
    def __init__(self):
        self.image= load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.imang=load_image(('run_animation.png'))
        if Boy.image == None:
            Boy.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 2

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()

def exit():
    global boy, grass
    del(boy)
    del(grass)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:\
            game_framework.change_state(title_state)

def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()