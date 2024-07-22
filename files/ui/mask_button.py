from files.ui.button import Button

class MaskButton:
    def __init__(self, App, draw_box=False):
        spr_mask_dims = [App.assets.mask_button.get_width(), App.assets.mask_button.get_height()]
        self.mask_button = Button((20, App.dimentions[1] - spr_mask_dims[1]- 20),  [spr_mask_dims[0], spr_mask_dims[1] + 500], sprite=App.assets.mask_button, draw_box=False)
        self.inMask = False
        self.mask_being_pressed = False
        self.quitting_mask = False
        self.entering_mask = False

    def update(self, App, canInteract=True):
        self.mask_button.update(App.uiSurface, App.mouse_hitbox)
        if canInteract and self.canEnter(App):
            if self.inMask and not self.quitting_mask:
                App.animations.mask.update(App.surface, App.deltaTime)
                App.animations.mask_animation.update(App.deltaTime)
                pos_sum = App.animations.mask_animation.position
                App.surface.blit(App.assets.mask_sprites[9], (-100 + pos_sum[0], -100 + pos_sum[1]))

            self.animation(App, canInteract=canInteract)

        if not canInteract:
            self.animation(App, canInteract=False)

        if App.animations.mask.sprite_num == 0 and self.quitting_mask:
            self.quitting_mask = False

    def canEnter(self, App): return not (App.objects.open_monitor_button.entering_camera or App.objects.open_monitor_button.inCamera or App.objects.open_monitor_button.quitting_camera)

    def animation(self, App, canInteract=True):
        if not self.inMask:
            if (self.mask_button.mouse_hovered and canInteract) or self.entering_mask:
                if not self.mask_being_pressed:
                    self.entering_mask = True
                    App.animations.mask.update(App.surface, App.deltaTime)

                    # Get in mask
                    if App.animations.mask.sprite_num == len(App.animations.mask.sprites) - 1:
                        self.inMask = True
                        self.entering_mask = False
                        self.mask_being_pressed = True
                        App.animations.mask.desactivate = True
                        App.assets.mask_on_sound.play()
            else:
                self.mask_being_pressed = False

        else:
            if self.mask_button.mouse_hovered:
                if not self.mask_being_pressed:
                    self.quitting_mask = True

            else:
                self.mask_being_pressed = False

            if self.quitting_mask:
                App.animations.mask.desactivate = False
                App.animations.mask.update(App.surface, App.deltaTime, reversed=True)

                # Get off mask
                if App.animations.mask.sprite_num == 0:
                    self.inMask = False
                    self.mask_being_pressed = True
                    self.quitting_mask = False
                    App.assets.mask_off_sound.play()