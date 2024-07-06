import pygame

import files.utils as f

def Draw(App):
	if App.warning_init.is_finished():
		game_states(App)
	else:
		App.warning_init.update(App)

def game_states(App):
	if (App.menu.start_game):
		App.game.updater(App)
	elif (App.minigame.inMinigame):
		App.minigame.update(App)
	else:
		App.menu.update(App)
		