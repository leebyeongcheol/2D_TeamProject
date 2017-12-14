import random

from pico2d import *

class FreeObject:
    def __init__(self):
        self.x, self.y = 30, 55
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
        self.life_time += frame_time
        distance = FreeBoy.RUN_SPEED_PPS * frame_time
        self.total_frames += FreeBoy.FRAMES_PER_ACTION * FreeBoy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4

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
        #else:
            #
        self.x += (self.xdir * distance)

        #falling#
        #if(self.x >830 and self.x< 1050):
        #    self.y -= 4*frame_time*100

        self.y += (self.ydir * distance)
        self.x = clamp(0, self.x, self.bg.w)
        self.y = clamp(0, self.y, self.bg.h)
        if self.jumpstate == 1:
            jumpindex = 2
            #if self.y != 90:
            if self.isJump == True:
                self.y += 2*frame_time * 100
                if self.y > 105:
                    self.isJump = False
            else:
               self.y -= 2*frame_time * 100
               if self.y < 55:
                   self.y = 55
                   self.isJump = True
                   self.jumpstate = 0


    def get_bb(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
       # return self.x - 14, self.y - 22, self.x + 10, self.y + 22
        return sx - 14, sy - 22, sx + 10, sy + 22

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
