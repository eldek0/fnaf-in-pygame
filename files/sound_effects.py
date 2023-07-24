import pygame

def sounds_effects_updater(App):
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