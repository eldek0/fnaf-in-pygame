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
        self.scroll_down:int = 0

    def update(self, App):
        surf = App.surface
        margin_x = 0
        margin_y = 50
        margin_yt = margin_y + 40
        margin_yt_between_texts = 50

        credits = Text(App, "Credits", (0, 5), App.assets.ocr_font40, (255, 255, 255), "x")
        credits.draw(App.uiSurface)

        sc_text = Text(App, "Created originally by Scott Cawthon", (margin_x, margin_y) , App.assets.ocr_font20, (255, 255, 255), lock="x")
        sc_text.draw(surf)

        thanks_subs = Text(App, "Thanks to all and every sub from okxd, you really mean a lot to me!", (margin_x, margin_y) , App.assets.ocr_font30, (255, 255, 255), lock="x")
        

        names = import_names()
        for i in range(len(names)):
            info = names[i].split(",")

            t = Text(App, str(info[0]), (margin_x, margin_yt + margin_yt_between_texts*(i)) - self.scroll_down, App.assets.ocr_font20, (255, 255, 255), lock="x")

            click = pygame.mouse.get_pressed()
            if (len(info) > 1):
                link = info[1]
                if t.getHitbox().colliderect(App.mouse_hitbox):
                    t.underline(True)
                    if (click[0] and not self.mouse_pressed):
                        pyperclip.copy(info[1])
                        self.mouse_pressed = True
                        print("text copied!")
            else:
                t.underline(False)

            t.draw(surf)
        
        if (click == (False, False, False)): self.mouse_pressed = False

        App.menu.menu_exit(App)