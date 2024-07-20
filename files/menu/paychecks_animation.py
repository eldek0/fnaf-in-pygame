import pygame

class PaycheckAnimations:
    def __init__(self, App):
        self.inAnimation = False
        self.fading = True
        self.canShow = True
        self.last_fade = False
        self.change_to_menu = False
        self.timer = pygame.time.get_ticks()
        self.paycheck_asset = App.assets.night_five_paycheck

    def update(self, App):
        if self.inAnimation:
            if not pygame.mixer.Channel(4).get_busy():
                pygame.mixer.Channel(4).play(App.assets.music_box2)

            self.night_paycheck(App)

            self.fade(App)
        else:
            self.timer = pygame.time.get_ticks()

    def fade(self, App):
        App.animations.fade_effect.update(App.uiSurface, App.deltaTime)
        
    def night_paycheck(self, App):

        if self.canShow:
            App.uiSurface.blit(self.paycheck_asset, (0, 0))
            
            if not self.last_fade:
                if pygame.time.get_ticks() - self.timer > 18000:
                    App.animations.fade_effect.continue_effect(out_effect=False)
                    self.last_fade = True
                    
            else:
                if App.animations.fade_effect.fade_alpha > 250:
                    self.change_to_menu = True
                    pygame.mixer.Channel(4).stop()