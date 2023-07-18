import pygame

import files.utils as f

def Draw(App):
	if App.scene == 0:

		if not App.objects.Animatronics.gameOver:
			# Sounds
			if not pygame.mixer.Channel(1).get_busy():
				pygame.mixer.Channel(1).play(App.assets.fan_sound)

			if App.objects.music_box.charge != 0:
				if not pygame.mixer.Channel(2).get_busy():
					pygame.mixer.Channel(2).play(App.assets.music_box)
			else:
				pygame.mixer.Channel(2).set_volume(1)
				if pygame.mixer.Channel(2).get_sound() == App.assets.music_box:
					pygame.mixer.Channel(2).play(App.assets.times_out)

				if not pygame.mixer.Channel(2).get_busy():
					pygame.mixer.Channel(2).play(App.assets.times_out)


			if App.objects.mask_button.inMask:
				if not pygame.mixer.Channel(4).get_busy():
					pygame.mixer.Channel(4).play(App.assets.mask_breathing)
			else:
				pygame.mixer.Channel(4).stop()

			if App.objects.office.animatronic_in_office:
				if not pygame.mixer.Channel(5).get_busy():
					pygame.mixer.Channel(5).play(App.assets.stare)
			if not App.objects.office.animatronic_in_office:
				pygame.mixer.Channel(5).stop()

			if App.objects.Animatronics.animatronics_in_game["PUPPET"].activated:
				App.objects.music_box.run_time(App)

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

		