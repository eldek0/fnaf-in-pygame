import pygame, random

class Office:
    def __init__(self, App):
        self.position = [-240, 0]
        self.move_speed = 20
        self.office_sprite = App.assets.office1
        self.right_vent_button, self.left_vent_button = App.assets.right_vent_button_off, App.assets.left_vent_button_off
        self.right_vent_on, self.left_vent_on, self.hallway_on = False, False, False
        self.occupied_office = [False, False, False, False] # Hallway, Right vent, Left vent, office front

        # Audio variables
        self.attempting_right_vent_interact, self.attempting_left_vent_interact  = False, False
        self.attempting_hallway_interact, self.attempting_esteregg_interact = False, False

        self.animatronic_in_office = False

        self.bunny_x_initial_position, self.bunny_speed = App.dimentions[0] + 300, 5.5
        self.bunny_x_position = self.bunny_x_initial_position
        self.bunny_moving_left = True
        self.hallway_animatrionic_fade = False
        self.timer = pygame.time.get_ticks()
        self.hallway_animatrionic_coyote_time = 0
        
        self.camera_movement_act = [False, False] # Left and Right movement
        # Left and right movement hitbox
        self.move_left, self.move_right = pygame.Rect(0, 0, 300, App.dimentions[1]), pygame.Rect(App.dimentions[0] - 300, 0, 300, App.dimentions[1])

        self.bbg_show = False
        self.dwarq_show = False
        self.plastic_show = False
        self.random_num:int = 0

    def update(self, App, canInteract=True, draw=True, animate=True):
        if self.animatronic_in_office:
            canInteract = False
            App.objects.open_monitor_button.quit_camera(App)
        
        if canInteract or self.animatronic_in_office:
            self.camera_movement(App)

        self.check_eggs()

        if draw:
            self.draw_office(App)

        if canInteract:
            self.hallway_interact(App)

            self.right_vent_interact(App)

            self.left_vent_interact(App)

            self.easter_egg_interact(App)

        if draw:
            # Draw vent buttons
            App.surface.blit(self.right_vent_button, (1440 + self.position[0], 360))
            App.surface.blit(self.left_vent_button, (100 + self.position[0], 360))

            self.animatrionics_in_office(App)

            self.desk_update(App)
            self.desk_rewards(App)
            
            if not animate:
                App.animations.desk.animate = False

        self.animatronic_detect(App)
        if self.hallway_animatrionic_fade:
            App.animations.darkness.update(App.uiSurface, App.deltaTime)
            if not App.animations.darkness.is_animating:
                self.hallway_animatrionic_fade = False

    def draw_office(self, App):
        App.surface.blit(self.office_sprite, self.position)

        if self.dwarq_show:
            App.surface.blit(App.assets.DWARF, (300 + self.position[0], 0))
            if pygame.time.get_ticks() - self.timer > 6000:
                App.playing = False

        elif self.plastic_show:
            App.surface.blit(App.assets.plastic, (1050 + self.position[0], 0))

        if App.objects.open_monitor_button.inCamera: self.random_num = 0

    def desk_rewards(self, App):
        custom_nights_completed = App.menu.custom_night_menu.completed_nights

        x_sum = 470 + self.position[0]

        if custom_nights_completed[2]: # New and Shiny (Toy bonnie)
            App.surface.blit(App.assets.custom_night_rewards[5], (560+ x_sum, 470))

        if custom_nights_completed[6]: # Freddy's Circus (Freddy Fazbear)
            App.surface.blit(App.assets.custom_night_rewards[1], (170+ x_sum, 490))

        if custom_nights_completed[1]: # Double trouble (unlocks bonnie)
            App.surface.blit(App.assets.custom_night_rewards[2], (260 + x_sum, 480))

        if custom_nights_completed[4]: # Ladies Night (chica)
            App.surface.blit(App.assets.custom_night_rewards[3], (175+ x_sum, 526))

        if custom_nights_completed[5]: # Foxy Foxy (foxy)
            App.surface.blit(App.assets.custom_night_rewards[4], (320+ x_sum, 515))

        if custom_nights_completed[3]: # Night of Misfits (BB)
            App.surface.blit(App.assets.custom_night_rewards[6], (490+ x_sum, 520))

        if custom_nights_completed[7]: # Cupcake Challenge (chica's cupcake)
            App.surface.blit(App.assets.custom_night_rewards[0], (610+ x_sum, 510))

        if custom_nights_completed[8]: # Fazbear Fever (microphone)
            App.surface.blit(App.assets.custom_night_rewards[8], (360+ x_sum, 620))

        if custom_nights_completed[9]: # Golden Freddy (golden freddy)
            App.surface.blit(App.assets.custom_night_rewards[7], (720+ x_sum, 530))

    def animatrionics_in_office(self, App):
        mangle = App.objects.Animatronics.animatronics_in_game["MANGLE"]
        baloon_boy = App.objects.Animatronics.animatronics_in_game["BALOON_BOY"]
        golden_freddy = App.objects.Animatronics.animatronics_in_game["GOLDEN_FREDDY"]

        if mangle.locationId == -1 and not mangle.isBeingJumpscared():
            App.surface.blit(App.assets.office_mangle, (400 + self.position[0], 0))

        if baloon_boy.locationId == -1:
            App.surface.blit(App.assets.office_baloon_boy, (320 + self.position[0], 280))

        if golden_freddy.locationId == -1 and not golden_freddy.isBeingJumpscared():
            App.surface.blit(App.assets.office_golden_freddy, (320 + self.position[0], 280))

    def camera_movement(self, App):
        
        if App.mouse_hitbox.colliderect(self.move_left) and self.position[0] < 0:
            self.camera_movement_act[1] = True
            if self.camera_movement_act[0]:
                self.position[0] += self.move_speed * App.deltaTime
                if self.position[0] > 0:
                    self.position[0] = 0
        elif App.mouse_hitbox.colliderect(self.move_right) and self.position[0] > -abs(App.assets.office1.get_width() - App.dimentions[0]):
            self.camera_movement_act[0] = True
            if self.camera_movement_act[1]:
                self.position[0] -= self.move_speed * App.deltaTime
                if self.position[0] < -abs(App.assets.office1.get_width() - App.dimentions[0]) :
                    self.position[0] = -abs(App.assets.office1.get_width() - App.dimentions[0])

    def hallway_interact(self, App):
        baloon_boy = App.objects.Animatronics.animatronics_in_game["BALOON_BOY"]
        hallway_rect = pygame.Rect(self.position[0] + 560, 200, 490, 370)

        if self.hallway_on:
            self.office_sprite = App.assets.flash_offices[self.get_flashed_office(App)]
        else:
            self.office_sprite = App.assets.office1
            

        hallway_collide = App.mouse_hitbox.colliderect(hallway_rect)

        # Mouse click 
        mouse_click = pygame.mouse.get_pressed()
        ctrl_clicked = pygame.key.get_pressed()[pygame.K_LCTRL]
        
        cannot_interact = self.occupied_office[0] or App.objects.battery.charge == 0

        if hallway_collide or ctrl_clicked:
            if mouse_click[0] or ctrl_clicked:
                if not (cannot_interact or App.objects.battery.charge == 0  or baloon_boy.locationId == -1):
                    self.hallway_on = True

                else:
                    # Make an error sound
                    self.hallway_on = False
                    if not self.attempting_hallway_interact:
                        App.assets.error_sound.play()

                self.attempting_hallway_interact = True
                
        if (not hallway_collide or not mouse_click[0]) and not ctrl_clicked:
            self.attempting_hallway_interact = False
            self.hallway_on = False

    def right_vent_interact(self, App):
        baloon_boy = App.objects.Animatronics.animatronics_in_game["BALOON_BOY"]
        right_vent_rect = pygame.Rect(1450 + self.position[0], 390, 55, 60)

        colliding_button = App.mouse_hitbox.colliderect(right_vent_rect)
        
        # Mouse click 
        mouse_click = pygame.mouse.get_pressed()
        if self.right_vent_on:
            self.right_vent_button = App.assets.right_vent_button_on
        else: self.right_vent_button = App.assets.right_vent_button_off

        if colliding_button:
            if mouse_click[0]:
                if not (self.occupied_office[1] or App.objects.battery.charge == 0  or baloon_boy.locationId == -1):
                    self.office_sprite = App.assets.right_vent_offices[self.get_flashed_right_vent(App)]
                    self.right_vent_on = True
                else:
                    self.right_vent_on = False
                    # Make an error sound
                    if not self.attempting_right_vent_interact:
                        App.assets.error_sound.play()
                    
                self.attempting_right_vent_interact = True

        if not colliding_button or not mouse_click[0]:
            self.right_vent_on = False
            self.attempting_right_vent_interact = False

        if not self.right_vent_on and not self.left_vent_on and not self.hallway_on:
            self.office_sprite = App.assets.office1
            
    def left_vent_interact(self, App):
        baloon_boy = App.objects.Animatronics.animatronics_in_game["BALOON_BOY"]
        left_vent_rect = pygame.Rect(125 + self.position[0], 390, 55, 60)

        colliding_button = App.mouse_hitbox.colliderect(left_vent_rect)
        
        # Mouse click 
        mouse_click = pygame.mouse.get_pressed()
        if self.left_vent_on:
            self.left_vent_button = App.assets.left_vent_button_on
        else: self.left_vent_button = App.assets.left_vent_button_off

        if colliding_button:
            if mouse_click[0]:
                if not (self.occupied_office[2] or App.objects.battery.charge == 0  or baloon_boy.locationId == -1):
                    self.office_sprite = App.assets.left_vent_offices[self.get_flashed_left_vent(App)]
                    self.left_vent_on = True
                else:
                    self.left_vent_on = False
                    # Make an error sound
                    if not self.attempting_left_vent_interact:
                        App.assets.error_sound.play()
                    
                self.attempting_left_vent_interact = True

        if not colliding_button or not mouse_click[0]:
            self.left_vent_on = False
            self.attempting_left_vent_interact = False

        if not self.left_vent_on and not self.hallway_on and not self.right_vent_on:
            self.office_sprite = App.assets.office1

    def easter_egg_interact(self, App):
        """ Freddy's nose """
        easter_egg_rect = pygame.Rect(145 + self.position[0], 172, 10, 10)

        mouse_click = pygame.mouse.get_pressed()
        colliding_rect = App.mouse_hitbox.colliderect(easter_egg_rect)

        if colliding_rect:
            if mouse_click[0]:
                if not self.attempting_esteregg_interact:
                    App.assets.boop.play()
                    self.attempting_esteregg_interact = True

        if not colliding_rect or not mouse_click[0]:
            self.attempting_esteregg_interact = False

        #pygame.draw.rect(App.uiSurface, (200, 255, 100), easter_egg_rect)

    def check_eggs(self):
        if self.random_num > 9304 and self.random_num < 9600: 
            self.bbg_show = True
        elif self.random_num == 6161:
            self.dwarq_show = True
        elif self.random_num > 100 and self.random_num < 500:
            self.plastic_show = True
        else:
            self.bbg_show = False
            self.dwarq_show = False
            self.plastic_show = False

    def desk_update(self, App):
        App.animations.desk.position = [ self.position[0] + 560,App.dimentions[1] - 435]
        if self.bbg_show:
            App.surface.blit(App.assets.baloon_girl, (850 + self.position[0] , App.surface.get_height() - 100))
        App.animations.desk.update(App.surface, App.deltaTime)

    def get_flashed_office(self, App):
        ToyFreddy = App.objects.Animatronics.animatronics_in_game["TOY_FREDDY"]
        ToyChica = App.objects.Animatronics.animatronics_in_game["TOY_CHICA"]
        withered_freddy = App.objects.Animatronics.animatronics_in_game["WITHERED_FREDDY"]
        withered_bonnie = App.objects.Animatronics.animatronics_in_game["WITHERED_BONNIE"]
        foxy = App.objects.Animatronics.animatronics_in_game["FOXY"]
        mangle = App.objects.Animatronics.animatronics_in_game["MANGLE"]

        if ToyFreddy.locationId == 101:
            if ToyFreddy.secondPositionId == 1:
                return 3
            elif ToyFreddy.secondPositionId == 2:
                return 4
        elif withered_freddy.locationId == 101:
            return 6
        elif ToyChica.locationId == 101:
            return 1
        elif withered_bonnie.locationId == 101:
            if foxy.locationId == 101:
                return 9
            return 5
        elif mangle.locationId == 101:
            if foxy.locationId == 101:
                return 10
            return 2
        elif foxy.locationId == 101:
            return 7
        
        return 0

    def get_flashed_right_vent(self, App):
        ToyBunny = App.objects.Animatronics.animatronics_in_game["TOY_BONNIE"]
        Mangle = App.objects.Animatronics.animatronics_in_game["MANGLE"]
        if ToyBunny.locationId == 102:
            return 1
        elif Mangle.locationId == 102:
            return 2

        return 0

    def get_flashed_left_vent(self, App):
        ToyChica = App.objects.Animatronics.animatronics_in_game["TOY_CHICA"]
        BaloonBoy = App.objects.Animatronics.animatronics_in_game["BALOON_BOY"]
        if ToyChica.locationId == 103:
            return 1
        elif BaloonBoy.locationId == 103:
            return 2

        return 0

    def animatronic_detect(self, App):
        self.toy_bonnie_in_hall(App)
        animatrionic_in_hall = ["WITHERED_FREDDY", "WITHERED_BONNIE", "WITHERED_CHICA", "TOY_FREDDY"]

        baloon_boy = App.objects.Animatronics.animatronics_in_game["BALOON_BOY"]
        golden_freddy = App.objects.Animatronics.animatronics_in_game["GOLDEN_FREDDY"]

        if not (baloon_boy.locationId == -1 and golden_freddy.locationId == -1):
            for i in range(len(animatrionic_in_hall)):
                if App.objects.Animatronics.animatronics_in_game[animatrionic_in_hall[i]].aggresivity != 0:
                    self.withered_animatrionic_in_office(App, animatrionic_in_hall[i], i)
        

    def toy_bonnie_in_hall(self, App):
        ToyBunny = App.objects.Animatronics.animatronics_in_game["TOY_BONNIE"]

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
                ToyBunny.prepare_to_jumpscare(App)

            if App.objects.mask_button.inMask:  
                if pygame.time.get_ticks() - self.hallway_animatrionic_coyote_time > 4000:
                    App.animations.darkness.fade_screen()

                if self.bunny_moving_left:
                    self.bunny_x_position -= self.bunny_speed * App.deltaTime
                else:
                    self.bunny_x_position += self.bunny_speed * App.deltaTime

            if App.animations.darkness._isFading:
                if not ToyBunny._prepare_to_jumpscare:
                    ToyBunny.change_location_id(App, 0, forced=True)
                self.animatronic_in_office = False
                self.bunny_moving_left = True
                self.bunny_x_position =self.bunny_x_initial_position

    def withered_animatrionic_in_office(self, App, id_name:str, office_sprite_id:int):
        animatrionic = App.objects.Animatronics.animatronics_in_game[id_name]
        if animatrionic.locationId == 104 and not animatrionic.changing_position and not animatrionic._prepare_to_jumpscare:
            self.hallway_animatrionic_fade = True
            if not self.animatronic_in_office:
                self.timer = pygame.time.get_ticks()
            self.animatronic_in_office = True
        

        time_to_put_mask = 3000
        if self.animatronic_in_office and animatrionic.locationId == 104:
            self.office_sprite = App.assets.animatrionic_offices[office_sprite_id]
            if pygame.time.get_ticks() - self.timer > time_to_put_mask:
                if not App.objects.mask_button.inMask or App.objects.mask_button.quitting_mask:
                    animatrionic.prepare_to_jumpscare(App)
                    if pygame.time.get_ticks() - self.timer > time_to_put_mask:
                        App.animations.darkness.fade_screen()
                else:
                    if pygame.time.get_ticks() - self.timer > 1000:
                        App.animations.darkness.fade_screen()

            if App.animations.darkness._isFading:
                self.office_sprite = App.assets.office1
                self.animatronic_in_office = False
                if not animatrionic._prepare_to_jumpscare:
                    animatrionic.change_location_id(App, 0, forced=True)

    def random_number(self): 
        self.random_num = random.randint(0, 150_000)
        self.timer = pygame.time.get_ticks()