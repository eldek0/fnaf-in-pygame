import pygame, random

from files.ui.button import Button

class Camera:
    def __init__(self, App):
        self.inCameraRoom:int = 1
        self.camera_buttons_positions = [
            (620 - 45, 621 - 135), (735 - 45,621 - 135), (620 - 45,556 - 135), (735 - 45,556 - 135), (600 - 45,700 - 135), (710 - 45,700 - 135), # 12 camera buttons
            (769 - 45,482 - 135), (612 - 45,471 - 135), (920 - 45,441 - 135), (830 - 45,570 - 135), (954 - 45,515 - 135), (945 - 45,608 - 135)
        ]

        # Camera buttons
        button_dims = [App.assets.room_button_unselected.get_width(), App.assets.room_button_unselected.get_height()]
        self.camera_buttons = []
        for i in range(len(self.camera_buttons_positions)):
            self.camera_buttons.append(Button((self.camera_buttons_positions[i][0] + button_dims[0]/2, self.camera_buttons_positions[i][1] + button_dims[1]/2), button_dims, App.assets.room_button_unselected))

        self.flash_light_hitbox = pygame.Rect(50, 50, 450, 600)

        # Timers, for each wide rooms (A camera movement is needed)
        self.timers_checkpoints = [
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0
        ]

        self.timers_wait_time_ms = []
        for i in range(12):
            self.timers_wait_time_ms.append(
                random.randint(5000, 7000)
            )

        self.cameras_x_position = [
            0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0
        ]

        # 0 its right 1 its left
        self.wide_cameras_mov_direction = [
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0
        ]

        self.occupied_camera = [
            False, False, False, False, False, False,
            False, False, False, False, False, False
        ]

        self.camera_speed = 5

        self.static_animation = False

        self.camera_flashlighting = False

        self.label_to_draw = None

        self.record_spr_timer = pygame.time.get_ticks()

    def update(self, App):
        self.camera_room_managment(App)

        App.animations.static_anim_1.update(App.surface)

        App.surface.blit(App.assets.camera_borderline, (0, 0))

        self.camera_ui(App)

        if self.static_animation:
            App.animations.static_anim_2.update(App.surface)
            if App.animations.static_anim_2.sprite_num == len(App.animations.static_anim_2.sprites) - 1:
                App.animations.static_anim_2.sprite_num = 0
                self.static_animation = False
                App.assets.camera_sound_1.play()

        #pygame.draw.rect(App.surface, (255,0,0), self.flash_light_hitbox)

    def cam_map(self, App):
        App.surface.blit(App.assets.camera_map, (550, 310))
        self.draw_cam_map_buttons(App)

    def draw_cam_map_buttons(self, App):
        button_dims = [App.assets.room_button_unselected.get_width(), App.assets.room_button_unselected.get_height()]
        for i in range(len(self.camera_buttons)):
            self.camera_buttons[i].update(App.surface, App.mouse_hitbox)

            if i+1 == self.inCameraRoom:
                self.camera_buttons[i].sprite = App.assets.room_button_selected
            else:
                self.camera_buttons[i].sprite = App.assets.room_button_unselected

            if self.camera_buttons[i].mouse_hovered and pygame.mouse.get_pressed()[0]:
                if not i+1 == self.inCameraRoom:
                    self.static_animation = True

                self.inCameraRoom = i+1

            App.surface.blit(App.assets.room_buttons_labels[i], (
                self.camera_buttons_positions[i][0] + button_dims[0]/2 + 5 , self.camera_buttons_positions[i][1] + button_dims[1]/2 + 7
            ))

    def camera_timer(self, App, index):
        # Timer
        if self.timers_checkpoints[index]:
            if pygame.time.get_ticks() - self.timers_checkpoints[index] > self.timers_wait_time_ms[index]:
                self.timers_checkpoints[index] = None

        elif not self.timers_checkpoints[index]:
            if self.wide_cameras_mov_direction[index] == 0:
                self.cameras_x_position[index] -= self.camera_speed

                # END CONDITION
                if self.cameras_x_position[index] < -abs(App.assets.main_hall_cameras[0].get_width() - App.dimentions[0]):
                    self.cameras_x_position[index] = -abs(App.assets.main_hall_cameras[0].get_width() - App.dimentions[0])
                    self.timers_checkpoints[index] = pygame.time.get_ticks()
                    if self.wide_cameras_mov_direction[index] == 0: self.wide_cameras_mov_direction[index] = 1
                    else: self.wide_cameras_mov_direction[index] = 0

            else:
                self.cameras_x_position[index] += self.camera_speed

                # END CONDITION
                if self.cameras_x_position[index] > 0:
                    self.cameras_x_position[index] = 0
                    self.timers_checkpoints[index] = pygame.time.get_ticks()
                    if self.wide_cameras_mov_direction[index] == 0: self.wide_cameras_mov_direction[0] = 1
                    else: self.wide_cameras_mov_direction[index] = 0

    def camera_ui(self, App):
        self.cam_map(App)
        labels_position = (550, 280)
        App.surface.blit(self.label_to_draw, labels_position)
        if self.inCameraRoom == 11:
            App.objects.music_box.update(App)

        self.record_sprite(App)

    def record_sprite(self, App):
        time = 1000
        if pygame.time.get_ticks() - self.record_spr_timer > 0 and pygame.time.get_ticks() - self.record_spr_timer < time:
            App.surface.blit(App.assets.camera_record_sprite, (62, 96))
        elif pygame.time.get_ticks() - self.record_spr_timer > time*2:
            self.record_spr_timer = pygame.time.get_ticks()
        

    def camera_room_managment(self, App):
        match self.inCameraRoom:
            case 1:
                self.camera_basics(App, App.assets.party_room_1_cameras,0, lambda:self.party_room_1(App))
                self.label_to_draw = App.assets.party_room_1_label
            case 2:
                self.camera_basics(App, App.assets.party_room_2_cameras,1, lambda:self.party_room_2(App))
                self.label_to_draw = App.assets.party_room_2_label
            case 3:
                self.camera_basics(App, App.assets.party_room_3_cameras,2, lambda:self.party_room_3(App))
                self.label_to_draw = App.assets.party_room_3_label
            case 4:
                self.camera_basics(App, App.assets.party_room_4_cameras,3, lambda:self.party_room_4(App))
                self.label_to_draw = App.assets.party_room_4_label
            case 5: 
                self.camera_basics(App, App.assets.left_air_vent_cameras,4, lambda:self.left_air_vent(App))
                self.label_to_draw = App.assets.left_air_vent_label
            case 6:
                self.camera_basics(App, App.assets.right_air_vent_cameras,5, lambda:self.right_air_vent(App))
                self.label_to_draw = App.assets.right_air_vent_label
            case 7:
                self.camera_basics(App, App.assets.main_hall_cameras,6, lambda:self.main_hall(App))
                self.label_to_draw = App.assets.main_hall_label
            case 8:
                self.camera_basics(App, App.assets.partsnservice_cameras,7, lambda:self.parts_n_service(App))
                self.label_to_draw = App.assets.parts_n_service_label
            case 9:
                self.camera_basics(App, App.assets.show_stage_cameras,8, lambda:self.show_stage(App))
                self.label_to_draw = App.assets.show_stage_label
            case 10:
                self.camera_basics(App, App.assets.game_area_cameras,9, lambda:self.game_area(App))
                self.label_to_draw = App.assets.game_area_label
            case 11:
                self.camera_basics(App, App.assets.prize_corner_cameras,10, lambda:self.prize_corner(App))
                self.label_to_draw = App.assets.prize_corner_label
            case 12:
                self.camera_basics(App, App.assets.kids_cove_cameras,11, lambda:self.kids_cove(App))
                self.label_to_draw = App.assets.kids_cove_label

        if App.objects.music_box.charge != 0:
            self.room_music()

    def room_music(self):
        # Puppet music
        if self.inCameraRoom == 11:
            pygame.mixer.Channel(2).set_volume(0.5)
        elif self.inCameraRoom == 12 or self.inCameraRoom == 10 or self.inCameraRoom == 9:
            pygame.mixer.Channel(2).set_volume(0.2)
        else:
            pygame.mixer.Channel(2).set_volume(0)

    def timers_update(self, App):
        """ Keep updating the camera timers even if the player its not with the cameras """
        # Only the last 6 cameras are the ones that can move
        for i in range(6):
            self.camera_timer(App, i + 6)

    def camera_basics(self, App, cameras_list:list, index:int, room_module):
        mouse_click = pygame.mouse.get_pressed()
        if index == 10:
            self.flash_light_hitbox[3] = 370
        else:
            self.flash_light_hitbox[3] = 600
        
        flashlight_collide = App.mouse_hitbox.colliderect(self.flash_light_hitbox)

        # --- Camera intelligence module ---
        try:
            m = room_module()
            surface_id_off, surface_id_on = m
        except TypeError as e:
            print(f"- Error in room {index + 1} - Error code: {e} - {m}")
            App.objects.Animatronics.console_animatrionic_position_log()

        

        if not self.occupied_camera[index]:
            App.animations.static_anim_1.alpha = 100

            surface_id = surface_id_off

            if flashlight_collide:
                if mouse_click[0]:
                    if surface_id_on:
                        surface_id = surface_id_on
                        if not self.camera_flashlighting:
                            App.assets.buzzlight.play()
                        self.camera_flashlighting = True

            App.surface.blit(cameras_list[surface_id], (self.cameras_x_position[index], 0))
        else:
            App.animations.static_anim_1.alpha = 255

        # Flashlighting detection
        if not flashlight_collide or not mouse_click[0] or self.occupied_camera[index]:
            surface_id = surface_id_off
            self.camera_flashlighting = False

        if not self.camera_flashlighting:
            App.assets.buzzlight.stop()

    # Normal
    def party_room_1(self, App):
        """ 1 """
        toy_chica_location = App.objects.Animatronics.animatronics_in_game["TOY_CHICA"]
        if toy_chica_location.locationId == 1:
            return 0, 3
        elif toy_chica_location.locationId != 1:
            return 0, 1
    # Normal
    def party_room_2(self, App):
        """ 2 """
        toy_bunny_location = App.objects.Animatronics.animatronics_in_game["TOY_BUNNY"]
        withered_chica_location = App.objects.Animatronics.animatronics_in_game["WITHERED_CHICA"]
        
        if toy_bunny_location.locationId == 2 and withered_chica_location.locationId != 2:
            return 0, 2
        if toy_bunny_location.locationId != 2 and withered_chica_location.locationId == 2:
            return 3, 4
        elif toy_bunny_location.locationId != 2 and withered_chica_location.locationId != 2:
            return 0, 1
    # Normal
    def party_room_3(self, App):
        """ 3 """
        withered_freddy_location = App.objects.Animatronics.animatronics_in_game["WITHERED_FREDDY"]
        toy_bunny_location = App.objects.Animatronics.animatronics_in_game["TOY_BUNNY"]
        if toy_bunny_location.locationId == 3 and withered_freddy_location.locationId != 3:
            return 0, 2
        elif toy_bunny_location.locationId != 3 and withered_freddy_location.locationId == 3:
            return 3, 4
        elif toy_bunny_location.locationId != 3:
            return 0, 1

    # Normal
    def party_room_4(self, App):
        """ 4 """
        toy_bunny_location = App.objects.Animatronics.animatronics_in_game["TOY_BUNNY"]
        toy_chica_location = App.objects.Animatronics.animatronics_in_game["TOY_CHICA"]
        withered_chica_location = App.objects.Animatronics.animatronics_in_game["WITHERED_CHICA"]

        if toy_bunny_location.locationId == 4 and toy_chica_location.locationId != 4 and withered_chica_location.locationId != 4:
            return 2, 3
        elif toy_bunny_location.locationId != 4 and toy_chica_location.locationId == 4 and withered_chica_location != 4:
            return 0, 4
        elif toy_chica_location.locationId != 4 and toy_bunny_location.locationId != 4 and withered_chica_location == 4:
            return 0, 5
        elif toy_chica_location.locationId != 4 and toy_bunny_location.locationId != 4:
            return 0, 1

    # Normal
    def left_air_vent(self, App):
        """ 5 """
        toy_chica_location = App.objects.Animatronics.animatronics_in_game["TOY_CHICA"]
        if toy_chica_location.locationId == 5:
            return 0, 4
        elif toy_chica_location.locationId != 5:
            return 0, 1

    # Normal
    def right_air_vent(self, App):
        """ 6 """
        toy_bunny_location = App.objects.Animatronics.animatronics_in_game["TOY_BUNNY"]
        withered_chica_location = App.objects.Animatronics.animatronics_in_game["WITHERED_CHICA"]

        if toy_bunny_location.locationId == 6 and withered_chica_location.locationId != 6:
            return 0, 2
        elif toy_bunny_location.locationId != 6 and withered_chica_location.locationId == 6:
            return 0, 3
        elif toy_bunny_location.locationId != 6 and withered_chica_location.locationId != 6:
            return 0, 1
    # Wider
    def main_hall(self, App):
        """ 7 """
        toy_chica_location = App.objects.Animatronics.animatronics_in_game["TOY_CHICA"]
        withered_freddy_location = App.objects.Animatronics.animatronics_in_game["WITHERED_FREDDY"]
        withered_bonnie_location = App.objects.Animatronics.animatronics_in_game["WITHERED_BONNIE"]

        if toy_chica_location.locationId == 7 and withered_freddy_location.locationId != 7 and withered_bonnie_location.locationId != 7:
            return 4, 5
        elif toy_chica_location.locationId != 7 and withered_freddy_location.locationId == 7 and withered_bonnie_location.locationId != 7:
            return 0, 3
        elif toy_chica_location.locationId != 7 and withered_freddy_location.locationId != 7 and withered_bonnie_location.locationId == 7:
            return 0, 2
        elif toy_chica_location.locationId != 7 and withered_freddy_location.locationId != 7 and withered_bonnie_location.locationId != 7: 
            return 0, 1
    # Wider
    def parts_n_service(self, App):
        """ 8 - First goes withered bonnie, then chica and finally freddy"""
        withered_freddy_location = App.objects.Animatronics.animatronics_in_game["WITHERED_FREDDY"]
        withered_bonnie_location = App.objects.Animatronics.animatronics_in_game["WITHERED_BONNIE"]
        withered_chica_location = App.objects.Animatronics.animatronics_in_game["WITHERED_CHICA"]

        if withered_freddy_location.locationId == 8 and withered_bonnie_location.locationId == 8 and withered_chica_location.locationId == 8:
            return 0, 1
        if withered_freddy_location.locationId == 8 and withered_bonnie_location.locationId != 8 and withered_chica_location.locationId == 8:
            return 0, 2
        elif withered_freddy_location.locationId == 8 and withered_bonnie_location.locationId != 8 and withered_chica_location.locationId != 8:
            return 0, 3
        elif withered_freddy_location.locationId != 8 and withered_bonnie_location.locationId != 8 and withered_chica_location.locationId != 8:
            return 0, 5
    # Wider
    def show_stage(self, App):
        """ 9 """

        toy_freddy_location = App.objects.Animatronics.animatronics_in_game["TOY_FREDDY"]
        toy_bunny_location = App.objects.Animatronics.animatronics_in_game["TOY_BUNNY"]
        toy_chica_location = App.objects.Animatronics.animatronics_in_game["TOY_CHICA"]

        if toy_bunny_location.locationId == 9 and toy_freddy_location.locationId == 9 and toy_chica_location.locationId == 9:
            return 0, 1

        elif toy_bunny_location.locationId != 9 and toy_freddy_location.locationId == 9 and toy_chica_location.locationId == 9:
            return 2, 3

        elif toy_bunny_location.locationId != 9 and toy_freddy_location.locationId == 9 and toy_chica_location.locationId != 9:
            return 4, 5

        elif toy_bunny_location.locationId != 9 and toy_freddy_location.locationId != 9 and toy_chica_location.locationId != 9:
            return 6, None

    # Wider
    def game_area(self, App):
        """ 10 """

        toy_freddy_location = App.objects.Animatronics.animatronics_in_game["TOY_FREDDY"]
        
        if toy_freddy_location.locationId == 10:
            return 0, 4
        else:
            return 0, 1
    # Wider
    def prize_corner(self, App):
        """ 11 """
        puppet = App.objects.Animatronics.animatronics_in_game["PUPPET"]
        if puppet.secondPositionId == 2:
            return 0, 2
        elif puppet.secondPositionId == 3:
            return 0, 3
        else:
            return 0, 1
    # Wider
    def kids_cove(self, App):
        """ 12 """
        return 0, 1