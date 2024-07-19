import pygame, random


class YouLostAnimation:
    def __init__(self, App):
        self.timer = pygame.time.get_ticks()
        self.state = 0
        self.nightToPlay = 1
        self.played_once = True
        self.ran_num = 0
        self.ran_screen = 0

    def update(self, App):
        match self.state:
            case 0:
                pygame.mixer.stop()
                self.nightToPlay = App.menu.nightToPlay
                App.animations.static_anim_1.update(App.uiSurface, App.deltaTime)
                App.animations.static_anim_1.alpha = 255
                App.assets.game_lost_static.play()
                
                self.state = 1
                self.timer = pygame.time.get_ticks()
            case 1:
                App.animations.static_anim_1.update(App.uiSurface, App.deltaTime)
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.state = 2
                    self.timer = pygame.time.get_ticks()
                    App.assets.game_lost_static.stop()
            
            case 2:
                App.uiSurface.blit(App.assets.lost_screen, (0, 0))

                App.animations.static_anim_1.alpha = 100
                App.animations.static_anim_1.update(App.uiSurface, App.deltaTime)

                App.uiSurface.blit(App.assets.game_over, (App.dimentions[0]/2 - App.assets.game_over.get_width()/2, App.dimentions[1] - 120))

                if pygame.time.get_ticks() - self.timer > 8000:
                    self.random_number()
                    if self.ran_num > 85_000:
                        # Minigame
                        App.minigame.startMinigame(App)
                    elif (self.ran_num > 5000 and self.ran_num < 5030):
                        pygame.mixer.stop()
                        pygame.mixer.Channel(1).play(App.assets.popstatic)
                        self.ran_screen = random.randint(0, len(App.assets.rare)-1)
                        self.state += 1
                    else:
                        # Return to menu
                        App.menu.init_menu_and_save_vars(App)
                        App.menu.static_with_change = True

            case 3:
                App.uiSurface.blit(App.assets.rare[self.ran_screen], (0, 0))
                if not (pygame.mixer.Channel(1).get_busy()):
                    # Return to menu
                    App.menu.init_menu_and_save_vars(App)
                    App.menu.static_with_change = True

    def random_number(self):
        self.ran_num = random.randint(0, 100_000)
                    
                    