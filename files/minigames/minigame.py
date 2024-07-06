import pygame, random
from files.minigames.give_gifts import GiveGifts
from files.minigames.save_them import SAVETHEM 

class Minigame:
    def __init__(self, App):
        self.inMinigame = True
        self.static_rect = pygame.Rect(0, 0, App.surface.get_width(), 50)
        self.static_timer:int = pygame.time.get_ticks()
        self.showing_static:bool = False
        self.minigames = [
            GiveGifts(App),
            SAVETHEM(App)
        ]
        self.inMinigameId:int = 1
        self.timer = pygame.time.get_ticks()
        self.time_to_voice:int = 3000
        self.letter_index = 0

    def update(self, App):
        App.minigamesSurface.fill((0, 0, 0))

        minigame = self.minigames[self.inMinigameId]
        if not minigame.ended:
            minigame.update(App)

        #self.back_voice(App)
        self.static(App)

    def static(self, App):
        if ( not self.showing_static and pygame.time.get_ticks() - self.static_timer > 3000):
            random_pos = random.randint(0, App.surface.get_height() - self.static_rect.height) 
            self.static_rect = pygame.Rect(0, random_pos, self.static_rect.width, self.static_rect.height)
            self.static_timer = pygame.time.get_ticks()
            self.showing_static = True

        if self.showing_static:
            pygame.draw.rect(App.minigamesSurface, (169,169,169), self.static_rect)

            if pygame.time.get_ticks() - self.static_timer > 2000:
                self.static_timer = pygame.time.get_ticks()
                self.showing_static = False

    def back_voice(self, App):
        if pygame.time.get_ticks() - self.timer > self.time_to_voice:
            if (self.letter_index > len(App.assets.sv_tm_audio) - 1):
                self.letter_index = 0
            App.assets.sv_tm_audio[self.letter_index].play()
            self.timer = pygame.time.get_ticks()
            self.letter_index += 1