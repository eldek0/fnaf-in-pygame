import pygame

import files.utils as f
from files.sound_effects import sounds_effects_updater

def Draw(App):
	if App.scene == 0:

		if not App.objects.Animatronics.gameOver:

			# Sounds
			sounds_effects_updater(App)

			# Background
			App.objects.camera.timers_update(App)

			if App.objects.open_monitor_button.inCamera == False:
				App.objects.office.update(App)
			elif App.objects.open_monitor_button.inCamera and App.objects.open_monitor_button.quitting_camera:
				App.objects.office.update(App, canInteract=False, draw=True)
			elif App.objects.open_monitor_button.inCamera:
				App.objects.office.update(App, canInteract=False, draw=False)
			
			if App.objects.open_monitor_button.inCamera and not App.objects.open_monitor_button.quitting_camera:
				# Update camera
				App.objects.camera.update(App)
				App.objects.open_monitor_button.update(App)
			elif App.objects.mask_button.inMask:
				# Update mask button
				App.objects.mask_button.update(App)
			else:
				# Update mask button
				App.objects.mask_button.update(App)
				# Update camera button
				App.objects.open_monitor_button.update(App)

			App.objects.battery.update(App)

			# Update animatronics
			App.objects.Animatronics.update(App)
			App.gameOver = App.objects.Animatronics.gameOver

		else:
			App.animations.static_anim_1.alpha = 255
			App.animations.static_anim_1.update(App.surface)

		