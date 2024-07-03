import pygame

class GameTimer:
    def __init__(self, App):
        self.time = 12
        self.position = [App.dimentions[0] - 105, 25]
        self.ticks = pygame.time.get_ticks()
        self.night = App.menu.nightToPlay
        self.hour = 70_000# 70 seconds

    def update(self, App, update_time=True):
        self.draw_night_label(App)
        self.draw_time(App)
        if update_time:
            self.update_time()
        if App.debug: self.debugTime()

    def debugTime(self):
        """Debug only"""
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_0]): self.ticks -= self.hour

    def update_time(self):
        if pygame.time.get_ticks() - self.ticks > self.hour:
            if self.time == 12:
                self.time = 1
            else:
                self.time += 1

            self.ticks = pygame.time.get_ticks()

    def draw_night_label(self, App):
        App.uiSurface.blit(App.assets.night_label, (self.position[0] - 66 + 20, self.position[1] + 5))
        App.uiSurface.blit(App.assets.numbers[self.night], (self.position[0] + 35 + 20, self.position[1] - 3 + 2))

    def draw_time(self, App):
        x_extra = 0
        reversed_time = str(self.time)[::-1]
        for number in reversed_time:
            try:
                App.uiSurface.blit(App.assets.numbers[int(number)], (self.position[0] - x_extra, self.position[1] + 40))
                x_extra += App.assets.numbers[int(number)].get_width()
            except ValueError as e:
                print(f"Error en draw_time: {e}")

        App.uiSurface.blit(App.assets.am_label, (self.position[0] + 33, self.position[1] + 44))