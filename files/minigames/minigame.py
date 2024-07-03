import pygame
from files.minigames.give_gifts import GiveGifts

class Minigame:
    def __init__(self, App):
        self.give_gifts = GiveGifts(App)

    def update(self, App):
        App.minigamesSurface.fill((0, 0, 0))
        self.give_gifts.update(App)