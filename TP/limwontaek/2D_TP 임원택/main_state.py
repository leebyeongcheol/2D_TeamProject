from pico2d import *
import game_framework
import title_state
import random

#파이프 X,Y값
object_Lpipe_X = 600
object_Lpipe_Y = 114
object_Lpipe_size = 50

class Mario:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, UP_RUN, UP_STAND= 0, 1, 2, 3, 4, 5

    def __init__(self):
        self.x, self.y = 100, 84
        self.frame = random.randint(0, 7)
        self.dir = 1
        self.state = self.RIGHT_STAND
        self.run_frames = 0
        self.stand_frames = 0
        self.jump_frames = 0
        self.jump_size = 50

        if Mario.image == None:
            self.image = load_image('animation_sheet.png')

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.LEFT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND
        elif event.key == SDLK_UP:
           self.state = self.UP_RUN

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0
    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.LEFT_RUN
            self.run_frames = 0
    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0
    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames = 0
    def handle_up_run(self):
        self.y += 5

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand,
        UP_RUN: handle_up_run,
    }


    def update(self):
        self.frame = (self.frame + 1) % 8
        # 오른쪽이동
        if self.state == self.RIGHT_RUN:
            self.x = min(800, self.x + 5)
            if (self.x >= object_Lpipe_X-object_Lpipe_size and self.x <= object_Lpipe_X+object_Lpipe_size) \
                    and (self.y>=0 and self.y <= object_Lpipe_Y):
                self.x -=5
            else:
                self.x +=5
        # 왼쪽이동
        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x -5)
            if (self.x >= object_Lpipe_X-object_Lpipe_size and self.x <= object_Lpipe_X + object_Lpipe_size) \
                    and (self.y >= 0 and self.y <= object_Lpipe_Y):
                self.x += 5
            else:
                self.x -= 5
        # 점프
        if self.y < 82 + self.Jump_size:
            self.y += 150
        elif self.y >= 82 + self.Jump_size:
            for i in range(self.Jump_size):
                self.y -= 1
            if self.y == 82:
                self.y = 82
                self.state = self.RIGHT_STAND

        delay(0.03)

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
        self.Lpipe.draw(object_Lpipe_X,object_Lpipe_Y)
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
        else:
            mario.handle_event(event)

def update():
    mario.update()

def draw():
    clear_canvas()
    background.draw()
    grass.draw()
    mario.draw()
    object.draw()
    update_canvas()


