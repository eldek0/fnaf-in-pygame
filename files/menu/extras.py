import pygame
from files.ui.Text import Text, Lock_to
from files.ui.button import Button
from files.animatronics.animatronics_main import AnimatronicsMain
from files.animations.sprites_animation import SpritesAnimation

class Extras:
    def __init__(self, App):
        space_between_texts = 40
        margin_y = -100
        margin_x = 40

        buttons_sprites = [App.assets.animatrionics_button, App.assets.jumpscares_button, App.assets.minigames_button, App.assets.real_time_button]
        self.buttons = []
        for i in range(len(buttons_sprites)):
            sprite:pygame.sprite.Sprite = buttons_sprites[i]
            button_size = sprite.get_rect()
            self.buttons.append(
                Button(
                    (margin_x, margin_y + button_size.h + space_between_texts*i), (button_size.w, button_size.h), sprite, lock_to="y"
                )
            )


        self.x_margin_elements = 500
        self.y_margin_elements = 30

        self.anim_main = AnimatronicsMain(App)

        anim_in_game:dict = self.anim_main.animatronics_in_game
        sprite = App.assets.sel_square
        button_size = sprite.get_rect()
        row_elements = 7
        self.select_animatronic_buttons = []
        self.select_jumpscare_animatronic_buttons = []
        self.keys_with_jumpscares = []
        for key in anim_in_game.keys():
            if self.anim_main.animatronics_in_game[key].jumpscare_animation:
                self.keys_with_jumpscares.append(key)

        # Add animatronics with jumpscares
        for i in range(len(self.keys_with_jumpscares)):
            if i < row_elements-1:
                pos = (self.x_margin_elements + 55*(i), self.y_margin_elements + 50)
            else:
                pos = (self.x_margin_elements + 55*(i-(row_elements-1)), self.y_margin_elements + 100)

            self.select_jumpscare_animatronic_buttons.append(
                Button(
                    pos, (button_size.w, button_size.h), sprite
                )
            )

        # Add every animatronics with image
        self.keys_imgs = []
        for key in anim_in_game.keys():
            if self.anim_main.animatronics_in_game[key].img_show:
                self.keys_imgs.append(key)

        for i in range(len(self.keys_imgs)):
            if i < row_elements-1:
                pos = (self.x_margin_elements + 55*(i), self.y_margin_elements + 50)
            else:
                pos = (self.x_margin_elements + 55*(i-(row_elements-1)), self.y_margin_elements + 100)

            self.select_animatronic_buttons.append(
                Button(
                    pos, (button_size.w, button_size.h), sprite
                )
            )

        row_elements = 3
        self.minigames_buttons = []
        t = App.assets.min_screenshots
        for i in range(len(t)):
            if i < row_elements-1:
                pos = (self.x_margin_elements + 200*(i), self.y_margin_elements + 150)
            else:
                pos = (self.x_margin_elements + 200*(i-(row_elements-1)), self.y_margin_elements + 350)
            texture = t[i]
            self.minigames_buttons.append(
                Button(
                    pos, (texture.get_width(), texture.get_height()), texture
                )
            )

        self.pressed_click = False
        self.pressed_key = False
        self.inOption = 1
        self.selectionButton = 0

    def update(self, App):
        surf:pygame.surface.Surface = App.uiSurface

        self.options_handler(App)

        tExtras = Text(App, "Extras", (0, 10), App.assets.ocr_font40, (255, 255, 255), "x")
        tExtras.draw(surf)
        
        for button in self.buttons:
            button.update(surf, App.mouse_hitbox)

        if self.inOption != 0:
            App.uiSurface.blit(App.assets.option_selected, (28, self.buttons[self.inOption-1].position[1] + 3))

        # Actions handler
        self.actions_handler(App)

        self.update_keys(App)

        App.menu.menu_exit(App)

    def actions_handler(self, App):
        click = pygame.mouse.get_pressed()
        for i in range(len(self.buttons)):
            if self.buttons[i].mouse_hovered and not self.pressed_click and i+1 != self.inOption:
                if click[0]:
                    self.change_option(App)
                    self.inOption = i+1
                
        self.pressed_click = click[0]
            
    def update_keys(self, App):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_DOWN]) and not self.pressed_key:
            self.change_option(App)
            self.inOption += 1
            self.pressed_key = True
            if self.inOption > len(self.buttons):
                self.inOption = 1

        elif (keys[pygame.K_UP]) and not self.pressed_key:
            self.change_option(App)
            self.inOption -= 1
            self.pressed_key = True
            if self.inOption < 1:
                self.inOption = len(self.buttons)
        
        if not keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            self.pressed_key = False

        return keys
    
    def change_option(self, App):
        self.selectionButton = 0
        pygame.mixer.Channel(5).stop()
        App.assets.blip1.play()
        self.reset_animations(App)

    def options_handler(self, App):
        surf:pygame.surface.SurfaceType = App.uiSurface
        match self.inOption:
            case 1:
                self.draw_anim(App, self.selectionButton)

                for i in range(len(self.select_animatronic_buttons)):
                    self.select_animatronic_buttons[i].update(surf, App.mouse_hitbox)
                    self.disp_number(App, i+1, self.select_animatronic_buttons[i].position)

                    if self.select_animatronic_buttons[i].mouse_hovered and pygame.mouse.get_pressed()[0] and not self.pressed_click:
                        self.selectionButton = i
                        self.reset_animations(App)
                        App.assets.blip1.play()
                        pygame.mixer.Channel(5).stop()
            case 2:
                self.jumpscare_update(App, self.selectionButton)

                for i in range(len(self.select_jumpscare_animatronic_buttons)):
                    self.select_jumpscare_animatronic_buttons[i].update(surf, App.mouse_hitbox)
                    self.disp_number(App, i+1, self.select_jumpscare_animatronic_buttons[i].position)

                    if self.select_jumpscare_animatronic_buttons[i].mouse_hovered and pygame.mouse.get_pressed()[0] and not self.pressed_click:
                        self.selectionButton = i
                        self.reset_animations(App)
                        pygame.mixer.Channel(5).stop()
            case 3:
                for i in range(len(self.buttons)):
                    button = self.minigames_buttons[i]
                    if button.mouse_hovered and pygame.mouse.get_pressed()[0]:
                        App.minigame.startMinigame(App, forceId=i)

                    
                    button.update(surf, App.mouse_hitbox)
            case 4:
                t = Text(App, "In this mode each hour", (self.x_margin_elements + 50, 300), App.assets.ocr_font20, (255, 255, 255))
                t.draw(surf)
                
                t2 = Text(App, "its equal to an hour in real life", (self.x_margin_elements + 20, 350), App.assets.ocr_font20, (255, 255, 255))
                t2.draw(surf)

                t3 = Text(App, "Have fun!", (self.x_margin_elements + 100, 400), App.assets.ocr_font30, (228, 158, 0))
                t3.draw(surf)
                
                if (self.buttons[3].mouse_hovered and pygame.mouse.get_pressed()[0] and not self.pressed_click) or (pygame.key.get_pressed()[pygame.K_RETURN] and not self.pressed_key):
                    App.menu.option_real_time()

    def disp_number(self, App, num:int, pos:tuple):
        x_extra = 0
        for i in range(len(str(num))):
            num_p = int(str(num)[i])
            if len(str(num)) > 1: x_extra = 9
            App.uiSurface.blit(App.assets.numbers[num_p], (pos[0] - (x_extra*(-1)**i) + 11, pos[1] + 7))
            x_extra += App.assets.numbers[num_p].get_width()

    def jumpscare_update(self, App, num):
        surf:pygame.surface.Surface = App.uiSurface
        jumpscareanim:SpritesAnimation = self.anim_main.animatronics_in_game[self.keys_with_jumpscares[num]].jumpscare_animation
        jumpscareanim.update(surf, App.deltaTime)

        if not pygame.mixer.Channel(5).get_busy() and jumpscareanim.sprite_num == 0:
            pygame.mixer.Channel(5).set_volume(1)
            pygame.mixer.Channel(5).play(App.assets.xScream1)

    def draw_anim(self, App, num):
        surf:pygame.surface.Surface = App.uiSurface
        img:pygame.surface.Surface = self.anim_main.animatronics_in_game[self.keys_imgs[num]].img_show

        text = str(self.keys_imgs[self.selectionButton]).capitalize().replace("_", " ")
        r = surf.get_rect()
        r.x += self.x_margin_elements
        r.y += self.y_margin_elements
        r.w -= self.x_margin_elements
        r.h -= self.y_margin_elements

        pos = Lock_to("x", (-50, self.y_margin_elements + 170), img.get_width(), img.get_height(), r)
        surf.blit(img, (r.x + pos[0], pos[1]))
        
        label = Text(App, text, (200, 330), App.assets.ocr_font40, (255, 255, 255), "x", lock_surf=r)
        label.draw(surf)

    def reset_animations(self, App): 
        App.animations.__init__(App)
        self.anim_main = AnimatronicsMain(App)