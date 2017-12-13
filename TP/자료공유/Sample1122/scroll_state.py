from pico2d import *

import game_framework


from boy import FreeBoy as Boy # import Boy class from boy.py
from background import FixedBackground as Background


name = "scroll_state"

boy = None
background = None

def create_world():
    global boy, background
    boy = Boy()
    background = Background()

    # fill here
    background.set_center_object(boy)
    boy.set_background(background)


def destroy_world():
    global boy, background
    del(boy)
    del(background)


def enter():
    #open_canvas(800, 600)
    hide_cursor()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass

def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                boy.handle_event(event)
                background.handle_event(event)



def update(frame_time):
    boy.update(frame_time)
    background.update(frame_time)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def draw():
    clear_canvas()
    background.draw()
    boy.draw()
    boy.draw_bb()
    update_canvas()






