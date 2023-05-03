import pygame
import constants
from classes.scenes.game import Game


class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((constants.SCREEN['WIDTH'], constants.SCREEN['HEIGHT']))
        self.title = pygame.display.set_caption(constants.TITLE)
        self.running = True
        self.fps = pygame.time.Clock()
        self.game = Game()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False

    def draw(self):
        self.game.draw(self.screen)
        self.game.update()

    def update(self):
        while self.running:
            self.fps.tick(constants.FPS)
            self.events()
            self.draw()
            pygame.display.update()

Main().update()