import pygame

class GameTimer:
    def __init__(self, App):
        self.time = 12
        self.position = [App.dimentions[0] - 105, 25]
        self.ticks = pygame.time.get_ticks()
        self.night = App.menu.inNight
        self.hour = 70000 # 70 seconds

    def update(self, App, update_time=True):
        self.draw_night_label(App)
        self.draw_time(App)
        if update_time:
            self.update_time()

    def update_time(self):
        if pygame.time.get_ticks() - self.ticks > self.hour:
            if self.time == 12:
                self.time = 1
            else:
                self.time += 1

            self.ticks = pygame.time.get_ticks()

    def draw_night_label(self, App):
        App.surface.blit(App.assets.night_label, (self.position[0] - 66 + 20, self.position[1] + 5))
        App.surface.blit(App.assets.numbers[self.night], (self.position[0] + 35 + 20, self.position[1] - 3 + 5))

    def draw_time(self, App):
        x_extra = 0
        reversed_time = str(self.time)[::-1]
        for number in reversed_time:
            App.surface.blit(App.assets.numbers[int(number)], (self.position[0] - x_extra, self.position[1] + 40))
            x_extra += App.assets.numbers[int(number)].get_width() + 7

        App.surface.blit(App.assets.am_label, (self.position[0] + 33, self.position[1] + 44))