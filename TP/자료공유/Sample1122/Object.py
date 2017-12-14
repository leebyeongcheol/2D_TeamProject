import random

from pico2d import *

class FPipe:
    def __init__(self):
        self.x, self.y = 354, 35
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir = 0
        self.ydir = 0
        self.jumpstate = 0
        self.isJump = False

    def set_background(self, bg):
        self.bg = bg

    def update(self, frame_time):
        pass
        # 1 pipe
        #if ((self.x > 330 and self.x < 380) and (self.y < 65)):
        #    self.x -= (self.xdir * distance)
        ## 2 pipe
        #if ((self.x > 445 and self.x < 495) and (self.y < 65)):
        #    self.x -= (self.xdir * distance)
        ##3 pipe
        #if ((self.x > 540 and self.x < 590) and (self.y < 75)):
        #   self.x -= (self.xdir * distance)
        ##4 pipe
        #if ((self.x > 660 and self.x < 710) and (self.y < 75)):
        #   self.x -= (self.xdir * distance)
#
    def get_bb(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        #return self.x - 14, self.y - 22, self.x + 10, self.y + 22
        return sx - 15, sy - 22, sx + 11, sy + 22

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
