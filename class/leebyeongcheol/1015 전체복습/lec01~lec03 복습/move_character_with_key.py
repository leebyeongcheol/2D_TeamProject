from pico2d import *

def handle_events():
    global running
    global x
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    x = x + 100
                elif event.key == SDLK_LEFT:
                    x = x - 100
                elif event.key == SDLK_ESCAPE:
                    running = False

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
x = 0
frame = 0

while ( x < 800 and running):
    clear_canvas_now()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()
    get_events()

close_canvas()