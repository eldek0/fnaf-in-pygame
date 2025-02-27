import pygame, random
from files.ui.button import Button
from files.game.game_objects import GameObjects
from files.game.game_controller import Game
from files.animations.animations_init import animations_init
from files.menu.custom_night import CustomNight
from files.menu.cutscene import Cutscene
from files.menu.credits import Credits
from files.menu.extras import Extras

class Menu:
    def __init__(self, App): 
        self.option:int = 0 # What button is the mouse hovering

        new_game_dims = App.assets.new_game_option.get_rect()
        self.new_game_button = Button((80, 420), (new_game_dims.width, new_game_dims.height), App.assets.new_game_option)

        continue_dims = App.assets.continue_option.get_rect()
        self.continue_button = Button((80, 490), (continue_dims.width, continue_dims.height), App.assets.continue_option)

        night_six_dims = App.assets.night_six_option.get_rect()
        self.night_six_button = Button((80, 560), (night_six_dims.width, night_six_dims.height), App.assets.night_six_option)

        custom_night_dims = App.assets.custom_night_option.get_rect()
        self.custom_night_button = Button((80, 630), (custom_night_dims.width, custom_night_dims.height), App.assets.custom_night_option)

        extras_size = App.assets.extras_button.get_rect()
        self.extras_button = Button((800, 630), (extras_size.width, extras_size.height), App.assets.extras_button)

        self.background_id = 0
        self.random_value_number = random.randint(500, 2000)
        self.random_value_number2 = random.randint(200, 800)
        self.return_normal_background = False

        self.objects_alpha = 0

        self.background_alpha = 255

        self.start_state = 0 # if 100 will try entering a cutscene

        if App.debug: self.start_state = 0

        self.timer = pygame.time.get_ticks()
        self.pressed_timer = pygame.time.get_ticks()

        self.start_game = False

        self.static_with_change = False

        self.option_ready_to_select = 0

        self.music_started = False

        self.pressed_key = False

        self.pressed_click = False

        self.credits = Credits()

        self.play_real_time_mode = False

        self.extras = Extras(App)

        self.essentials_variables(App)

    def essentials_variables(self, App):
        self.custom_night_menu = CustomNight(App)

        self.cutscene = Cutscene(App)

        self.cutscenes_data = [False, False, False, False]

        self.inNight = 1
        self.nightToPlay = 1

        self.played_once = False

        self.passed_real_time = False

    def static_animation(self, App):
        App.animations.static_anim_1.alpha = 190
        App.animations.static_anim_1.update(App.uiSurface, App.deltaTime)

        # More static animation
        App.animations.static_stripes_animation5.update(App, App.uiSurface)
        
        App.animations.random_static_animation.update(App.uiSurface, App.deltaTime)

    def music(self, App):
        if not pygame.mixer.Channel(2).get_busy():
            pygame.mixer.Channel(2).play(App.assets.menu_static_2)

    def draw_menu_stars(self, App):
        title_dims = App.assets.fnaf_title.get_rect()
        if self.inNight >= 6:
            App.uiSurface.blit(App.assets.star, (80, title_dims.h + 35))
        if self.inNight >= 7:
            App.uiSurface.blit(App.assets.star, (80 + 65, title_dims.h + 35))
            if self.custom_night_menu.completed_nights[0] == True: # 4/20 mode is completed
                App.uiSurface.blit(App.assets.star, (80 + 65*2, title_dims.h + 35))

                if self.passed_real_time:
                    App.uiSurface.blit(App.assets.blue_star, (80 + 65*3, title_dims.h + 35))
            else:
                if self.passed_real_time:
                    App.uiSurface.blit(App.assets.blue_star, (80 + 65*2, title_dims.h + 35))

    def reset_data_option(self, App):
        key = pygame.key.get_pressed()
        if key[pygame.K_DELETE]:
            if pygame.time.get_ticks() - self.pressed_timer > 6000:
                cutscenes = self.cutscenes_data
                self.__init__(App)
                self.cutscenes_data = cutscenes
                self.static_with_change = True
        else:
            self.pressed_timer = pygame.time.get_ticks()

    def start_music(self, App):
        pygame.mixer.music.load(App.assets.background_music_menu)
        pygame.mixer.music.play(-1)
        pygame.mixer.Channel(2).play(App.assets.menu_static_1)
        pygame.mixer.Channel(2).queue(App.assets.menu_static_2)

    def check_cutscene(self):
        if self.inNight < 5:
            if not self.cutscenes_data[self.inNight - 1]:
                self.start_state = 100

    def update(self, App):
        self.check_cutscene()

        if self.start_state < 2:
            
            App.assets.background_menu[self.background_id].set_alpha(self.background_alpha)
            App.uiSurface.blit(App.assets.background_menu[self.background_id], (0,0))
            
            self.static_animation(App)

            # Labels
            App.uiSurface.blit(App.assets.fnaf_title, (80, 30))

            dims = App.assets.scott_credits.get_rect()
            credits_rect = pygame.Rect(
                App.dimentions[0] - dims.w - 10, App.dimentions[1] - dims.h - 20,
                dims.w, dims.h
            )

            if (App.mouse_hitbox.colliderect(credits_rect)):
                App.uiSurface.blit(App.assets.sel_scott_credits, (credits_rect.x, credits_rect.y))
                press = pygame.mouse.get_pressed()
                if press[0]:
                    self.credits.__init__()
                    self.start_state = 12
            else:
                App.uiSurface.blit(App.assets.scott_credits, (credits_rect.x, credits_rect.y))

            dims = App.assets.delete_data_label.get_rect()
            App.uiSurface.blit(App.assets.delete_data_label, (App.dimentions[0]/2 - dims.w/2, App.dimentions[1] - dims.h - 20))
            dims = App.assets.version.get_rect()
            App.uiSurface.blit(App.assets.version, (10, App.dimentions[1] - dims.h - 20))

            self.new_game_button.update(App.uiSurface, App.mouse_hitbox)
            self.continue_button.update(App.uiSurface, App.mouse_hitbox)

            if self.inNight >= 6:
                self.night_six_button.update(App.uiSurface, App.mouse_hitbox)
            if self.inNight >= 7:
                self.custom_night_button.update(App.uiSurface, App.mouse_hitbox)
                self.extras_button.update(App.uiSurface, App.mouse_hitbox)

        if self.start_state == 0:
            self.change_background(App)
            self.music(App)
            self.reset_data_option(App)
            if not self.music_started:
                self.start_music(App)
                self.music_started = True

            self.draw_menu_stars(App)

            keys = self.update_keys(App)
            mouse = pygame.mouse.get_pressed()

            if (self.new_game_button.mouse_hovered and mouse[0]) or (keys[pygame.K_RETURN] and self.option == 1):
                self.option_to_select(App, lambda:self.option_1(App), 1)

            elif (self.continue_button.mouse_hovered and mouse[0]) or (keys[pygame.K_RETURN] and self.option == 2):
                if self.played_once:
                    self.option_to_select(App, lambda:self.option_2(), 2)

            elif ((self.night_six_button.mouse_hovered and mouse[0]) or (keys[pygame.K_RETURN] and self.option == 3)) and self.inNight >= 6:
                if self.played_once:
                    self.option_to_select(App, lambda:self.option_3(), 3)

            elif self.inNight >= 7:

                if ((self.custom_night_button.mouse_hovered and mouse[0]) or (keys[pygame.K_RETURN] and self.option == 4)):
                    if self.played_once:
                        self.option_to_select(App, lambda:self.option_4(), 4)

                elif ((self.extras_button.mouse_hovered and mouse[0]) or (keys[pygame.K_RETURN] and self.option == 5)):
                    if self.played_once:
                        self.option_to_select(App, lambda:self.option_5(), 5)

            if not mouse[0]: 
                self.pressed_click = False

            # Option sprite selector
            if self.option == 1:
                App.uiSurface.blit(App.assets.option_selected, (28, self.new_game_button.position[1] + 3))
            elif self.option == 2:
                App.uiSurface.blit(App.assets.option_selected, (28, self.continue_button.position[1] + 3))
                App.uiSurface.blit(App.assets.night_label_2, (80, 535))
                night = self.inNight
                if night > 5:
                    night = 5
                App.uiSurface.blit(App.assets.numbers2_small[night], (150, 537))

            elif self.option == 3:
                App.uiSurface.blit(App.assets.option_selected, (28, self.night_six_button.position[1] + 3))
            elif self.option == 4:
                App.uiSurface.blit(App.assets.option_selected, (28, self.custom_night_button.position[1] + 3))
            elif self.option == 5:
                App.uiSurface.blit(App.assets.option_selected, (750, self.extras_button.position[1] + 3))

        if self.start_state > 0:
            if self.start_state != 100:
                pygame.mixer.Channel(2).stop()
            self.begin_game(App)

        self.static(App)
        

    def option_1(self, App):
        self.inNight = 1
        self.nightToPlay = 1
        self.start_state = 1
        self.custom_night_menu = CustomNight(App)

    def option_2(self):
        self.start_state = 2
        self.objects_alpha = 255
        self.nightToPlay = self.inNight
        if self.inNight > 5:
            self.nightToPlay = 5

    def option_3(self):
        self.start_state = 2
        self.objects_alpha = 255
        self.nightToPlay = 6

    def option_4(self):
        self.start_state = 10
        self.objects_alpha = 255
        self.nightToPlay = 7

    def option_5(self):
        self.extras.inOption = 1
        self.start_state = 13
        self.pressed_key = False

    def option_real_time(self):
        self.play_real_time_mode = True
        self.start_state = 2
        self.objects_alpha = 255

    def option_to_select(self,App, func, option:int):
        self.option = option
        if self.option_ready_to_select == option and not self.pressed_click:
            self.pressed_key = True
            func()

        if self.option == option and not self.option_ready_to_select == option and not self.pressed_click:
            self.option_ready_to_select = option
            self.pressed_click = True
            App.assets.blip1.play()

    def update_keys(self, App):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_DOWN]) and not self.pressed_key:
            App.assets.blip1.play()
            self.option += 1
            if not (self.played_once):
                self.option = 1
            elif (self.option > 2 and self.inNight <= 5):
                self.option = 1
            elif (self.option > 3 and self.inNight == 6):
                self.option = 1
            elif (self.option > 5 and self.inNight >= 7):
                self.option = 1
            self.pressed_key = True

        elif (keys[pygame.K_UP]) and not self.pressed_key:
            App.assets.blip1.play()
            self.option -= 1
            if not (self.played_once):
                self.option = 1
            elif (self.option < 1 and self.inNight <= 5):
                self.option = 2
            elif (self.option < 1 and self.inNight == 6):
                self.option = 3
            elif (self.option < 1 and self.inNight >= 7):
                self.option = 5
            self.pressed_key = True
        
        if not keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            self.pressed_key = False

        return keys

    def menu_exit(self, App, force=False):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_ESCAPE] and not App.menu.pressed_key) or force:
            App.menu.start_state = 0
            App.menu.static_with_change = True
            App.menu.pressed_key = True

        App.assets.esc_to_return.set_alpha(150)
        App.uiSurface.blit(App.assets.esc_to_return, (15, App.uiSurface.get_height() - 15))    

    def static(self, App):
        if self.static_with_change:
            App.animations.static_anim_2.update(App.uiSurface, App.deltaTime)

            if App.animations.static_anim_2.sprite_num == len(App.animations.static_anim_2.sprites) - 1:
                App.animations.static_anim_2.sprite_num = 0
                App.assets.blip1.play()
                self.static_with_change = False

    def change_background(self, App):
        if pygame.time.get_ticks() - self.timer > self.random_value_number:
            self.return_normal_background = True
            self.random_value_number = random.randint(100, 2000)
            self.background_id = random.randint(1, 3)
            self.timer = pygame.time.get_ticks()
            
        if pygame.time.get_ticks() - self.timer > 60 and self.return_normal_background:
            self.background_id = 0
            self.return_normal_background = False

        if pygame.time.get_ticks() - self.timer > self.random_value_number2:
            choice = random.randint(0, 10)
            self.background_alpha = 25*choice
            self.random_value_number2 = random.randint(200, 800)

    def begin_game(self, App):
        if self.start_state == 1:
            self.show_newspaper(App)
        elif self.start_state >= 2:
            self.show_night(App)

    def show_newspaper(self, App):
        App.assets.newspaper.set_alpha(self.objects_alpha)
        App.uiSurface.blit(App.assets.newspaper, (0, 0))
        
        
        if self.objects_alpha < 255:
            if pygame.time.get_ticks() - self.timer > 5:
                self.objects_alpha += 1 * App.deltaTime
                self.timer = pygame.time.get_ticks()
                #App.animations.fade_effect.stop_effect()
        else:
            if pygame.time.get_ticks() - self.timer > 4000:
                App.animations.fade_effect.continue_effect(out_effect=False)
                App.animations.fade_effect.update(App.uiSurface, App.deltaTime)

                if App.animations.fade_effect.fade_alpha > 240:
                    pygame.mixer.music.unload()
                    self.start_state += 1
                    App.animations.fade_effect.stop_effect()

    def init_menu_and_save_vars(self, App):
        night = self.inNight
        played_once = self.played_once
        cutscenes_data = self.cutscenes_data
        custom_completed_nights = self.custom_night_menu.completed_nights
        custom_night = self.custom_night_menu
        passed_real_time = self.passed_real_time

        self.__init__(App)

        self.inNight = night
        self.played_once = played_once
        self.cutscenes_data = cutscenes_data
        self.custom_night_menu = custom_night
        self.passed_real_time = passed_real_time


    def show_night(self, App):
        if self.start_state <= 7:
            label = None
            if self.play_real_time_mode:
                label = App.assets.realTimeNight
            else:
                label = App.assets.nights_12am[self.nightToPlay - 1]

            label.set_alpha(self.objects_alpha)
            night_dims = label.get_rect()
            App.uiSurface.blit(label, (App.dimentions[0] / 2 - night_dims.w / 2, App.dimentions[1] / 2 - night_dims.h / 2))

        match self.start_state:
            case 2:
                pygame.mixer.music.unload()
                App.animations.fade_effect.update(App.uiSurface, App.deltaTime)
                App.animations.static_anim_2.update(App.uiSurface, App.deltaTime)

                if App.animations.static_anim_2.sprite_num == len(App.animations.static_anim_2.sprites) - 1:
                    self.timer = pygame.time.get_ticks()
                    App.animations.static_anim_2.sprite_num = 0
                    App.assets.blip1.play()
                    self.start_state += 1
                    

            case 3:
                if pygame.time.get_ticks() - self.timer > 2000:
                    self.start_state = 4

            case 4:
                if self.objects_alpha > 20:
                    if pygame.time.get_ticks() - self.timer > 5:
                        self.objects_alpha -= 5 * App.deltaTime
                        self.timer = pygame.time.get_ticks()
                else:
                    self.start_state = 5
                    
            case 5:
                self.objects_alpha = 0
                if pygame.time.get_ticks() - self.timer < 2000:
                    App.uiSurface.blit(App.assets.loading_icon, (App.dimentions[0] - (App.assets.loading_icon.get_width() + 20 ), App.dimentions[1] - (App.assets.loading_icon.get_height() + 20 ) ))
                else:
                    self.timer = pygame.time.get_ticks()
                    self.start_state = 6

            case 6:
                if pygame.time.get_ticks() - self.timer > 1500:
                    self.start_state = 7

            case 7:
                self.start_game = True
                self.played_once = True
                App.animations = animations_init(App)
                App.objects = GameObjects(App, real_time_mode=self.play_real_time_mode)
                App.game = Game(App, real_time_mode=self.play_real_time_mode)
            case 10: 
                # Init objects for custom night menu
                App.surface.fill((0, 0, 0))
                App.objects = GameObjects(App)
                self.start_state = 11

            case 11: # Custom night
                self.custom_night_menu.update(App)

            case 12: # Credits
                self.credits.update(App)

            case 13: # Extra!
                self.extras.update(App)

            case 100: # Cutscenes
                self.cutscene.update(App, self.inNight)
                if self.cutscene.finished:
                    self.init_menu_and_save_vars(App)
                    self.cutscenes_data[self.inNight - 1] = True
                    