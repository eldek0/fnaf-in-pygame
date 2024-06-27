import pygame, random

class StaticStripesAnimation:
    def __init__(self, App, time_to_appear:int=2000, speed_frame:int=1, random_sprites_range:tuple=(0, 4), alpha=30):
        self.time_to_appear = time_to_appear
        self.timer = pygame.time.get_ticks()
        self.speed_frame = speed_frame
        self.random_sprites_range = random_sprites_range
        self.alpha = alpha

        self.update_dims(App)

    def update_dims(self, App):
        self.index = random.randint(self.random_sprites_range[0], self.random_sprites_range[1])
        self.chosen_stripe = App.assets.static_stripes[self.index]
        self.big_stripe_dims = self.chosen_stripe.get_rect()
        self.big_stripe_y_location = -self.big_stripe_dims.height

    def update(self, App, surface:pygame.Surface):
        self.chosen_stripe.set_alpha(self.alpha)
        surface.blit(self.chosen_stripe, (0, self.big_stripe_y_location))
        self.big_stripe_y_location += self.speed_frame * App.deltaTime
        if self.big_stripe_y_location > App.dimentions[1]:
            self.big_stripe_y_location = -self.big_stripe_dims.height
            if pygame.time.get_ticks() - self.timer > self.time_to_appear:
                self.update_dims(App)
        else:
            self.timer = pygame.time.get_ticks()