import pygame

def sounds_effects_updater(App):
    if not pygame.mixer.Channel(8).get_busy():
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

        mangle = App.objects.Animatronics.animatronics_in_game["MANGLE"]
        if mangle.locationId == -1:
            pygame.mixer.Channel(6).set_volume(1)
        elif (App.objects.camera.inCameraRoom == mangle.locationId and App.objects.open_monitor_button.inCamera and not mangle.changing_position):
            pygame.mixer.Channel(6).set_volume(0.4)
        else:
            pygame.mixer.Channel(6).set_volume(0)
        
        if not pygame.mixer.Channel(6).get_busy():
            pygame.mixer.Channel(6).play(App.assets.mangle_noise)
        
        baloon_boy = App.objects.Animatronics.animatronics_in_game["BALOON_BOY"]
        
        if baloon_boy.locationId == -1:
            pygame.mixer.Channel(7).set_volume(1)
        else:
            if not pygame.mixer.Channel(7).get_busy():
                pygame.mixer.Channel(7).set_volume(0)

        if not pygame.mixer.Channel(7).get_busy():
            pygame.mixer.Channel(7).play(App.assets.baloon_laugh)

        # Scary ambiance
        position = App.objects.Animatronics.every_animatrionic_position
        if pygame.time.get_ticks() - App.ambiance_sound > 25000:
            if position[101] != [] or position[103] != [] or position[102] != []:
                App.assets.scary_ambiance.play()
                App.ambiance_sound = pygame.time.get_ticks()