from files.animations.sprites_animation import SpritesAnimation
from files.animations.darkness_effect import DarknessAnimation

class animations_init:
    def __init__(self, App):
        self.monitor = SpritesAnimation(sprites=App.assets.camera_sprites, position=(0, 0))

        self.mask = SpritesAnimation(sprites=App.assets.mask_sprites[0:9], position=(0, 0), frame_wait=1)

        self.desk = SpritesAnimation(sprites=App.assets.desk_animation, position=(0, 0), frame_wait=4, isLoop=True)

        self.static_anim_1 = SpritesAnimation(sprites=App.assets.static_1, position=(0, 0), alpha=255, isLoop=True)

        self.static_anim_2 = SpritesAnimation(sprites=App.assets.static_2, position=(0, 0), frame_wait=3)

        self.darkness = DarknessAnimation(App=App, position=(0,0), frame_wait=3, fading_time=15000)

        # -- Jumpscares --
        self.puppet_jump = SpritesAnimation(sprites=App.assets.puppet_screamer_animation, position=(0, 0), frame_wait=2)
        self.toy_bunny_jump = SpritesAnimation(sprites=App.assets.toy_bunny_screamer_animation, position=(0, 0), frame_wait=2)
        self.toy_chica_jump = SpritesAnimation(sprites=App.assets.toy_chica_screamer_animation, position=(0, 0), frame_wait=2)