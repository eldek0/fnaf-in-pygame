import pygame
from pygame.locals import *
from files.minigames.dummy import MinigameDummy
from files.minigames.entity import Entity

class GiveGifts(MinigameDummy):
    def __init__(self, App):
        super().__init__(App)

        self.surf_width, self.surf_height = App.surface.get_width(), App.surface.get_height()
        self.puppet = Entity(App.assets.puppet_minigame, (self.surf_width/2 - App.assets.puppet_minigame.get_width()/2, self.surf_height/2 - App.assets.puppet_minigame.get_height()/2))
        self.score = 0 # One score is a hundred points 
        
        delta_y = 50
        
        self.souls:list = [
            Entity(App.assets.soul, (self.surf_width/4 - App.assets.puppet_minigame.get_width()/2, self.surf_height/4 - App.assets.puppet_minigame.get_height()/2 + delta_y)),
            Entity(App.assets.soul, (self.surf_width/1.5 - App.assets.puppet_minigame.get_width()/1.5 + 100, self.surf_height/4 - App.assets.puppet_minigame.get_height()/2 + delta_y)),
            Entity(App.assets.soul, (self.surf_width/4 - App.assets.puppet_minigame.get_width()/2, self.surf_height/1.5 - App.assets.puppet_minigame.get_height()/1.5 + delta_y + 100)),
            Entity(App.assets.soul, (self.surf_width/1.5 - App.assets.puppet_minigame.get_width()/1.5 + 100, self.surf_height/1.5 - App.assets.puppet_minigame.get_height()/1.5 + delta_y + 100))
        ]

        margin = 90
        size_horizontal = 20
        size_vertical = 50
        self.boundaries:list = [
            (pygame.Rect(margin, margin, size_vertical, self.surf_height - (margin)*2 + 30), (200, 200, 200)), # Vertical left
            (pygame.Rect(self.surf_width - margin - size_vertical, margin, size_vertical, self.surf_height - (margin)*2 + 30), (200, 200, 200)), # Vertical right
            (pygame.Rect(margin, margin, self.surf_width - margin*2, size_horizontal), (200, 200, 200)), # Horizontal up
            (pygame.Rect(margin, self.surf_height - (margin - 30), self.surf_width - margin*2, size_horizontal), (200, 200, 200)) # Horizontal down
        ]

        for i in range(len(self.souls)):
            soul = self.souls[i]
            self.boundaries.append(
                (soul.texture, tuple(soul.position), lambda index=i:self.detect_collition(App, index), False, 0)
            )


        self.masks = [
            App.assets.chica_mask,
            App.assets.fred_mask,
            App.assets.bonnie_mask,
            App.assets.foxy_mask
        ]

        self.last = Entity(App.assets.soul, (self.surf_width/2 - App.assets.puppet_minigame.get_width()/2, self.surf_height/2 - App.assets.puppet_minigame.get_height()/2))

        self.state = 0 # 0. Give gifts, 1. Give life

        self.gifts_and_masks_given = [False, False, False, False]

        self.timer = pygame.time.get_ticks()

    def update(self, App):
        if not pygame.Channel(2).get_busy():
            pygame.Channel(2).play(App.assets.static_end)

        for soul in self.souls:
            soul.update()

        self.draw_boundaries(App, self.boundaries, self.puppet)

        self.puppet.update()

        self.show_score(App, (75, 10))

        pos = (340, 2)
        if (self.state == 0):
            App.minigamesSurface.blit(App.assets.give_gifts, pos)
            self.show_gifts(App)
        else:
            App.minigamesSurface.blit(App.assets.give_life, pos)
            self.show_lives(App)

        if (self.state == 1 and self.gifts_and_masks_given == [True, True, True, True]):
            self.last.update()
        else:
            self.key_movement(App)

        self.comprobe_state(App)

    def key_movement(self, App):
        key = pygame.key.get_pressed()

        if (key[pygame.K_RIGHT] or key[pygame.K_d]):
            self.puppet.movement('r')
            self.puppet.texture = App.assets.puppet_minigame
        
        if (key[pygame.K_LEFT] or key[pygame.K_a]):
            self.puppet.movement('l')
            self.puppet.texture = pygame.transform.flip(App.assets.puppet_minigame, True, False)

        if (key[pygame.K_UP] or key[pygame.K_w]):
            self.puppet.movement('u')

        if (key[pygame.K_DOWN] or key[pygame.K_s]):
            self.puppet.movement('d')

    def show_score(self, App, position:tuple):
        num_width = App.assets.numbers_big[0].get_width()
        App.minigamesSurface.blit(App.assets.numbers_big[0], position)
        App.minigamesSurface.blit(App.assets.numbers_big[self.score], (position[0] + num_width, position[1]))
        App.minigamesSurface.blit(App.assets.numbers_big[0], (position[0] + num_width*2, position[1]))
        App.minigamesSurface.blit(App.assets.numbers_big[0], (position[0] + num_width*3, position[1]))

    def show_gifts(self, App):
        for i in range(len(self.gifts_and_masks_given)):
            if (self.gifts_and_masks_given[i]):
                if (i%2 == 0):
                    pos = (self.souls[i].position[0] + 120, self.souls[i].position[1] + 8)
                else:
                    pos = (self.souls[i].position[0] - 120, self.souls[i].position[1] - 8)

                App.minigamesSurface.blit(App.assets.gift, pos)

    def show_lives(self, App):
        for i in range(len(self.gifts_and_masks_given)):
            if (self.gifts_and_masks_given[i]):
                pos = (self.souls[i].position[0] - 20, self.souls[i].position[1] - 35)
                App.minigamesSurface.blit(self.masks[i], pos)

    def detect_collition(self, App, index:int):
        if not self.gifts_and_masks_given[index]:
            self.score += 1
            if self.state == 0:
                pygame.mixer.Channel(1).play(App.assets.cake_sound)
            else:
                pygame.mixer.Channel(1).play(App.assets.pop)
                self.puppet.speed -= 4

            self.gifts_and_masks_given[index] = True
            self.timer = pygame.time.get_ticks()

    def comprobe_state(self, App):
        if (self.state == 0 and self.gifts_and_masks_given == [True, True, True, True]):
            if pygame.time.get_ticks() - self.timer >= 5_000:
                self.state = 1
                self.gifts_and_masks_given = [False, False, False, False]

        elif (self.state == 1 and self.gifts_and_masks_given == [True, True, True, True]):
            self.jumpscare(App, App.animations.golden_freddy_jump)