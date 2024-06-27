import pygame

class Cutscene:
    def __init__(self, App):
        self.music_started = False
        self.state:int = -2
        self.timer = pygame.time.get_ticks()
        self.deco_timer = pygame.time.get_ticks()
        self.move_extremes = ( -abs(App.assets.cutscene_background.get_width() - App.dimentions[0]) + 350, -150 )
        self.x_pos = self.move_extremes[0]/2
        self.move_rect_left = pygame.Rect(0, 0, App.dimentions[0]/3, App.dimentions[1])
        self.move_rect_right = pygame.Rect(App.dimentions[0] - App.dimentions[0]/3, 0, App.dimentions[0]/3, App.dimentions[1])
        self.speed = 4
        self.sprites_index = 0
        App.animations.static_anim_1.alpha = 0
        self.finished = False
        self.showFreddy = False
        self.freddy_pos = []
        self.puppet_pos = []
        self.delta_pos = 0

    def update(self, App, inNight:int):
        self.inNight = inNight
        # Background
        App.surface.blit(App.assets.cutscene_background, (self.x_pos, 0))

        match self.state:
            case -2:
                App.surface.fill((0, 0, 0))
                self.state += 1
                self.timer = pygame.time.get_ticks()
                self.deco_timer = pygame.time.get_ticks()

            case -1:
                App.surface.fill((0, 0, 0))
                if pygame.time.get_ticks() - self.timer > 2666:
                    self.state += 1
                    self.timer = pygame.time.get_ticks()
            case 0:
                if not self.music_started:
                    print("cutscene")
                    App.assets.cutscene_ambient.play()
                    App.assets.ambiance_2.play()
                    self.music_started = True
                App.surface.blit(App.assets.cutscene_black, (0, 0))

                if pygame.time.get_ticks() - self.timer > 3200:
                    self.state += 1
                    self.timer = pygame.time.get_ticks()

            case 1:
                
                # Draw bonnie and chica
                self.draw_characters(App)

                mask_anim = App.animations.cutscene_mask_animation
                mask_anim.update()

                App.surface.blit(App.assets.cutscene_mask, (mask_anim.position[0], mask_anim.position[0]))

                self.movement(App)

                self.static(App)

                if pygame.time.get_ticks() - self.timer > 32000 and pygame.time.get_ticks() - self.timer < 35000:
                    # Starts sounding the error sound
                    if not pygame.mixer.Channel(5).get_busy():
                        pygame.mixer.Channel(5).play(App.assets.robot_err)

                    if pygame.time.get_ticks() - self.timer > 34000:
                        pygame.mixer.Channel(5).stop()

                if pygame.time.get_ticks() - self.timer > 35000:
                    # The screen glitches even more
                    App.animations.static_anim_2_looped.update(App.uiSurface)
                    if not pygame.mixer.Channel(5).get_busy():
                        pygame.mixer.Channel(5).play(App.assets.static_end)
                    
                    
                if pygame.time.get_ticks() - self.timer > 36000:
                    pygame.mixer.Channel(5).stop()
                    pygame.mixer.Channel(0).stop()
                    App.assets.cutscene_ambient.stop()
                    App.assets.ambiance_2.stop()
                    self.state = 2
                    self.timer = pygame.time.get_ticks()

            case 2:
                App.surface.fill((0, 0, 0))
                if pygame.time.get_ticks() - self.timer < 1500:
                    if self.inNight == 1:
                        img = App.assets.err_img
                    else:
                        img = App.assets.its_me
                    App.uiSurface.blit(img, (20, 20))

                if pygame.time.get_ticks() - self.timer > 3000:
                    self.finished = True


    def draw_characters(self, App):
        if self.inNight == 2 or self.inNight == 3:
            self.sprites_index = self.inNight - 1
        else:
            self.sprites_index = 0

        App.surface.blit(App.assets.cutscene_chica[self.sprites_index], (self.x_pos, 0))
        App.surface.blit(App.assets.cutscene_bonnie[self.sprites_index], ((App.assets.cutscene_background.get_width() - App.dimentions[0]) + self.x_pos, 0))
        
        if self.inNight == 3:
            if not self.showFreddy:
                if self.x_pos < self.move_extremes[0] + 40:
                    self.freddy_pos = [App.assets.cutscene_background.get_width()/4 - 110, 0]
                    self.showFreddy = True
                elif self.x_pos > self.move_extremes[1] - 40:
                    self.freddy_pos = [App.assets.cutscene_background.get_width()/4 + 460, 0]
                    self.showFreddy = True


            if self.showFreddy:
                App.surface.blit(App.assets.cutscene_freddy, (self.freddy_pos[0] + self.x_pos, self.freddy_pos[1]))

        if self.inNight == 4:
            if self.delta_pos > 0: self.delta_pos -= self.speed/3 * App.deltaTime
            elif self.delta_pos < 0: self.delta_pos += self.speed/3 * App.deltaTime

            dims = App.assets.cutscene_puppet.get_rect()
            self.puppet_pos = [App.dimentions[0]/2 - dims.w/2, 0]
            App.surface.blit(App.assets.cutscene_puppet, (self.puppet_pos[0] + self.delta_pos, 0))

    def movement(self, App):
        collide_left = App.mouse_hitbox.colliderect(self.move_rect_left)
        collide_right = App.mouse_hitbox.colliderect(self.move_rect_right)

        if collide_right:
            self.x_pos -= self.speed * App.deltaTime
            

            if self.x_pos < self.move_extremes[0] :
                self.x_pos = self.move_extremes[0]
                

        elif collide_left:
            self.x_pos += self.speed * App.deltaTime
            

            if self.x_pos > self.move_extremes[1]:
                self.x_pos = self.move_extremes[1]


        if self.x_pos > self.move_extremes[1]- 10 or self.x_pos < self.move_extremes[0] + 10:
            collide_right = False
            collide_left = False

        # For puppet
        if collide_right: self.delta_pos -= self.speed/1.7 * App.deltaTime
        elif collide_left: self.delta_pos += self.speed/1.7 * App.deltaTime

        # Move sound
        if collide_left or collide_right:
            if not pygame.mixer.Channel(0).get_busy():
                pygame.mixer.Channel(0).play(App.assets.move_sound)

        else:
            pygame.mixer.Channel(0).stop()

    def static(self, App):
        if pygame.time.get_ticks() - self.deco_timer > 1000:
            App.animations.static_anim_1.alpha = 160
            if pygame.time.get_ticks() - self.deco_timer > 1400:
                App.animations.static_anim_1.alpha = 0
                if pygame.time.get_ticks() - self.deco_timer > 1800:
                    App.animations.static_anim_1.alpha = 160
                    if pygame.time.get_ticks() - self.deco_timer > 2000:
                        App.animations.static_anim_1.alpha = 0
                        self.deco_timer = pygame.time.get_ticks()

        App.animations.static_anim_1.update(App.surface)