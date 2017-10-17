from pico2d import*

def handle_event(self, event):
    if(event.type, event.key) == (SDL_KEYDOWN,SDLK_LEFT):
        if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
            self.state = self. LEFT_RUN
        elif(event.type, event.key) ==(SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.RIGHT_RUN
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN):
                self.state = self.LEFT_STAND
        elif ( event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND

def update(self):
    self.frame = (self.frame +1) %8
    if self.state == self.RIGHT_RUN:
        self.x = min(800, self.x +5)
    elif self.state == self.LEFT_RUN:
        self.x = max(0,self.x -5)

def handle_events():
    global running
    global hero
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False
        else:
            hero.handle_event(event)


