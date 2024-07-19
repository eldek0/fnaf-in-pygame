import pygame, random
from files.minigames.give_gifts import GiveGifts
from files.minigames.save_them import SAVETHEM
from files.minigames.foxy_go import FoxyGoGo
from files.minigames.take_cake_to_children import TakeCakeToTheChildren

class Minigame:
    def __init__(self, App):
        self.transMinigame = False
        self.inMinigame = False
        self.static_rect = pygame.Rect(0, 0, App.surface.get_width(), 50)
        self.static_timer:int = pygame.time.get_ticks()
        self.reset_minigames(App)
        self.inMinigameId:int = 0
        self.timer = pygame.time.get_ticks()
        self.time_to_voice:int = 3000
        self.letter_index = 0

        self.red_static = [
            pygame.Rect(0, 0, App.surface.get_width(), 170),
            pygame.Rect(0, 400, App.surface.get_width(), 50),
            pygame.Rect(0, 400, App.surface.get_width(), 50)
        ]

        self.static_time_to_move = 50

    def reset_minigames(self, App):
        self.minigames = [
            GiveGifts(App),
            SAVETHEM(App),
            FoxyGoGo(App),
            TakeCakeToTheChildren(App)
        ]

    def update(self, App):
        App.minigamesSurface.fill((0, 0, 0))

        if self.transMinigame:
            surf:pygame.surface.Surface = App.minigamesSurface
            if pygame.time.get_ticks() - self.static_timer > self.static_time_to_move:
                for static in self.red_static:
                    static.y = random.randint(0, surf.get_height() - static.height)
                self.static_timer = pygame.time.get_ticks()
            
            for static in self.red_static:
                pygame.draw.rect(surf, (255, 0, 0), static)

            if pygame.time.get_ticks() - self.timer > 3000:
                self.transMinigame = False
                if self.minigames[self.inMinigameId].ended:
                    self.inMinigame = False
                    App.menu.init_menu_and_save_vars(App)
                else:
                    self.inMinigame = True
                    self.reset_minigames(App)

                self.timer = pygame.time.get_ticks()
                self.static_timer = pygame.time.get_ticks()
                App.assets.static_end.stop()

        elif self.inMinigame:
            self.update_minigame(App)

    def update_minigame(self, App):
        if not pygame.Channel(2).get_busy():
            pygame.Channel(2).play(App.assets.minigame_ambient)

        minigame = self.minigames[self.inMinigameId]
        if not minigame.ended:
            minigame.update(App)

        self.back_voice(App)
        self.static(App)

        if minigame.ended: self.exit_minigame_with_static(App)

    def static(self, App):

        if pygame.time.get_ticks() - self.static_timer > 1800:
            if random.randint(0, 3) == 1:
                App.animations.static_anim_1.alpha = 50
            else:
                App.animations.static_anim_1.alpha = 20
            self.static_timer = pygame.time.get_ticks()

        # White static
        App.animations.static_anim_1.update(App.surface, App.deltaTime)

    def back_voice(self, App):
        if pygame.time.get_ticks() - self.timer > self.time_to_voice:
            if (self.letter_index > len(App.assets.sv_tm_audio) - 1):
                self.letter_index = 0
            App.assets.sv_tm_audio[self.letter_index].play()
            self.timer = pygame.time.get_ticks()
            self.letter_index += 1

    def isInMinigame(self): return self.inMinigame or self.transMinigame

    def exit_minigame_with_static(self, App):
        pygame.mixer.music.unload()
        pygame.mixer.stop()
        App.assets.static_end.play()
        self.inMinigame = False
        self.transMinigame = True
        self.timer = pygame.time.get_ticks()
        self.static_timer = pygame.time.get_ticks()

    def startMinigame(self, App):
        pygame.mixer.music.unload()
        pygame.mixer.stop()
        self.__init__(App)
        App.assets.static_end.play()
        self.transMinigame = True
        self.inMinigameId = random.randint(0, 3)
        