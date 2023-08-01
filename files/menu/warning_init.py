import pygame
from files.save.save import save, read
from files.menu.menu import Menu

class WarningInit:
    def __init__(self, App):
        self._finished = False
        self.timer = pygame.time.get_ticks()
        self.alpha = 255

    def update(self, App):
        dims = App.inital_warning.get_rect()
        App.inital_warning.set_alpha(self.alpha)
        App.surface.blit(App.inital_warning, (App.dimentions[0]/2 - dims.w/2, App.dimentions[1]/2 - dims.h/2))

        if App.loaded:
            if pygame.time.get_ticks() - self.timer > 4000:
                self.alpha -= 2

            if self.alpha <= 0:
                self.finish(App)
        else:
            self.timer = pygame.time.get_ticks()

    def is_finished(self): return self._finished

    def finish(self, App):
        """ Change to menu and load everything from the save file """
        if not self._finished:
            data = read(App)

            App.menu = Menu(App)

            if data:
                App.menu.inNight = data["Night"]
                App.menu.played_once = data["Played"]
                App.menu.custom_night_menu.completed_nights = data["Custom"]
                App.menu.cutscenes_data = data["Cutscenes"]

            self._finished = True