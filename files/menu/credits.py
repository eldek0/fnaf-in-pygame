import pygame
from files.Text import Text

def import_names() ->list:
    with open("files/cre.txt", "r") as pk:
        names = pk.readlines()
    return names

class Credits:
    def __init__(self):
        pass

    def update(self, App):
        margin_x = 100
        margin_y = 50
        margin_yt = margin_y + 100
        margin_yt_between_texts = 50

        sc_text = Text(App, "Created originally by Scott Cawthon", (margin_x, margin_y) , App.assets.ocr_font, (255, 255, 255), lock="x")
        sc_text.draw(App.surface)
        names = import_names()
        for i in range(len(names)):
            info = names[i].split(",")

            t = Text(App, str(names[i]), (margin_x, margin_yt + margin_yt_between_texts*(i+1)), App.assets.ocr_font, (255, 255, 255), lock="x")

            t.draw(App.surface)