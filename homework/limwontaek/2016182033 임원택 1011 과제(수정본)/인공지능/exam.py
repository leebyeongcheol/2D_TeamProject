import random
import numbers
from pico2d import *

MouseState = False
Movingboy = 10
global Each_numbers
Each_numbers = 0

def handle_events():
    global running
    global MouseState
    global mouse_x,mouse_y
    global Movingboy

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_0:
                Movingboy = 0
            elif event.key == SDLK_1:
                Movingboy =1
            elif event.key == SDLK_2:
                Movingboy =2
            elif event.key == SDLK_3:
                Movingboy = 3
            elif event.key == SDLK_4:
                Movingboy =4
            elif event.key == SDLK_5:
                Movingboy =5
            elif event.key == SDLK_6:
                Movingboy =6
            elif event.key == SDLK_6:
                Movingboy =6
            elif event.key == SDLK_6:
                Movingboy =6
            elif event.key == SDLK_7:
                Movingboy =7
            elif event.key == SDLK_8:
                Movingboy =8
            elif event.key == SDLK_9:
                Movingboy =9
            elif event.key == SDLK_a:
                Movingboy =10
            elif event.key == SDLK_UP:
                Movingboy +=1
            elif event.key == SDLK_DOWN:
                Movingboy -= 1

        elif event.type == SDL_MOUSEMOTION:
            mouse_x = event.x
            mouse_y = 600-event.y
            MouseState = True
        else:
            MouseState = False

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
class Boy:
    global MouseState
    global mouse_x
    global mouse_y
    global Movingboy
    global num
    global cnt

    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0,1,2,3

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

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }

    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7)
        self.dir = 1
        self.state= self.RIGHT_RUN
        self.run_frames = 0
        self.stand_frames = 0
        self.index = 0
        self.cnt = 0
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)


    def update_mouse(self):
        self.frame = (self.frame + 1) % 8
        if MouseState == True:
            if mouse_x <= self.x:
                self.x -= 5
            elif mouse_x >= self.y:
                self.x += 2
            if mouse_y <= self.y:
                self.y -= 5
            elif mouse_y >= self.y:
                self.y += 2
    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state*100, 100, 100, self.x, self.y)
        numbers.draw(self.index,self.x+20,self.y-20,0.5)

    def drawnumbers(self):
        if self.index == Movingboy:
            numbers.draw(self.index,750,550,1)

def main():
    open_canvas()
    team = [Boy() for i in range(1000)]
    grass = Grass()

    global  running
    running = True
    while running:
        handle_events()

        for i in range(11):
            if i != Movingboy:
                team[i].update()
            else:
                team[i].update_mouse()
        clear_canvas()
        grass.draw()
        for i in range(11):
            team[i].draw()
            team[i].index =i
            team[i].drawnumbers()
        update_canvas()

        delay(0.05)

    close_canvas()

if __name__ == '__main__':
    main()