import pygame
from files.menu.paychecks_animation import PaycheckAnimations


class NightBeatenAnimation:
    def __init__(self, App):
        self.index = 4
        self.reversed = True
        self.space = 40
        self.position_x = 370
        self.dims_y = App.assets.five_animation[0].get_height()
        self.numbers_width = App.assets.five_animation[0].get_width()
        self.alpha = 0
        self.timer = pygame.time.get_ticks()
        self.start_animation = False
        self.ended_animation = False
        self.pay_animation = PaycheckAnimations(App)

    def update(self, App):
        # Change alpha
        if not self.pay_animation.inAnimation:
            if not self.start_animation:
                self.alpha = App.animations.in_fade_effect.fade_alpha
                App.assets.five_animation[self.index].set_alpha(self.alpha)
                App.assets.big_am.set_alpha(self.alpha)

            if self.alpha >= 240:
                self.start_animation = True
                App.animations.in_fade_effect.fade_alpha = 245
                App.surface.fill((0,0,0))
            else:
                App.animations.in_fade_effect.update(App)
                App.animations.in_fade_effect.fade_screen()

            position = (self.position_x, App.dimentions[1]/2 - self.dims_y/2)
            if not self.index == -1:
                if self.reversed:
                    App.surface.blit(App.assets.five_animation[self.index], position)
                else:
                    App.surface.blit(App.assets.six_animation[self.index], position)
                
            App.surface.blit(App.assets.big_am, (self.position_x + self.numbers_width + self.space, App.dimentions[1]/2 - self.dims_y/2))

            print(self.index)

            if self.start_animation and not self.ended_animation:
                self.change_numbers(App)

            if self.ended_animation:
                if pygame.time.get_ticks() - self.timer > 4000:
                    print("change start")
                    if App.menu.inNight < 5: 
                        self.end_reset_variables(App)
                    else:
                        self.pay_animation.inAnimation = True

        elif self.pay_animation.inAnimation:
            App.surface.fill((0,0,0))

            if App.menu.inNight == 6:
                self.pay_animation.paycheck_asset = App.assets.night_six_paycheck

            if self.pay_animation.change_to_menu:
                self.end_reset_variables(App, toMenu=True)

        self.pay_animation.update(App)
                

    def end_reset_variables(self, App, toMenu=False):
        if toMenu:
            night = App.menu.inNight
            App.menu.__init__(App)
            App.menu.start_state = 0
            App.menu.inNight = night
        else:
            App.menu.start_state = 2
        App.menu.start_game = False
        App.menu.timer = pygame.time.get_ticks()
        App.menu.objects_alpha = 255
        App.menu.played_once = True
        if App.menu.inNight <= 5:
            App.menu.inNight += 1

    def change_numbers(self, App):
        if self.reversed:
            if self.index != -1:
                if pygame.time.get_ticks() - self.timer > 200:
                    self.index -= 1
                    self.timer = pygame.time.get_ticks()
            else:
                if pygame.time.get_ticks() - self.timer > 700:
                    self.index = 0
                    self.reversed = False
                    self.timer = pygame.time.get_ticks()

        else:
            if self.index != 5:
                if pygame.time.get_ticks() - self.timer > 200:
                    self.index += 1
                    self.timer = pygame.time.get_ticks()
            else:
                
                pygame.mixer.Sound.play(App.assets.joy_sound)
                self.ended_animation = True
                self.timer = pygame.time.get_ticks()
                