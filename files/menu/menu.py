import pygame, random
from files.ui.button import Button
from files.game.game_objects import GameObjects
from files.game.game_controller import Game
from files.animations.animations_init import animations_init

class Menu:
    def __init__(self, App): 
        self.option:bool = True # What button is the mouse hovering

        new_game_dims = App.assets.new_game_option.get_rect()
        self.new_game_button = Button((80, 370), (new_game_dims.width, new_game_dims.height), App.assets.new_game_option)

        continue_dims = App.assets.continue_option.get_rect()
        self.continue_button = Button((80, 430), (continue_dims.width, continue_dims.height), App.assets.continue_option)

        self.background_id = 0
        self.random_value_number = random.randint(500, 2000)
        self.random_value_number2 = random.randint(200, 800)
        self.return_normal_background = False

        self.objects_alpha = 0

        self.background_alpha = 255

        self.start_state = 0

        self.timer = pygame.time.get_ticks()

        self.inNight = 1

        self.start_game = False

        self.static_with_change = False

        self.played_once = False

        pygame.mixer.music.load(App.assets.background_music_menu)
        pygame.mixer.music.play(-1)

    def static_animation(self, App):
        App.animations.static_anim_1.update(App.surface)
        App.animations.static_anim_1.alpha = 100

        # More static animation
        App.animations.static_stripes_animation.update(App)
        App.animations.static_stripes_animation2.update(App)
        App.animations.static_stripes_animation3.update(App)
        App.animations.static_stripes_animation4.update(App)

    def update(self, App):
        if self.start_state == 0:
            self.change_background(App)

        if self.start_state < 2:
            
            App.assets.background_menu[self.background_id].set_alpha(self.background_alpha)
            App.surface.blit(App.assets.background_menu[self.background_id], (0,0))
            
            self.static_animation(App)

            # Labels
            App.surface.blit(App.assets.fnaf_title, (80, 30))
            self.new_game_button.update(App.surface, App.mouse_hitbox)
            self.continue_button.update(App.surface, App.mouse_hitbox)

            mouse = pygame.mouse.get_pressed()
            #print(mouse)
            # Mouse option
            if self.new_game_button.mouse_hovered:
                self.option = True
                if mouse[0]:
                    self.start_state = 1
            elif self.continue_button.mouse_hovered:
                if self.played_once:
                    self.option = False
                    if mouse[0]:
                        pygame.mixer.music.unload()
                        self.start_state = 2
                        self.objects_alpha = 255

            if self.option:
                App.surface.blit(App.assets.option_selected, (28, 373))
            else:
                App.surface.blit(App.assets.option_selected, (28, 433))

        if self.start_state > 0:
            self.begin_game(App)

        self.static(App)

    def static(self, App):
        if self.static_with_change:
            App.animations.static_anim_2.update(App.surface)

            if App.animations.static_anim_2.sprite_num == len(App.animations.static_anim_2.sprites) - 1:
                App.animations.static_anim_2.sprite_num = 0
                App.assets.camera_sound_1.play()
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
            self.background_alpha = 24*choice
            self.random_value_number2 = random.randint(200, 800)

    def begin_game(self, App):
        if self.start_state == 1:
            self.show_newspaper(App)
        elif self.start_state >= 2:
            self.show_night(App)

    def show_newspaper(self, App):
        App.assets.newspaper.set_alpha(self.objects_alpha)
        App.surface.blit(App.assets.newspaper, (0, 0))

        if self.objects_alpha < 255:
            if pygame.time.get_ticks() - self.timer > 5:
                self.objects_alpha += 1
                self.timer = pygame.time.get_ticks()
        else:
            if pygame.time.get_ticks() - self.timer > 4000:
                App.animations.darkness_reversed.fade_screen()
                App.animations.darkness_reversed.update(App)

                if App.animations.darkness_reversed.fade_alpha > 240:
                    pygame.mixer.music.unload()
                    self.start_state += 1

                

    def show_night(self, App):
        App.assets.nights_12am[self.inNight - 1].set_alpha(self.objects_alpha)
        night_dims = App.assets.nights_12am[self.inNight - 1].get_rect()
        App.surface.blit(App.assets.nights_12am[self.inNight - 1], (App.dimentions[0] / 2 - night_dims.w / 2, App.dimentions[1] / 2 - night_dims.h / 2))

        match self.start_state:
            case 2:
                App.animations.darkness_reversed.update(App)
                App.animations.static_anim_2.update(App.surface)

                if App.animations.static_anim_2.sprite_num == len(App.animations.static_anim_2.sprites) - 1:
                    self.timer = pygame.time.get_ticks()
                    App.animations.static_anim_2.sprite_num = 0
                    App.assets.camera_sound_1.play()
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
                if pygame.time.get_ticks() - self.timer < 4000:
                    App.surface.blit(App.assets.loading_icon, (App.dimentions[0] - (App.assets.loading_icon.get_width() + 20 ), App.dimentions[1] - (App.assets.loading_icon.get_height() + 20 ) ))
                else:
                    self.timer = pygame.time.get_ticks()
                    self.start_state = 6

            case 6:
                if pygame.time.get_ticks() - self.timer > 3000:
                    self.start_state = 7

            case 7:
                self.start_game = True
                self.played_once = True
                App.animations = animations_init(App)
                App.objects = GameObjects(App)
                App.game = Game(App)