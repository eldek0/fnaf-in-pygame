import pygame


class YouLostAnimation:
    def __init__(self, App):
        self.timer = pygame.time.get_ticks()
        self.state = 0
        self.inNight = 1
        self.played_once = True

    def update(self, App):
        match self.state:
            case 0:
                self.inNight = App.menu.inNight
                App.animations.static_anim_1.update(App.surface)
                App.animations.static_anim_1.alpha = 255
                App.assets.game_lost_static.play()
                
                self.state = 1
                self.timer = pygame.time.get_ticks()
            case 1:
                App.animations.static_anim_1.update(App.surface)
                if pygame.time.get_ticks() - self.timer > 10000:
                    self.state = 2
                    self.timer = pygame.time.get_ticks()
                    App.assets.menu_static.stop()
                    App.assets.game_lost_static2.stop()
            
            case 2:
                App.surface.blit(App.assets.lost_screen, (0, 0))

                App.animations.static_anim_1.alpha = 100
                App.animations.static_anim_1.update(App.surface)

                App.surface.blit(App.assets.game_over, (App.dimentions[0]/2 - App.assets.game_over.get_width()/2, App.dimentions[1] - 120))

                if pygame.time.get_ticks() - self.timer > 8000:
                    # Return to menu
                    App.menu.__init__(App)
                    App.menu.start_state = 0
                    App.menu.start_game = False
                    App.menu.static_with_change = True
                    App.menu.option = False
                    App.menu.inNight = self.inNight
                    App.menu.played_once = self.played_once
                    
                    