import pygame, random
from files.minigames.give_gifts import GiveGifts
from files.minigames.save_them import SAVETHEM 

class Minigame:
    def __init__(self, App):
        self.static_rect = pygame.Rect(0, 0, App.surface.get_width(), 50)
        self.static_timer:int = pygame.time.get_ticks()
        self.showing_static:bool = False
        self.minigames = [
            GiveGifts(App),
            SAVETHEM(App)
        ]
        self.inMinigameId:int = 1

    def update(self, App):
        App.minigamesSurface.fill((0, 0, 0))
        self.static(App)

        minigame = self.minigames[self.inMinigameId]
        if not minigame.ended:
            minigame.update(App)

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