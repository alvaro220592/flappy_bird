import constants
import pygame
from classes.objects.object import Object
from classes.objects.pipe import Pipe

class Game:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.sky01 = Object('assets/img/sky.png', 0, 0, self.all_sprites)
        self.sky02 = Object('assets/img/sky.png', constants.SCREEN['WIDTH'], 0, self.all_sprites)
        self.pipe01 = Pipe('assets/img/pipe1.png', 300, 400, self.all_sprites)
        self.pipe02 = Pipe('assets/img/pipe2.png', 300, -100, self.all_sprites)
        self.ground01 = Object('assets/img/ground.png', 0, constants.SCREEN['HEIGHT'] - 164, self.all_sprites)
        self.ground02 = Object('assets/img/ground.png', constants.SCREEN['WIDTH'], constants.SCREEN['HEIGHT'] - 164, self.all_sprites)

        self.move_ground()
        self.move_sky()

    def draw(self, screen):
        self.all_sprites.draw(screen)
        self.move_ground()
        self.move_sky()
        self.pipe01.move()
        self.pipe02.move()

    def update(self):
        self.move_sky()
        self.move_ground()
        self.all_sprites.update()

    def move_sky(self):
        self.sky01.rect[0] -= constants.SKY['SPEED']
        self.sky02.rect[0] -= constants.SKY['SPEED']
        if self.sky01.rect[0] <= -constants.SCREEN['WIDTH']:
            self.sky01.rect[0] = 0

        if self.sky02.rect[0] <= 0:
            self.sky02.rect[0] = constants.SCREEN['WIDTH']

    def move_ground(self):
        self.ground01.rect[0] -= constants.GROUND['SPEED']
        self.ground02.rect[0] -= constants.GROUND['SPEED']
        if self.ground01.rect[0] <= -constants.SCREEN['WIDTH']:
            self.ground01.rect[0] = 0
        
        if self.ground02.rect[0] <= 0:
            self.ground02.rect[0] = constants.SCREEN['WIDTH']

    