import constants
from classes.objects.object import Object


class Pipe(Object):
    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

    def update(self):
        self.move()

    def move(self):
        self.rect[0] -= constants.GROUND['SPEED']
        if self.rect[0] == -100:
            self.kill()