from files.ui.button import Button
from files.scenes.office import Office
from files.scenes.camera import Camera
from files.ui.camera_button import CameraButton
from files.animatronics.animatronics_main import AnimatronicsMain
from files.ui.music_box import MusicBoxButton
from files.ui.mask_button import MaskButton
from files.ui.battery import Battery
from files.ui.game_timer import GameTimer

class GameObjects:
    def __init__(self, App):
        # Monitor button
        self.open_monitor_button = CameraButton(App, draw_box=False)
        
        # Mask button
        self.mask_button = MaskButton(App, draw_box=False)

        # Office class
        self.office = Office(App)

        # Camera class
        self.camera = Camera(App)
        
        self.battery = Battery(App)

        self.gameTimer = GameTimer(App)

        # Animatronics manager
        self.Animatronics = AnimatronicsMain(App)

        # Puppet's music box
        self.music_box = MusicBoxButton(App, (300, 500))