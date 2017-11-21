import cProfile
import start_state
import game_framework

import scroll_state as main_state
#import tile_state as main_state



game_framework.run(start_state)
#cProfile.run('game_framework.run(collision)', None, True)

