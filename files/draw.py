import pygame

import files.utils as f

def Draw(App):
	#App.menu.start_state = 6
	if not App.menu.start_game:
		App.menu.update(App)
	else:
		App.game.updater(App)