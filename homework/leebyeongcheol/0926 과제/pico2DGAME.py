import  random
from pico2d import *

def handle_events():
    global running
    global mouseX
    global mouseY
    global boyNum

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_0:
                boyNum = 0
            elif event.key == SDLK_1:
                boyNum = 1
            elif event.key == SDLK_2:
                boyNum = 2
            elif event.key == SDLK_3:
                boyNum = 3
            elif event.key == SDLK_4:
                boyNum = 4
            elif event.key == SDLK_5:
                boyNum = 5
            elif event.key == SDLK_6:
                boyNum = 6
            elif event.key == SDLK_7:
                boyNum = 7
            elif event.key == SDLK_8:
                boyNum = 8
            elif event.key == SDLK_9:
                boyNum = 9
            elif event.key == SDLK_a:
                boyNum = 10
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEMOTION:
            mouseX = event.x
            mouseY = 600 - event.y

class Grass:
    def __init__(self):
        self.image= load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 2

    def mouse_update(self):
        self.frame = (self.frame + 1) % 8
        if self.x > mouseX:
            self.x -= 2
        else:
            self.x += 2
        if self.y > mouseY:
            self.y -= 2
        else:
            self.y += 2

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

open_canvas()

team = [Boy() for i in range(11)]
grass = Grass()
running = True

mouseX = 0
mouseY = 0
boyNum = 0

while running:

    handle_events()
    clear_canvas()
    grass.draw()
    for i in range(11):
        if i != boyNum:
            team[i].update()
        else:
            team[i].mouse_update()

    for boy in team:
        boy.update()
        boy.draw()

    update_canvas()

    delay(0.05)

close_canvas()
