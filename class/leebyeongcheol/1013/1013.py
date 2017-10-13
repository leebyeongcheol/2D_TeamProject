from pico2d import *


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    image = None
    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0

        self.run_frames = 0
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

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

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand}


def handle_events():
    global running
    global selectBoy
    global change
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            selectBoy.x, selectBoy.y = event.x, 600 - event.y
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_0:
                selectBoy = team[0]
                change = 0
                print("0")
            elif event.key == SDLK_1:
                selectBoy = team[1]
                change = 1
                print("1")
            elif event.key == SDLK_2:
                selectBoy = team[2]
                change = 2
                print("2")
            elif event.key == SDLK_3:
                selectBoy = team[3]
                change = 3
                print("3")
            elif event.key == SDLK_4:
                selectBoy = team[4]
                change = 4
                print("4")
            elif event.key == SDLK_5:
                selectBoy = team[5]
                change = 5
                print("5")
            elif event.key == SDLK_6:
                selectBoy = team[6]
                change = 6
                print("6")
            elif event.key == SDLK_7:
                selectBoy = team[7]
                change = 7
                print("7")
            elif event.key == SDLK_8:
                selectBoy = team[8]
                change = 8
                print("8")
            elif event.key == SDLK_9:
                selectBoy = team[9]
                change = 9
                print("9")
            elif event.key == SDLK_q:
                selectBoy = team[10]
                change = 10
                print("10")
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_DOWN:
                change -= 1
                if (change < 0):
                    change = change * -999
                print(change)
                selectBoy = team[change]
            elif event.key == SDLK_UP:
                change += 1
                change %= 1000
                print(change)
                selectBoy = team[change]


open_canvas()

team = [Boy() for i in range(1000)]
grass = Grass()
boy = Boy()
running = True
selectBoy = team[0]
change = 0
while running:
    for boy in team:
        boy.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()

    update_canvas()
    delay(0.05)
    handle_events()
