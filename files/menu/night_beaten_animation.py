import pygame, random
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
        self.confetti_timer = pygame.time.get_ticks()
        self.confetti_direction = [
            {"time_spawn":0, "add":(1, 1), "ran_time":random.randint(1, 100)},
            {"time_spawn":500, "add":(1, 1), "ran_time":random.randint(1, 100)},
            {"time_spawn":4800, "add":(-1, 1), "ran_time":random.randint(1, 100)},
            {"time_spawn":1500, "add":(-1, 1), "ran_time":random.randint(1, 100)},
            {"time_spawn":3000, "add":(1, 1), "ran_time":random.randint(1, 100)},
            {"time_spawn":2300, "add":(-1, 1), "ran_time":random.randint(1, 100)},
            {"time_spawn":2000, "add":(-1, 1), "ran_time":random.randint(1, 100)},
            {"time_spawn":4000, "add":(1, 1), "ran_time":random.randint(1, 100)},
            {"time_spawn":3400, "add":(-1, 1), "ran_time":random.randint(1, 100)},
            {"time_spawn":5300, "add":(-1, 1), "ran_time":random.randint(1, 100)},
            {"time_spawn":3400, "add":(-1, 1), "ran_time":random.randint(1, 100)},
            {"time_spawn":4500, "add":(1, 1), "ran_time":random.randint(1, 100)}
        ]

    def update(self, App):
        # Change alpha
        if not self.pay_animation.inAnimation:
            if not self.start_animation:
                App.animations.fade_effect.continue_effect(out_effect=False)
                self.alpha = App.animations.fade_effect.fade_alpha
                App.assets.five_animation[self.index].set_alpha(self.alpha)
                App.assets.big_am.set_alpha(self.alpha)
                self.confetti_timer = pygame.time.get_ticks()

            if self.alpha >= 250:
                self.start_animation = True
                App.animations.fade_effect.stop_effect()
                App.animations.fade_effect.continue_effect(out_effect=True)
                App.uiSurface.fill((0,0,0))
            else:
                App.animations.fade_effect.update(App.uiSurface, App.deltaTime)

            position = (self.position_x, App.dimentions[1]/2 - self.dims_y/2)
            if not self.index == -1:
                if self.reversed:
                    App.uiSurface.blit(App.assets.five_animation[self.index], position)
                else:
                    App.uiSurface.blit(App.assets.six_animation[self.index], position)
                
            App.uiSurface.blit(App.assets.big_am, (self.position_x + self.numbers_width + self.space, App.dimentions[1]/2 - self.dims_y/2))

            if self.start_animation and not self.ended_animation:
                self.change_numbers(App)

            if self.ended_animation:
                if pygame.time.get_ticks() - self.timer > 4000:
                    if App.menu.nightToPlay == 7:
                        index = App.menu.custom_night_menu.mode_index
                        App.menu.custom_night_menu.completed_nights[index] = True

                    if App.menu.nightToPlay < 5: 
                        self.end_reset_variables(App)
                    else:
                        if App.menu.nightToPlay == 7 and App.menu.custom_night_menu.completed_nights == [True, True, True, True, True, True, True, True, True, True]:
                            self.pay_animation.inAnimation = True
                            self.pay_animation.paycheck_asset = App.assets.night_seven_paycheck
                        elif App.menu.nightToPlay == 5 or App.menu.nightToPlay == 6:
                            self.pay_animation.inAnimation = True
                        else:
                            self.end_reset_variables(App, toMenu=True)
                            print("to menu")

        elif self.pay_animation.inAnimation:
            App.uiSurface.fill((0,0,0))

            if App.menu.nightToPlay == 6:
                self.pay_animation.paycheck_asset = App.assets.night_six_paycheck

            if self.pay_animation.change_to_menu:
                self.end_reset_variables(App, toMenu=True)

        self.pay_animation.update(App)
        self.update_confetti(App)
                
    def update_confetti(self, App):
        index = 0
        time_to_spawn = 0
        if self.start_animation:
            for anim in App.animations.confs_animation:
                data = self.confetti_direction[round(index%(len(self.confetti_direction)-1))]
                if pygame.time.get_ticks() - self.confetti_timer > time_to_spawn + data["time_spawn"] + data["ran_time"] + anim.ran_value*8:
                    anim.position[0] += data["add"][0]/2.5 * App.deltaTime
                    anim.position[1] += data["add"][1]*1.5 * App.deltaTime
                    anim.update(App.uiSurface)
                index += 1

    def end_reset_variables(self, App, toMenu=False):
        if toMenu:
            App.menu.init_menu_and_save_vars(App)
        else:
            App.menu.start_state = 2

        App.menu.start_game = False
        App.menu.timer = pygame.time.get_ticks()
        App.menu.objects_alpha = 255
        if App.menu.nightToPlay <= 5:
            App.menu.nightToPlay += 1
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
                