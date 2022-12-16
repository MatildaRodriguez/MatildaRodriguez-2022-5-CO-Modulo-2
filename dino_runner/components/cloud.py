import random
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD


class Cloud (Sprite):
    def __init__(self):
        self.image = CLOUD 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 300
        self.dino_rect.y = 90
        self.dino_run = True

    def draw (self, screen):
        screen.blit(self.image, (self.dino_rect.x , self.dino_rect.y)) 
        #self.type = random.randint(0,1)
