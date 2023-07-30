import pygame
from files.ui.button import Button
from files.menu.modes_data import modes_data

class CustomNight:
    def __init__(self, App):
        self.animatrionics_data = {}
        self.icons_gotten = False
        self.ready_button = Button(
            position=(App.dimentions[0] - 200, App.dimentions[1] - 80), sprite=App.assets.ready_button, 
            dimentions=(App.assets.ready_button.get_width(), App.assets.ready_button.get_height())
            )

        self.right_button = Button(
            position=((App.dimentions[0] - 50)/2 - 250, App.dimentions[1] - 80), sprite=App.assets.arrow_right2, 
            dimentions=(App.assets.arrow_right2.get_width(), App.assets.arrow_right2.get_height())
            )

        self.left_button = Button(
            position=((App.dimentions[0] - 50)/2 + 250, App.dimentions[1] - 80), sprite=App.assets.arrow_left2, 
            dimentions=(App.assets.arrow_left2.get_width(), App.assets.arrow_left2.get_height())
            )

        self.modes = []
        self.timer = pygame.time.get_ticks()
        self.click_ = True
        self.mode_index = 0
        self.completed_nights = [
            False, False, False, False, False,
            False, False, False, False, False
        ]
        

    def set_modes(self, App):
        for i in range(10):
            # modes data
            modes_data_dict = modes_data(i+1, self.get_aggresiveness())

            self.modes.append(
                {"name":App.assets.modes_labels[i], "data":modes_data_dict}
            )

    def get_animatrionics_icons(self, App):
        self.animatronics = App.objects.Animatronics.animatronics_in_game
        self.animatronics_keys = list(self.animatronics.keys())
        self.animatronics_keys.remove("PUPPET")
        
        for key in self.animatronics_keys:
            self.animatrionics_data[key] = {
                "index":self.animatronics[key].custom_index,
                "aggresive":10
            }

    def update(self, App):
        if not self.icons_gotten:
            self.get_animatrionics_icons(App)
            self.set_modes(App)
            self.icons_gotten = True

        App.surface.fill((0, 0, 0))

        App.surface.blit(App.assets.custom_night_title, (100, 30))

        dims = App.assets.custom_night_level_info.get_rect()
        App.surface.blit(App.assets.custom_night_level_info, (App.dimentions[0]/2 - dims.w/2, 630))

        self.draw_animatrionics_icons(App, 100)
        self.draw_animatrionics_icons(App, 350, _range=(5, 10), row=1)

        self.ready_button.update(App.surface, App.mouse_hitbox)

        mouse = pygame.mouse.get_pressed()

        if self.ready_button.mouse_hovered and mouse[0]:
            App.menu.start_state = 2

        self.check_in_mode(App)
        self.draw_mode_buttons(App)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            App.menu.start_state = 0
            App.menu.static_with_change = True
            

    def check_in_mode(self, App):
        aggresive_animatrionics = self.get_aggresiveness()
        for i in range(len(self.modes)):
            if aggresive_animatrionics == self.modes[i]["data"]:
                dims = self.modes[i]["name"].get_rect()
                App.surface.blit(self.modes[i]["name"], (App.dimentions[0]/2 - dims.w/2, App.dimentions[1] - 80))

                if self.completed_nights[i]:
                    App.surface.blit(App.assets.star, ((App.dimentions[0] - 50)/2 - 310, App.dimentions[1] - 80) )
                break
                    
    def get_aggresiveness(self):
        # Get only animatrionics aggresiveness
        aggresive_animatrionics = {}
        for key in self.animatronics_keys:
            aggresive_animatrionics[key] = self.animatrionics_data[key]["aggresive"]

        return aggresive_animatrionics

    def draw_mode_buttons(self, App):
        mouse = pygame.mouse.get_pressed()
        self.right_button.update(App.surface, App.mouse_hitbox)
        self.left_button.update(App.surface, App.mouse_hitbox)
        
        if self.right_button.mouse_hovered and mouse[0] and self.click_:
            self.mode_index += 1
            if self.mode_index > len(self.modes) -1:
                self.mode_index = 0

        if self.left_button.mouse_hovered and mouse[0] and self.click_:
            self.mode_index -= 1
            if self.mode_index < 0:
                self.mode_index = len(self.modes) - 1

        if (self.right_button.mouse_hovered or self.left_button.mouse_hovered) and mouse[0] and self.click_:
            for key in self.animatronics_keys:
                self.animatrionics_data[key]["aggresive"] = self.modes[self.mode_index]["data"][key]
            App.assets.coin_sound.play()
            self.click_ = False

    def draw_animatrionics_icons(self, App, y_position, _range=(0, 5), row=0):
        mouse = pygame.mouse.get_pressed()

        for i in range(_range[0], _range[1]):
            # ~ ~ ICON AND LABEL ~ ~
            key = self.animatronics_keys[i]
            index = self.animatrionics_data[key]["index"]
            x_pos = 100 + (105 + 70)*((i - _range[0]))
            icon = App.assets.animatrionic_icons[index]
            label = App.assets.animatrionic_labels[index]
            icon_dims = icon.get_rect()
            label_dims = label.get_rect()
            
            App.surface.blit(icon, (x_pos, y_position))
            App.surface.blit(label, (x_pos + icon_dims.w/2 - label_dims.w/2, y_position + 130))

            # ~ ~ aggresive SLIDER ~ ~
            aggresive = self.animatrionics_data[key]["aggresive"]

            # Right button
            right_button_dims = App.assets.arrow_right.get_rect()
            right_button = Button(
                position=(x_pos, y_position + 170 + 40*row),
                dimentions=(right_button_dims.w, right_button_dims.h),
                sprite=App.assets.arrow_right
            )
            right_button.update(App.surface, App.mouse_hitbox)

            if right_button.mouse_hovered and mouse[0] and self.click_:
                self.animatrionics_data[key]["aggresive"] -= 1
                if self.animatrionics_data[key]["aggresive"] < 0: self.animatrionics_data[key]["aggresive"] = 0
                App.assets.coin_sound.play()
                self.click_ = False

            # Left button
            left_button_dims = App.assets.arrow_left.get_rect()
            left_button = Button(
                position=(x_pos + 100, y_position + 170 + 40*row),
                dimentions=(left_button_dims.w, left_button_dims.h),
                sprite=App.assets.arrow_left
            )
            left_button.update(App.surface, App.mouse_hitbox)

            if left_button.mouse_hovered and mouse[0] and self.click_:
                self.animatrionics_data[key]["aggresive"] += 1
                if self.animatrionics_data[key]["aggresive"] > 20: self.animatrionics_data[key]["aggresive"] = 20
                App.assets.coin_sound.play()
                self.click_ = False

            x_extra = 0
            # Draw numbers 
            for num in str(abs(aggresive)):
                App.surface.blit(App.assets.numbers2[int(num)], (x_pos + 50 + x_extra, y_position + 175 + 40*row))
                x_extra += 20

        if not mouse[0]:
            self.click_ = True