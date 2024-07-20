import pygame
import pyperclip
from files.Text import Text

def import_names() ->list:
    with open("files/cre.txt", "r") as pk:
        names = pk.readlines()
    return names

class Credits:
    def __init__(self):
        self.mouse_pressed = False
        self.scroll_down:int = -330

    def update(self, App):
        surf:pygame.surface.Surface = App.surface
        uisurf:pygame.surface.Surface = App.uiSurface
        margin_x = 0
        margin_y = 50 - self.scroll_down
        margin_yt = margin_y + 190
        margin_yt_between_texts = 30

        sc_text = Text(App, "Created originally by Scott Cawthon", (margin_x, margin_y) , App.assets.ocr_font20, (255, 255, 255), lock="x")
        ek_text = Text(App, "Recreation made by Eldek", (margin_x, margin_y + 60) , App.assets.ocr_font20, (255, 255, 255), lock="x")
        sc_text.draw(surf)
        ek_text.draw(surf)

        pg_text = Text(App, "Made using python 1.12.0 and pygame 2.4.0", (margin_x, margin_y + 90) , App.assets.ocr_font20, (255, 255, 255), lock="x")
        pg_text.draw(surf)

        thanks_subs = Text(App, "Thanks to all and every sub from okxd,", (margin_x, margin_y + 140) , App.assets.ocr_font30, (255, 255, 255), lock="x")
        thanks_subs2 = Text(App, "You really mean a lot to me!", (margin_x, margin_y + 160) , App.assets.ocr_font30, (255, 255, 255), lock="x")
        thanks_subs.draw(uisurf)
        thanks_subs2.draw(uisurf)

        names = import_names()
        for i in range(len(names)):
            text = names[i]

            t = Text(App, str(text), (margin_x, margin_yt + margin_yt_between_texts*(i)), App.assets.ocr_font20, (255, 255, 255), lock="x")

            t.draw(surf)

            if i == len(names) - 1:
                if t.y < -10:
                    App.menu.menu_exit(App, force=True)

        App.menu.menu_exit(App)

        self.scroll_down += 0.2

        App.assets.esc_to_return.set_alpha(150)
        uisurf.blit(App.assets.esc_to_return, (surf.get_width() - 130, surf.get_height() - 15))