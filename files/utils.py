import pygame

def text(surface:pygame.Surface, txt:str, position:tuple, FUENTE:pygame.font, COLOR:tuple):
	font_text = FUENTE.render(txt, 1, (COLOR))
	surface.blit(font_text, position)

def draw_hitbox(surf:pygame.surface.Surface, color:tuple, rect:pygame.Rect):
	x = rect.x
	y = rect.y
	w = rect.width
	h = rect.height
	color = color
	pygame.draw.line(surf, color, (x, y), (x + w, y), 1)
	pygame.draw.line(surf, color, (x + w, y), (x + w, y + h), 1)
	pygame.draw.line(surf, color, (x, y), (x, y + h), 1)
	pygame.draw.line(surf, color, (x, y + h), (x + w, y + h), 1)

def get_shader_diff(surface:pygame.surface.Surface) -> tuple:
	ini_size = surface.get_size()
	window_size = pygame.display.get_window_size()
	return ((window_size[0] - ini_size[0])/window_size[0], (window_size[1] - ini_size[1])/window_size[1])

def transform_rect(surface:pygame.surface.Surface, rect:pygame.Rect):
	diff = get_shader_diff(surface)
	rect.x += diff[0]
	rect.y += diff[1]
	rect.w += diff[0]
	rect.h += diff[1]