import pygame

from files.animatronics.animatronic_base import Animatronic

class WitheredChica(Animatronic):
	def __init__(self, App, aggresivity:int, custom_index:int):
		super().__init__(aggresivity, 8, App.animations.withered_chica_jump, 4, custom_index)

	def movement(self, App):
		withered_bonnie = App.objects.Animatronics.animatronics_in_game["WITHERED_BONNIE"]

		match self.locationId:
			case 8:
				if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
					if withered_bonnie.locationId != 8:
						self.change_location_id(App, 4)
					else:
						self.timer = pygame.time.get_ticks()
				
			case 4:
				if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
					self.change_location_id(App, 2)

			case 2:
				if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
					self.change_location_id(App, 6)

			case 6:
				if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity and App.objects.open_monitor_button.inCamera:
					self.change_location_id(App, 104)