import random
from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    global mousex, mousey

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
             if event.key == SDLK_F1:
                 team[1].x = mousex
                 team[1].y = mousey
             elif event.key == SDLK_F2:
                 team[2].x = mousex
                 team[2].y = mousey
             elif event.key == SDLK_F3:
                 team[3].x = mousex
                 team[3].y = mousey
             elif event.key == SDLK_F4:
                 team[4].x = mousex
                 team[4].y = mousey
             elif event.key == SDLK_F5:
                 team[5].x = mousex
                 team[5].y = mousey
             elif event.key == SDLK_F6:
                 team[6].x = mousex
                 team[6].y = mousey
             elif event.key == SDLK_F7:
                 team[7].x = mousex
                 team[7].y = mousey
             elif event.key == SDLK_F8:
                 team[8].x = mousex
                 team[8].y = mousey
             elif event.key == SDLK_F9:
                 team[9].x = mousex
                 team[9].y = mousey
             elif event.key == SDLK_F10:
                 team[10].x = mousex
                 team[10].y = mousey
             elif event.key == SDLK_F11:
                 team[0].x = mousex
                 team[0].y = mousey
        elif event.type == SDL_MOUSEMOTION:
            mousex, mousey = event.x, 600 - event.y


open_canvas()

grass = Grass()
team = [Boy() for i in range(11)]

running =True

while running:
    handle_events()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.update()
        boy.draw()
    update_canvas()

    delay(0.05)

close_canvas()