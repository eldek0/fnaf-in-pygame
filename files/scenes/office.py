import pygame

class Office:
    def __init__(self, App):
        self.position = [0, 0]
        self.move_speed = 10
        self.office_sprite = App.assets.office1
        self.right_vent_button, self.left_vent_button = App.assets.right_vent_button_off, App.assets.left_vent_button_off
        self.right_vent_on, self.left_vent_on, self.hallway_on = False, False, False
        self.occupied_office = [False, False, False, False] # Hallway, Right vent, Left vent, office front

        # Audio variables
        self.attempting_right_vent_interact, self.attempting_left_vent_interact  = False, False
        self.attempting_hallway_interact = False

        self.animatronic_in_office = False

        self.bunny_x_initial_position, self.bunny_speed = App.dimentions[0] + 300, 4
        self.bunny_x_position = self.bunny_x_initial_position
        self.bunny_moving_left = True
        self.hallway_animatrionic_fade = False
        self.timer = pygame.time.get_ticks()
        self.hallway_animatrionic_coyote_time = 0

    def update(self, App, canInteract=True, draw=True):
        if self.animatronic_in_office:
            canInteract = False
        
        if canInteract:
            self.camera_movement(App)

        if draw:
            App.surface.blit(self.office_sprite, self.position)

        if canInteract:
            self.hallway_interact(App)

            self.right_vent_interact(App)

            self.left_vent_interact(App)

        if draw:
            # Draw vent buttons
            App.surface.blit(self.right_vent_button, (1440 + self.position[0], 360))
            App.surface.blit(self.left_vent_button, (100 + self.position[0], 360))

            self.desk_update(App)

        self.animatronic_detect(App)
        if self.hallway_animatrionic_fade:
            App.animations.darkness.update(App)
            if not App.animations.darkness.is_animating:
                print("desactivated")
                self.hallway_animatrionic_fade = False

    def camera_movement(self, App):
        move_left, move_right = pygame.Rect(0, 0, 300, App.dimentions[1]), pygame.Rect(App.dimentions[0] - 300, 0, 300, App.dimentions[1])
        
        if App.mouse_hitbox.colliderect(move_left) and self.position[0] < 0:
            self.position[0] += self.move_speed
            if self.position[0] > 0:
                self.position[0] = 0
        if App.mouse_hitbox.colliderect(move_right) and self.position[0] > -abs(App.assets.office1.get_width() - App.dimentions[0]) :
            self.position[0] -= self.move_speed
            if self.position[0] < -abs(App.assets.office1.get_width() - App.dimentions[0]) :
                self.position[0] = -abs(App.assets.office1.get_width() - App.dimentions[0])

    def hallway_interact(self, App):
        hallway_rect = pygame.Rect(self.position[0] + 560, 200, 490, 370)

        if self.hallway_on:
            self.office_sprite = self.get_flashed_office(App)
        else:
            self.office_sprite = App.assets.office1

        # Mouse click 
        mouse_click = pygame.mouse.get_pressed()
        if App.mouse_hitbox.colliderect(hallway_rect):
            if mouse_click[0]:
                if not (self.occupied_office[0] or App.objects.battery.charge == 0):
                    self.hallway_on = True
                    if not self.attempting_hallway_interact:
                        App.assets.buzzlight.play()

                else:
                    # Make an error sound
                    self.hallway_on = False
                    if not self.attempting_hallway_interact:
                        App.assets.error_sound.play()

                self.attempting_hallway_interact = True
                
        if not App.mouse_hitbox.colliderect(hallway_rect) or not mouse_click[0]:
            self.hallway_on = False
            if self.attempting_hallway_interact:
                App.assets.buzzlight.stop()
            self.attempting_hallway_interact = False

    def right_vent_interact(self, App):
        right_vent_rect = pygame.Rect(1450 + self.position[0], 390, 55, 60)

        colliding_button = App.mouse_hitbox.colliderect(right_vent_rect)
        
        # Mouse click 
        mouse_click = pygame.mouse.get_pressed()
        if self.right_vent_on:
            self.right_vent_button = App.assets.right_vent_button_on
        else: self.right_vent_button = App.assets.right_vent_button_off

        if colliding_button:
            if mouse_click[0]:
                if not (self.occupied_office[1] or App.objects.battery.charge == 0):
                    self.office_sprite = self.get_flashed_right_vent(App)
                    self.right_vent_on = True
                    if not self.attempting_right_vent_interact:
                        App.assets.buzzlight.play()
                else:
                    App.assets.buzzlight.stop()
                    self.right_vent_on = False
                    # Make an error sound
                    if not self.attempting_right_vent_interact:
                        App.assets.error_sound.play()
                    
                self.attempting_right_vent_interact = True

        if not colliding_button or not mouse_click[0]:
            if self.right_vent_on:
                App.assets.buzzlight.stop()
                self.office_sprite = App.assets.office1
                self.right_vent_on = False
            self.attempting_right_vent_interact = False
            
    def left_vent_interact(self, App):
        left_vent_rect = pygame.Rect(125 + self.position[0], 390, 55, 60)

        colliding_button = App.mouse_hitbox.colliderect(left_vent_rect)
        
        # Mouse click 
        mouse_click = pygame.mouse.get_pressed()
        if self.left_vent_on:
            self.left_vent_button = App.assets.left_vent_button_on
        else: self.left_vent_button = App.assets.left_vent_button_off

        if colliding_button:
            if mouse_click[0]:
                if not (self.occupied_office[2] or App.objects.battery.charge == 0):
                    self.office_sprite = self.get_flashed_left_vent(App)
                    self.left_vent_on = True
                    if not self.attempting_left_vent_interact:
                        App.assets.buzzlight.play()
                else:
                    App.assets.buzzlight.stop()
                    self.left_vent_on = False
                    # Make an error sound
                    if not self.attempting_left_vent_interact:
                        App.assets.error_sound.play()
                    
                self.attempting_left_vent_interact = True

        if not colliding_button or not mouse_click[0]:
            if self.left_vent_on:
                App.assets.buzzlight.stop()
                self.office_sprite = App.assets.office1
                self.left_vent_on = False
            self.attempting_left_vent_interact = False

    def desk_update(self, App):
        App.animations.desk.position = [ self.position[0] + 560,App.dimentions[1] - 435]
        App.animations.desk.update(App.surface)

    def get_flashed_office(self, App):
        ToyFreddy = App.objects.Animatronics.animatronics_in_game["TOY_FREDDY"]
        ToyChica = App.objects.Animatronics.animatronics_in_game["TOY_CHICA"]
        withered_freddy = App.objects.Animatronics.animatronics_in_game["WITHERED_FREDDY"]
        withered_bonnie = App.objects.Animatronics.animatronics_in_game["WITHERED_BONNIE"]

        if ToyFreddy.locationId == 101:
            return App.assets.flash_offices[3]
        elif ToyFreddy.locationId == 101 and True==True: #TODO
            return App.assets.flash_offices[4]
        elif withered_freddy.locationId == 101:
            return App.assets.flash_offices[6]
        elif ToyChica.locationId == 101:
            return App.assets.flash_offices[1]
        elif withered_bonnie.locationId == 101:
            if withered_bonnie.secondPositionId == 1:
                return App.assets.flash_offices[5]
            elif withered_bonnie.secondPositionId == 1:
                # If foxy is in the hallway
                return App.assets.flash_offices[9]
        
        return App.assets.flash_offices[0]

    def get_flashed_right_vent(self, App):
        ToyBunny = App.objects.Animatronics.animatronics_in_game["TOY_BUNNY"]
        if ToyBunny.locationId == 102:
            return App.assets.right_vent_offices[1]

        return App.assets.right_vent_offices[0]

    def get_flashed_left_vent(self, App):
        ToyChica = App.objects.Animatronics.animatronics_in_game["TOY_CHICA"]
        if ToyChica.locationId == 103:
            return App.assets.left_vent_offices[1]

        return App.assets.left_vent_offices[0]

    def animatronic_detect(self, App):
        self.toy_bunny(App)
        animatrionic_in_hall = ["WITHERED_FREDDY", "WITHERED_BONNIE"]

        for i in range(len(animatrionic_in_hall)):
            self.withered_animatrionic_in_office(App, animatrionic_in_hall[i], i)
        

    def toy_bunny(self, App):
        ToyBunny = App.objects.Animatronics.animatronics_in_game["TOY_BUNNY"]

        if ToyBunny.locationId == 104 and not ToyBunny.changing_position and not ToyBunny._prepare_to_jumpscare:
            if not self.animatronic_in_office:
                self.timer = pygame.time.get_ticks()
                self.hallway_animatrionic_coyote_time = pygame.time.get_ticks()
            self.animatronic_in_office = True
            self.hallway_animatrionic_fade = True

        if self.animatronic_in_office and ToyBunny.locationId == 104:
            if not App.objects.mask_button.inMask:
                self.hallway_animatrionic_coyote_time = pygame.time.get_ticks()

            if not App.animations.darkness._isFading and App.objects.mask_button.inMask:
                App.surface.blit(App.assets.office_bunny, (self.bunny_x_position, 0))

            position_dimension = App.dimentions[0]/2 - App.assets.office_bunny.get_width()/2

            if self.bunny_x_position < position_dimension and self.bunny_moving_left:
                self.bunny_moving_left = False

            if pygame.time.get_ticks() - self.timer > 3000 and (not App.objects.mask_button.inMask or App.animations.darkness._isFading):
                App.animations.darkness.fade_screen()
                ToyBunny.prepare_to_jumpscare()

            if App.objects.mask_button.inMask:  
                if pygame.time.get_ticks() - self.hallway_animatrionic_coyote_time > 6000:
                    App.animations.darkness.fade_screen()

                if self.bunny_moving_left:
                    self.bunny_x_position -= self.bunny_speed
                else:
                    self.bunny_x_position += self.bunny_speed

            if App.animations.darkness._isFading:
                if not ToyBunny._prepare_to_jumpscare:
                    ToyBunny.change_location_id(App, 3)
                self.animatronic_in_office = False
                self.bunny_moving_left = True
                self.bunny_x_position =self.bunny_x_initial_position

    def withered_animatrionic_in_office(self, App, id_name:str, office_sprite_id:int, rest_location:int):
        animatrionic = App.objects.Animatronics.animatronics_in_game[id_name]
        if animatrionic.locationId == 104 and not animatrionic.changing_position and not animatrionic._prepare_to_jumpscare:
            self.hallway_animatrionic_fade = True
            if not self.animatronic_in_office:
                self.timer = pygame.time.get_ticks()
            self.animatronic_in_office = True
        

        if self.animatronic_in_office and animatrionic.locationId == 104:
            self.office_sprite = App.assets.animatrionic_offices[office_sprite_id]
            if pygame.time.get_ticks() - self.timer > 1000:
                if not App.objects.mask_button.inMask or App.objects.mask_button.quitting_mask:
                    animatrionic.prepare_to_jumpscare()
                    if pygame.time.get_ticks() - self.timer > 1000 + 2000:
                        App.animations.darkness.fade_screen()
                else:
                    if pygame.time.get_ticks() - self.timer > 1000 + 4000:
                        App.animations.darkness.fade_screen()

            if App.animations.darkness._isFading:
                self.office_sprite = App.assets.office1
                self.animatronic_in_office = False
                if not animatrionic._prepare_to_jumpscare:
                    animatrionic.change_location_id(App, rest_location)