from pico2d import *
import game_framework
import title_state
import random

class Mario:
    image = None
    global object_X

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND= 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 100, 84
        self.frame = random.randint(0, 7)
        self.dir = 1
        self.state = self.RIGHT_STAND
        self.run_frames = 0
        self.stand_frames = 0

        if Mario.image == None:
            self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
     #   self.handle_state[self.state](self)
        if self.state == self.RIGHT_RUN:
            self.x = min(800, self.x + 5)
            if (self.x >= 600-50 and self.x <= 600+50) and (self.y>=0 and self.y <= 114):
                self.x -=5
            else:
                self.x +=5
        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x -5)
            if (self.x >= 600 - 50 and self.x <= 600 + 50) and (self.y >= 0 and self.y <= 114):
                self.x += 5
            else:
                self.x -= 5
        delay(0.03)

   #def handle_left_run(self):
   #    self.x -= 5
   #    self.run_frames += 1
   #    if self.x < 0:
   #        self.state = self.RIGHT_RUN
   #        self.x = 0
   #    if self.run_frames == 100:
   #        self.state = self.LEFT_STAND
   #        self.stand_frames = 0

   #def handle_left_stand(self):
   #    self.stand_frames += 1
   #    if self.stand_frames == 50:
   #        self.state = self.LEFT_RUN
   #        self.run_frames = 0

   #def handle_right_run(self):
   #    self.x += 5
   #    self.run_frames += 1
   #    if self.x > 800:
   #        self.state = self.LEFT_RUN
   #        self.x = 800
   #    if self.run_frames == 100:
   #        self.state = self.RIGHT_STAND
   #        self.stand_frames = 0

   #def handle_right_stand(self):
   #    self.stand_frames += 1
   #    if self.stand_frames == 50:
   #        self.state = self.RIGHT_RUN
   #        self.run_frames = 0
#
   #handle_state = {
   #    LEFT_RUN: handle_left_run,
   #    RIGHT_RUN: handle_right_run,
   #    LEFT_STAND: handle_left_stand,
   #    RIGHT_STAND: handle_right_stand
   #}

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

class BackGroung:
    def __init__(self):
        self.image = load_image("background.png")
    def draw(self):
        self.image.draw(400,300)
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 26)

class Object:
    def __init__(self):
        self.Lpipe = load_image('object_LongPipe.png')
        self.cloud = load_image('cloud.png')
    def draw(self):
        object_X = 600
        self.Lpipe.draw(object_X,114)
        self.cloud.draw(700,400)
        self.cloud.draw(400,550)

#class Trap:
#    global trap_X
#    def __init__(self):
#        self.cloud_trap = load_image("cloud.png")
#        self.trap_X = 200
#    def draw(self):
#        self.cloud.draw(trap_X,350)
#    def update(self):
#        if()

def enter():
    global mario, grass, object,background
    mario = Mario()
    grass = Grass()
    object = Object()
    background = BackGroung()


def exit():
    global mario, grass, object,background
    del(mario)
    del(grass)
    del(object)
    del(background)


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_MOUSEMOTION :
            mousex, mousey = event.x, 600 - event.y
       # elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                mario.state = mario.LEFT_RUN
            if event.key == SDLK_RIGHT:
                mario.state = mario.RIGHT_RUN
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                mario.state = mario.LEFT_STAND
            if event.key == SDLK_RIGHT:
                mario.state = mario.RIGHT_STAND

def update():
    mario.update()

def draw():
    clear_canvas()
    background.draw()
    grass.draw()
    mario.draw()
    object.draw()
    update_canvas()


