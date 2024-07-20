import pygame, random
from files.save.save import read
from files.menu.menu import Menu
from files.minigames.minigame import Minigame

class WarningInit:
    def __init__(self, App):
        self._finished = False
        self.timer = pygame.time.get_ticks()
        self.alpha = 255
        self.ran_number = 0
        self.ran_screen = 0
        self.death_screen = False

    def update(self, App):
        dims = App.inital_warning.get_rect()
        App.inital_warning.set_alpha(self.alpha)
        App.uiSurface.blit(App.inital_warning, (App.dimentions[0]/2 - dims.w/2, App.dimentions[1]/2 - dims.h/2))

        if App.loaded:
            if pygame.time.get_ticks() - self.timer > 4000:
                self.alpha -= 2 * App.deltaTime 

            if self.alpha <= 0:
                self.finish(App)
        else:
            self.timer = pygame.time.get_ticks()

    def is_finished(self): return self._finished

    def finish(self, App):
        """ Change to menu and load everything from the save file """
        if not self._finished:
            data = read(App)
            if not App.debug:
                data = read(App)

            
            App.menu = Menu(App)
            App.minigame = Minigame(App)

            if data:
                App.menu.inNight = data["Night"]
                App.menu.played_once = data["Played"]
                App.menu.custom_night_menu.completed_nights = data["Custom"]
                App.menu.cutscenes_data = data["Cutscenes"]
                App.ctrl_adv = data["Ctrl"]
                App.menu.passed_real_time = data["RealTime"]
            
            if data["Played"]: # At least opened the game once
                self.death_screen_probability(App)

            if not self.death_screen:
                App.started = True
                self._finished = True
            else:
                self.random_appearance(App)

    def death_screen_probability(self, App):
        if not self.death_screen:
            self.ran_number = random.randint(0, 100_000)
            if (self.ran_number >= 5000 and self.ran_number < 5030):
                self.death_screen = True
                self.ran_screen = random.randint(0, len(App.assets.rare) - 1)
                pygame.mixer.stop()
                pygame.mixer.Channel(1).play(App.assets.popstatic)

    def random_appearance(self, App):
        App.uiSurface.blit(App.assets.rare[self.ran_screen], (0, 0))
        if not (pygame.mixer.Channel(1).get_busy()):
            App.started = True
            self._finished = True