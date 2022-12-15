import random

from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacles

class Bird (Obstacles):

    def __init__(self, image):
        self.image = BIRD
        self.bird_rect = self.image.get.rect()
        self.bird_rect.y = random.randint(0,2)
        self.fly_index = 0
        self.type = image
        super ().__init__ (image,self.type)
        self.rect.y = 325

    def fly (self):
        self.image = BIRD [0] if self.fly_index < 5 else BIRD [1]
        self.bird_rect = self.image.get_rect()
        self.fly_index += 1

