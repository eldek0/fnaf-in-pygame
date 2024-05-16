import pygame, random
from files.ui.button import Button
from files.game.game_objects import GameObjects
from files.game.game_controller import Game
from files.animations.animations_init import animations_init
from files.menu.custom_night import CustomNight
from files.menu.cutscene import Cutscene

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

        self.background_id = 0
        self.random_value_number = random.randint(500, 2000)
        self.random_value_number2 = random.randint(200, 800)
        self.return_normal_background = False

        self.objects_alpha = 0

        self.background_alpha = 255

        self.start_state = 0 # if 100 will try entering a cutscene

        if App.debug: self.start_state = 7

        self.timer = pygame.time.get_ticks()
        self.pressed_timer = pygame.time.get_ticks()

        self.start_game = False

        self.static_with_change = False

        self.option_ready_to_select = 0

        self.music_started = False

        self.essentials_variables(App)

        
        
    def essentials_variables(self, App):
        self.custom_night_menu = CustomNight(App)

        self.cutscene = Cutscene(App)

        self.cutscenes_data = [True, True, True, False]

        self.inNight = 5
        self.nightToPlay = 5

        self.played_once = True

    def static_animation(self, App):
        App.animations.static_anim_1.update(App.uiSurface)
        App.animations.static_anim_1.alpha = 160

        # More static animation
        App.animations.static_stripes_animation5.update(App, App.uiSurface)
        App.animations.random_static_animation.update(App.uiSurface)

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

        if self.start_state == 0:
            self.change_background(App)
            self.music(App)
            self.reset_data_option(App)
            if not self.music_started:
                self.start_music(App)
                self.music_started = True

        if self.start_state < 2:
            
            App.assets.background_menu[self.background_id].set_alpha(self.background_alpha)
            App.uiSurface.blit(App.assets.background_menu[self.background_id], (0,0))
            
            self.static_animation(App)

            # Labels
            App.uiSurface.blit(App.assets.fnaf_title, (80, 30))
            dims = App.assets.scott_credits.get_rect()
            App.uiSurface.blit(App.assets.scott_credits, (App.dimentions[0] - dims.w - 10, App.dimentions[1] - dims.h - 20))
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

            self.draw_menu_stars(App)

            #print(mouse)
            # Mouse option
            if self.start_state == 0:
                if self.new_game_button.mouse_hovered:
                    self.option_to_select(App, lambda:self.option_1(App), 1)

                elif self.continue_button.mouse_hovered:
                    if self.played_once:
                        self.option_to_select(App, lambda:self.option_2(), 2)

                elif self.night_six_button.mouse_hovered and self.inNight >= 6:
                    if self.played_once:
                        self.option_to_select(App, lambda:self.option_3(), 3)

                elif self.custom_night_button.mouse_hovered and self.inNight >= 7:
                    if self.played_once:
                        self.option_to_select(App, lambda:self.option_4(), 4)

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

    def option_to_select(self,App, func, option:int):
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            self.option = option
            if self.option_ready_to_select == option:
                func()


        if self.option == option and not self.option_ready_to_select == option and not mouse[0]:
            self.option_ready_to_select = option
            App.assets.blip1.play()


    def static(self, App):
        if self.static_with_change:
            App.animations.static_anim_2.update(App.uiSurface)

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
                self.objects_alpha += 1
                self.timer = pygame.time.get_ticks()
                App.animations.fade_effect.stop_effect()
        else:
            if pygame.time.get_ticks() - self.timer > 4000:
                App.animations.fade_effect.continue_effect(out_effect=False)
                App.animations.fade_effect.update(App.uiSurface)

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

        self.__init__(App)

        self.inNight = night
        self.played_once = played_once
        self.cutscenes_data = cutscenes_data
        self.custom_night_menu = custom_night


    def show_night(self, App):
        App.assets.nights_12am[self.nightToPlay - 1].set_alpha(self.objects_alpha)
        night_dims = App.assets.nights_12am[self.nightToPlay - 1].get_rect()
        App.uiSurface.blit(App.assets.nights_12am[self.nightToPlay - 1], (App.dimentions[0] / 2 - night_dims.w / 2, App.dimentions[1] / 2 - night_dims.h / 2))

        match self.start_state:
            case 2:
                pygame.mixer.music.unload()
                App.animations.fade_effect.update(App.uiSurface)
                App.animations.static_anim_2.update(App.uiSurface)

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
                        self.objects_alpha -= 5
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
                App.objects = GameObjects(App)
                App.game = Game(App)
            case 10: 
                # Init objects for custom night menu
                App.surface.fill((0, 0, 0))
                App.objects = GameObjects(App)
                self.start_state = 11

            case 11: # Custom night
                self.custom_night_menu.update(App)

            case 100: # Cutscenes
                self.cutscene.update(App, self.inNight)
                if self.cutscene.finished:
                    self.init_menu_and_save_vars(App)
                    self.cutscenes_data[self.inNight - 1] = True
                    