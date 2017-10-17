from pico2d import *
import game_framework
import title_state
import random
import numbers

class Boy:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND= 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.dir = 1
        self.state = self.RIGHT_STAND
        self.run_frames = 0
        self.stand_frames = 0
        if Boy.image == None:
            self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
     #   self.handle_state[self.state](self)
        if self.state == self.RIGHT_RUN:
            self.x = min(800, self.x + 5)
            self.x += 5
        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x -5)
            self.x -= 5
        delay(0.002)

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





class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

global people

people = 11

def enter():
    global boy, grass
    boy = [Boy() for i in range(people)]
    grass = Grass()

def exit():
    global boy, grass
    del(boy)
    del(grass)

global boyindex


boyindex = 0

def handle_events():
    global mousex, mousey

    events = get_events()

    global boyindex
    global people


    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_MOUSEMOTION :
            mousex, mousey = event.x, 600 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:# and boyindex <= people - 1:
            boyindex += 1
            if boyindex >= 11:
                boyindex = 10
            boy[boyindex].x = mousex
            boy[boyindex].y = mousey

        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN and boyindex > -1 :
            boyindex -= 1
            boy[boyindex].x = mousex
            boy[boyindex].y = mousey
        #elif (event.type,event.key)==(SDL_KEYDOWN, SDLK_LEFT):
        #    if boy[boyindex].state in (boy[boyindex].RIGHT_STAND, boy[boyindex].LEFT_STAND):
        #        boy[boyindex].state = boy[boyindex].LEFT_RUN
        #elif (event.type,event.key)==(SDL_KEYDOWN, SDLK_RIGHT):
        #    if boy[boyindex].state in (boy[boyindex].RIGHT_STAND, boy[boyindex].LEFT_STAND):
        #         boy[boyindex].state = boy[boyindex].RIGHT_RUN
        #elif (event.type,event.key)==(SDL_KEYUP, SDLK_LEFT):
        #    if boy[boyindex].state in (boy[boyindex].RIGHT_RUN, boy[boyindex].LEFT_STAND):
        #        boy[boyindex].state = boy[boyindex].LEFT_STAND
        #elif (event.type,event.key)==(SDL_KEYUP, SDLK_LEFT):
        #    if boy[boyindex].state in (boy[boyindex].RIGHT_RUN, boy[boyindex].LEFT_STAND):
        #        boy[boyindex].state = boy[boyindex].LEFT_STAND

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                boy[boyindex].state = boy[boyindex].LEFT_RUN
            if event.key == SDLK_RIGHT:
                boy[boyindex].state = boy[boyindex].RIGHT_RUN
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                boy[boyindex].state = boy[boyindex].LEFT_STAND
            if event.key == SDLK_RIGHT:
                boy[boyindex].state = boy[boyindex].RIGHT_STAND



def update():
    for team in  boy:
        team.update()

def draw():
    clear_canvas()
    grass.draw()
    global boyindex
    numbers.draw(boyindex + 1, 740, 540)
    for team in boy:
        team.draw()
    update_canvas()



