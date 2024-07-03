import pygame

import files.utils as f

def Draw(App):
	if not App.warning_init.is_finished():
		App.warning_init.update(App)
	
	else:
		if not App.inMinigame:
			if not App.menu.start_game:
				App.menu.update(App)
			else:
				App.game.updater(App)
		else:
			App.minigame.update(App) # TODO CHANGE LATER