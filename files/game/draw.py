import pygame

import files.utils as f
from files.game.game_controller import Game

def Draw(App):
	if not App.warning_init.is_finished():
		App.warning_init.update(App)
	
	else:
		App.game = Game(App)
		App.game.updater(App)