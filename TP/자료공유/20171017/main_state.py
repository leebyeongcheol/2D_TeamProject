from pico2d import*
import random
import game_framework
import title_state

def handle_events():
    global  running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 20)
class Boy:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0,1,2,3

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.LEFT_RUN
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                    self.state = self.RIGHT_RUN
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                if self.state in (self.LEFT_RUN):
                    self.state = self.LEFT_STAND
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                if self.state in (self.RIGHT_RUN,):
                    self.state = self.RIGHT_STAND

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
        self.x, self.y = random.randint(100, 700), 55
        self.frame = random.randint(0,7)
        self.dir = 1
        self.state = self.RIGHT_STAND
        self.run_frames = 0
        self.stand_frames = 0
        if self.image == None:
            Boy.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.state == self.RIGHT_RUN:
            self.x += 5
            self.x = min(800, self.x + 5)
        elif self.state == self.LEFT_RUN:
            self.x -= 5
            self.x = max(0, self.x - 5)

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state*100, 32, 30, self.x, self.y)

def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()

def exit():
    global boy, grass
    del(boy)
    del(grass)

def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

def main():
    open_canvas()
    global boy
    boy = Boy()
    grass = Grass()

    global running
    running = True
    while running:
        handle_events()

        boy.update()

        clear_canvas()
        grass.draw()
        boy.draw()
        update_canvas()

        delay(0.05)

    close_canvas()

if __name__ == '__main__':
    main()