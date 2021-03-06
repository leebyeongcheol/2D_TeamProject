from pico2d import *
import game_framework
import title_state
import random


class Mario:
    image = None
    Jump_size = 150

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, UP_JUMP, DOWN = 0, 1, 2, 3, 5, 4,

    def __init__(self):
        self.x, self.y = 100, 82
        self.frame = random.randint(0, 7)
        self.dir = 1
        self.state = self.RIGHT_STAND
        self.run_frames = 0
        self.stand_frames = 0
        if Mario.image == None:
            self.image = load_image('animation_sheet1.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

        if(self.state != self.UP_JUMP):
            if self.state == self.RIGHT_RUN:
                self.x = min(800, self.x + 5)
                if (self.x >= 600 - 50 and self.x <= 600 + 50) and (self.y >= 0 and self.y <= 200):
                    self.x -= 5
                else:
                    self.x += 5
            elif self.state == self.LEFT_RUN:
                self.x = max(0, self.x - 5)
                if (self.x >= 600 - 50 and self.x <= 600 + 50) and (self.y >= 0 and self.y <= 200):
                    self.x += 5
                else:
                    self.x -= 5
        elif self.state == self.UP_JUMP:
            if self.y < 82 + self.Jump_size:
                    self.y += 150
            elif self.y >= 82 +self.Jump_size:
                 for i in range(self.Jump_size):
                    self.y -= 1
                    #self.x += 10/self.Jump_size
                 if self.y == 82:
                     self.y = 82
                     self.state = self.RIGHT_STAND

        delay(0.03)

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def set_background(self, bg):
        self.bg = bg

class BackGround:
    def __init__(self):
        self.image = load_image("background.png")
    def draw(self):
        self.image.draw(400,300)

def enter():
    global mario, grass, object, background
    mario = Mario()
    background = BackGround()


def exit():
    global mario, grass, object, background
    del(mario)
    del(background)


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                mario.state = mario.LEFT_RUN
            if event.key == SDLK_RIGHT:
                mario.state = mario.RIGHT_RUN
            if event.key == SDLK_UP:
                mario.state = mario.UP_JUMP
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
    mario.draw()
    update_canvas()



