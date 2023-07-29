import pygame
from files.ui.button import Button

class CustomNight:
    def __init__(self, App):
        self.animatrionics_data = {}
        self.icons_gotten = False
        self.ready_button = Button(
            position=(App.dimentions[0] - 200, App.dimentions[1] - 300), sprite=App.assets.ready_button, 
            dimentions=(App.assets.ready_button.get_width(), App.assets.ready_button.get_height()))

    def get_animatrionics_icons(self, App):
        self.animatronics = App.objects.Animatronics.animatronics_in_game
        self.animatronics_keys = list(self.animatronics.keys())
        self.animatronics_keys.remove("PUPPET")
        print(self.animatronics_keys)
        for key in self.animatronics_keys:
            self.animatrionics_data[key] = {
                "index":self.animatronics[key].custom_index,
                "aggresive":10
            }

    def update(self, App):
        if not self.icons_gotten:
            self.get_animatrionics_icons(App)
            self.icons_gotten = True

        App.surface.fill((0, 0, 0))

        self.draw_animatrionics_icons(App, 60)
        self.draw_animatrionics_icons(App, 360, _range=(5, 10))

        self.ready_button.update(App.surface, App.mouse_hitbox)

        mouse = pygame.mouse.get_pressed()

        if self.ready_button.mouse_hovered and mouse[0]:
            App.menu.start_state = 2

    def draw_animatrionics_icons(self, App, y_position, _range=(0, 5)):
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
            mouse = pygame.mouse.get_pressed()

            # Right button
            right_button_dims = App.assets.arrow_right.get_rect()
            right_button = Button(
                position=(x_pos, y_position + 210),
                dimentions=(right_button_dims.w, right_button_dims.h),
                sprite=App.assets.arrow_right
            )
            right_button.update(App.surface, App.mouse_hitbox)

            if right_button.mouse_hovered and mouse[0]:
                self.animatrionics_data[key]["aggresive"] -= 1
                if self.animatrionics_data[key]["aggresive"] < 0: self.animatrionics_data[key]["aggresive"] = 0

            # Left button
            left_button_dims = App.assets.arrow_left.get_rect()
            left_button = Button(
                position=(x_pos + 100, y_position + 210),
                dimentions=(left_button_dims.w, left_button_dims.h),
                sprite=App.assets.arrow_left
            )
            left_button.update(App.surface, App.mouse_hitbox)

            if left_button.mouse_hovered and mouse[0]:
                self.animatrionics_data[key]["aggresive"] += 1
                if self.animatrionics_data[key]["aggresive"] > 20: self.animatrionics_data[key]["aggresive"] = 20

            x_extra = 0
            # Draw numbers 
            for num in str(abs(aggresive)):
                App.surface.blit(App.assets.numbers2[int(num)], (x_pos + 50 + x_extra, y_position + 215))
                x_extra += 20