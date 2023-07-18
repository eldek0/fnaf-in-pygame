import pygame

def text(surface:pygame.Surface, txt:str, position:tuple, FUENTE:pygame.font, COLOR:tuple):
	font_text = FUENTE.render(txt, 1, (COLOR))
	surface.blit(font_text, position)