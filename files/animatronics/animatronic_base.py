import pygame, random
from abc import ABC

class Animatronic(ABC):
    def __init__(self, aggresivity:int, locationId:int, jumpscare_animation:list, rest_room:int, custom_index:int):
        """
        locationId:
            - From 1 to 12 are room locations
            - Greater that 100 are office locations
            101: Office hallway
            102: Right vent
            103: Left vent
            104: In Office Desk
            0: Rest after attacking

        """


        self.locationId = locationId
        self.secondPositionId = 1
        self.timer = pygame.time.get_ticks()
        self.changing_position:bool = False
        self.action_error:bool = False # When the animatronic is moving
        self._previous_movement = [] # The changing and the location
        self._jumpscare:bool = False
        self.jumpscare_animation = jumpscare_animation
        self._gameOver = False
        self.occupied_camera_time = 5000
        self.inOfficeDesk:bool = False # If the animatronic is in office to attack
        self.name_id:str = "-"
        self._prepare_to_jumpscare = False # Get a random timer and jumpscare the player
        self.jumpscare_wait_time = 3000
        self.time_with_mask_goal = 120
        self.time_with_mask = 0
        self.rest_room = rest_room # The room where the animatrionic rests after a screamer attempt
        self.aggresivity = aggresivity
        self.movement_time = 50_000
        self.custom_index = custom_index # For custom night
        self.noise_timer = pygame.time.get_ticks()
        self.time_to_make_noise = 10000

        # Aveliable animatrionics with the same room position
        self.aveliable_rooms_positions = {
            101: [["FOXY", "WITHERED_BONNIE"], ["FOXY", "MANGLE"], ["TOY_FREDDY"]],
            10 : [["BALOON_BOY", "TOY_FREDDY"]]
            }

    def jumpscare_update(self, App):
        if self.aggresivity != 0:
            if self._jumpscare:
                self.jumpscare_animation.update(App.surface)
                App.objects.open_monitor_button.quitting_camera = True
                App.objects.mask_button.quitting_mask = True
                if self.jumpscare_animation.sprite_num == len(self.jumpscare_animation.sprites) - 1:
                    self._gameOver = True

    def update(self, App):
        if self.aggresivity != 0:      
            if not self._jumpscare:
                if self._prepare_to_jumpscare:
                    self.jumpscare_time(App)
                else:
                    self.movement(App)

            # Static to camera
            if self.changing_position:
                self._change_occupied_camera_or_office(App, True)
            elif not self.changing_position and self.action_error:
                self._change_occupied_camera_or_office(App, False)
                self.action_error = False
            
            self.animatrionic_movement_sounds(App)

            # If in room 0
            if self.locationId == 0 and self.rest_room != None:
                self.change_location_id(App, self.rest_room)

    def animatrionic_movement_sounds(self, App):
        if pygame.time.get_ticks() - self.noise_timer > self.time_to_make_noise:
            if not(self.name_id == "BALOON_BOY" and self.name_id == "MANGLE"):
                if self.locationId == 5 or self.locationId == 6:
                    App.assets.vents_sounds.play()

                elif self.changing_position:
                    ran = random.randint(0, len(App.assets.walk_sounds) - 1)
                    App.assets.walk_sounds[ran].play()
            elif self.name_id == "BALOON_BOY":
                if not self.locationId == -1:
                    if self.changing_position:
                        ran = random.randint(0, 3)
                        if ran == 3:
                            App.assets.baloon_laugh.play()
                        else:
                            App.assets.baloon_noises[ran].play()

            elif self.name_id == "MANGLE":
                if not self.locationId == -1 and not self.locationId == 6:
                    if self.changing_position:
                        App.assets.metal_run_sound.play()


            self.noise_timer = pygame.time.get_ticks()

    def jumpscare_time(self, App):
        if pygame.time.get_ticks() - self.timer > self.jumpscare_wait_time and App.objects.open_monitor_button.inCamera:
            self.jumpscare(App)

    def _change_occupied_camera_or_office(self, App, state:bool):
        """ Change occupied camera and office """
        # If previous_movement is below 100 its a camera
        if self._previous_movement[0] -1 < 100:
            App.objects.camera.occupied_camera[self._previous_movement[0] - 1] = state # Camera
        else:
            App.objects.office.occupied_office[self._previous_movement[0] - 101] = state # Office

        if self._previous_movement[1] -1 < 100:
            App.objects.camera.occupied_camera[self._previous_movement[1] - 1] = state # Camera
        else:
            App.objects.office.occupied_office[self._previous_movement[1] - 101] = state # Office

    def movement(self, App):
        pass

    def verify_free_room(self, App, room_location:int):
        animatrionics_in_room = App.objects.Animatronics.every_animatrionic_position[room_location]
        if animatrionics_in_room == []: return True

        if not room_location in list(self.aveliable_rooms_positions.keys()):
            for animatrionic in animatrionics_in_room:
                if animatrionic.name_id != self.name_id:
                    return False

            return True
        else:
            found_match = False
            for animatrionic in animatrionics_in_room:
                for aveliable_pos in self.aveliable_rooms_positions[room_location]:
                    found_match = False
                    for name in aveliable_pos:
                        print(name)
                        if animatrionic.name_id == name:
                            found_match = True
                        else:
                            break

                    if found_match: break
                if found_match: break

            if found_match and self.name_id in aveliable_pos:
                return True
            return False

    def change_location_id(self ,App, room_location:int, secondPositionId=1, forced=False):
        changing_to_location = room_location
        changing_to_position = secondPositionId
        self._previous_movement = [changing_to_location, self.locationId, changing_to_position, self.secondPositionId]

        if (changing_to_location == 104 or changing_to_location == -1 or changing_to_location == 0):
            self.changing_position = True
            self._wait_movement_time(force=True)
        else:
            self._wait_movement_time()
        is_free_room = self.verify_free_room(App, room_location)
        
        """print(f"free-room ({self.name_id}): {is_free_room}, force: {forced}")
        print("its me! it works!")
        print(App.objects.Animatronics.every_animatrionic_position[room_location])
        print(self.aveliable_rooms_positions)"""
        
        # If it's empty or its forced
        if forced or is_free_room:
            if not self.changing_position:
                self.locationId = changing_to_location
                self.secondPositionId = changing_to_position
                changing_to_location = -1
                self.time_with_mask = 0
        else:
            # We need more time !
            self.timer = pygame.time.get_ticks()
            self.changing_position = False

    def _wait_movement_time(self, force=False):
        """ Will provoke the static while moving """
        if not self.changing_position:
            self.timer = pygame.time.get_ticks()
            self.changing_position = True
            self.action_error = True

        elif self.changing_position:
            if not force:
                time_to_change = self.occupied_camera_time/self.aggresivity
            else:
                time_to_change = 0

            if pygame.time.get_ticks() - self.timer > time_to_change:
                self.changing_position = False
                self.timer = pygame.time.get_ticks()

    def isGameOver(self):
        return self._gameOver

    def get_prev_movement(self):
        if self.action_error and self.changing_position == False:
            self.prev_copy = self._previous_movement
            self._previous_movement = [-1, -1]
            self.action_error = False
            return self.prev_copy
        return [-1 , -1]

    def jumpscare(self, App):
        if not self._jumpscare:
            pygame.mixer.Channel(8).play(App.assets.xScream1)
            self._jumpscare = True

    def prepare_to_jumpscare(self, App):
        self.change_location_id(App, -1, forced=True)
        self.timer = pygame.time.get_ticks()
        self._prepare_to_jumpscare = True

    def isBeingJumpscared(self): return self._jumpscare