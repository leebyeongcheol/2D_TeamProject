from pico2d import*
import random
import game_framework
import title_state

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
    def __init__(self):
        self.x, self.y = 0,90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x +=2
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
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()

def exit():
    global boy, grass
    del(boy)
    del(grass)

def handle_events():
    global running
    global MouseState
    global mouse_x, mouse_y
    global Movingboy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)



def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

