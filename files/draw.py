import pygame

import files.utils as f

def Draw(App):
	if not App.menu.start_game:
		App.menu.update(App)
	else:
		App.game.updater(App)