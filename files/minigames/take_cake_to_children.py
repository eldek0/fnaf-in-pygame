import pygame, random
from files.minigames.dummy import MinigameDummy
from files.minigames.entity import Entity
from files.minigames.scenes.take_cake_scene import TakeCakeToTheChildrenScene

class TakeCakeToTheChildren(MinigameDummy):
    def __init__(self, App):
        super().__init__(App)
        self.freadbear = Entity(App.animations.cake_fred_walking, (350, 450))
        self.sceneElements = TakeCakeToTheChildrenScene(App, self)

        self.childs = []
        x_separation = 600
        y_separation = 130
        for i in range(6):
            self.childs.append(
                [Entity(App.animations.various_childs_anim[i][0], (160 + x_separation*((i)%2), 260 + y_separation*(i//2)) ),
                 pygame.time.get_ticks(), random.randint(5000, 9000)]
            )

        self.sad_child = Entity(App.animations.sad_child_anim, (300, 70))

        self.car = Entity(App.assets.car, (App.surface.get_width() + 300, 60), framesToMove=500, speed=35)

        self.purple_guy = Entity(App.assets.small_purple_guy, (420, 15))
        self.purple_guy.desactivate()

        self.timer = pygame.time.get_ticks()
        self.car_to_appear = 0
        self.game_state = 0
        self.child_state = 2

    def update(self, App):
        self.sceneElements.update(App, self.scene, self)

        self.draw_scene(App)

        self.key_movement(App)

        self.freadbear.update()

        self.update_child_wait(App)

        self.update_scene(App)

    def draw_scene(self, App):
        rooms = self.sceneElements.rooms
        # Add the childs
        for i in range(len(self.childs)):
            child = self.childs[i][0]
            rooms[self.scene].append(
                (child.texture, tuple(child.position), lambda index=i:self.feed_child(index), False)
            )
            child.update()

        # Add the car
        rooms[self.scene].append(
            (self.car.texture, tuple(self.car.position))
        )

        # Add purple guy
        if self.purple_guy.is_activated():
            rooms[self.scene].append(
                (self.purple_guy.texture, tuple(self.purple_guy.position))
            )

        # Add the sad child
        rooms[self.scene].append(
            (self.sad_child.texture, tuple(self.sad_child.position))
        )

        self.draw_boundaries(App, rooms[0], self.freadbear)
        
        width = App.surface.get_width()
        label_width = App.assets.take_cake_to_the_children_label.get_width()
        App.minigamesSurface.blit(App.assets.take_cake_to_the_children_label, (width/2 - label_width/2, 680))

    def feed_child(self, index):
        self.childs[index][1] = pygame.time.get_ticks()

    def update_child_wait(self, App):
        for i in range(len(self.childs)):
            time = self.childs[i][1]
            tolerance = self.childs[i][2]
            if (pygame.time.get_ticks() - time > tolerance*2): # GET MAD
                self.childs[i][0].texture = App.animations.various_childs_anim[i][2]
            elif (pygame.time.get_ticks() - time > tolerance): # GET ANGRY
                self.childs[i][0].texture = App.animations.various_childs_anim[i][1]
            elif (pygame.time.get_ticks() - time >= 0): # GET NORMAL
                if self.childs[i][0].texture != App.animations.various_childs_anim[i][0]:
                    pygame.mixer.Channel(1).play(App.assets.pop)
                self.childs[i][0].texture = App.animations.various_childs_anim[i][0]


    def key_movement(self, App):
        key = pygame.key.get_pressed()

        if (key[pygame.K_RIGHT] or key[pygame.K_d]):
            self.freadbear.movement('r')
        
        elif (key[pygame.K_LEFT] or key[pygame.K_a]):
            self.freadbear.movement('l')

        elif (key[pygame.K_UP] or key[pygame.K_w]):
            self.freadbear.movement('u')

        elif (key[pygame.K_DOWN] or key[pygame.K_s]):
            self.freadbear.movement('d')

    def update_scene(self, App):
        match self.game_state:
            case 0:
                if pygame.time.get_ticks() - self.timer > self.car_to_appear:
                    self.car.movement("l")
                    self.car.update()

                    if self.car.position[0] <= 200:
                        self.update_game_state()

            case 1:
                self.purple_guy.activate()
                self.update_game_state()
            
            case 2:
                if pygame.time.get_ticks() - self.timer > 2000:
                    self.child_state += 1
                    if (self.child_state < 7):
                        self.sad_child.texture = App.assets.child_crying_states[self.child_state]
                        self.timer = pygame.time.get_ticks()
                    else:
                        self.update_game_state()
            
            case 3:
                if pygame.time.get_ticks() - self.timer > 4000:
                    self.sad_child.texture = App.assets.dead_child
                    self.update_game_state()
                    self.freadbear.speed = 8

            case 4:
                self.freadbear.speed = 5
                if pygame.time.get_ticks() - self.timer > 3000:
                    self.purple_guy.desactivate()
                    self.update_game_state()

            case 5:
                self.freadbear.speed = 1
                self.car.movement("l")
                self.car.update()

                if self.car.position[0] <= -90:
                    self.jumpscare(App, App.animations.puppet_jump)


    def update_game_state(self):
        self.game_state += 1
        self.timer = pygame.time.get_ticks()