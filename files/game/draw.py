import pygame

import files.utils as f

def Draw(App):
	if App.warning_init.is_finished():
		game_states(App)
	else:
		App.warning_init.update(App)

def game_states(App):
	if (App.minigame.isInMinigame()):
		App.minigame.update(App)
	elif (App.menu.start_game):
		App.game.updater(App)
	else:
		App.menu.update(App)
		