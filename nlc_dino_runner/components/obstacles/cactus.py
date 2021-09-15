import random

from nlc_dino_runner.components.obstacles.obstacles import Obstacles
# from nlc_dino_runner.utils.constants import SMALL_CACTUS


# Clase hija
class Cactus(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 315

    # def update(self, *args, **kwargs) -> None:
    #     pass
    #
    # def draw(self):
    #     pass
