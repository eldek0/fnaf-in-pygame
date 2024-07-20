import pygame

class GameTimer:
    def __init__(self, App, real_time_mode=False):
        self.real_time_mode = real_time_mode
        self.position = [App.dimentions[0] - 105, 25]
        self.times = [
            12, 0, 0
        ]
        if self.real_time_mode:
            hours_xpos = self.position[0] - 65*2
        else:
            hours_xpos = self.position[0]

        self.time_position = [
            (hours_xpos, self.position[1]), # Hours
            (self.position[0] - 65, self.position[1]), # Minutes
            (self.position[0], self.position[1]) # Seconds
        ]
        self.ticks = pygame.time.get_ticks()
        self.night = App.menu.nightToPlay

        self.GAMEHOUR = 70_000
        self.REALLIFEHOUR = 60_000*60

        if self.real_time_mode:
            self.hour = self.REALLIFEHOUR # 1 hour in real life (60 seconds * 60)
            print("Game running in real time !")
            self.seconds_timer = pygame.time.get_ticks()
        else:
            self.hour = self.GAMEHOUR# 70 seconds

    def update(self, App, update_time=True):
        if not self.real_time_mode:
            self.draw_night_label(App)
        self.draw_time(App)
        if update_time:
            self.update_time()
        if self.real_time_mode:
            pos = list(self.time_position[1])
            pos[0] += 25
            pos[1] += 39
            App.uiSurface.blit(App.assets.dots, pos)

            pos[0] -= 65
            App.uiSurface.blit(App.assets.dots, pos)

        if App.debug: self.debugTime()
            

    def debugTime(self):
        """Debug only"""
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_0]): self.ticks -= self.hour

    def update_time(self):
        if pygame.time.get_ticks() - self.ticks > self.hour:
            self.times[1] = 0
            self.times[2] = 0
            if self.times[0] == 12:
                self.times[0] = 1
            else:
                self.times[0] += 1

            self.ticks = pygame.time.get_ticks()

        if self.real_time_mode:
            if ((pygame.time.get_ticks() - self.seconds_timer) > self.hour/(60*60)):
                self.times[2] += 1
                self.seconds_timer = pygame.time.get_ticks()

            if self.times[2] >= 60:
                self.times[1] += 1
                self.times[2] = 0

    def draw_night_label(self, App):
        App.uiSurface.blit(App.assets.night_label, (self.position[0] - 66 + 20, self.position[1] + 5))
        App.uiSurface.blit(App.assets.numbers[self.night], (self.position[0] + 35 + 20, self.position[1] - 3 + 2))

    def draw_time(self, App):
        if self.real_time_mode:
            lenght = len(self.times)
        else:
            lenght = 1
        for i in range(lenght):
            time = self.times[i]
            x_extra = 0
            reversed_time = str(time)[::-1]

            if (i == 1 or i == 2) and len(reversed_time) == 1:
                reversed_time = f"{time}0"

            for number in reversed_time:
                try:
                    App.uiSurface.blit(App.assets.numbers[int(number)], (self.time_position[i][0] - x_extra, self.time_position[i][1] + 40))
                    x_extra += App.assets.numbers[int(number)].get_width()
                except ValueError as e:
                    print(f"Error en draw_time: {e}")

        App.uiSurface.blit(App.assets.am_label, (self.position[0] + 33, self.position[1] + 44))