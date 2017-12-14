import random

from pico2d import *

class Onegrass:
    def __init__(self):
        self.x, self.y = 0, 0

    def set_background(self, bg):
        self.bg = bg

    def update(self, frame_time):
        pass
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
        return sx, sy, sx + 817, sy + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class OnePipe:
    def __init__(self):
        self.x, self.y = 354, 35

    def set_background(self, bg):
        self.bg = bg

    def update(self, frame_time):
        pass
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
        return sx - 15, sy - 22, sx + 11, sy + 22

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class TwoPipe:
    def __init__(self):
        self.x, self.y = 469, 45

    def set_background(self, bg):
        self.bg = bg

    def update(self, frame_time):
        pass
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
        return sx - 15, sy - 22, sx + 11, sy + 22

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class ThreePipe:
    def __init__(self):
        self.x, self.y = 563, 55

    def set_background(self, bg):
        self.bg = bg

    def update(self, frame_time):
        pass
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
        return sx - 15, sy - 22, sx + 11, sy + 22

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

