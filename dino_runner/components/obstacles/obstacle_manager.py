import pygame

from dino_runner.utils.constants import SMALL_CACTUS

from dino_runner.components.obstacles.cactus import Cactus

from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self,game):
        cactus = Cactus(SMALL_CACTUS)
        if len(self.obstacles) == 0:
            self.obstacles.append (cactus)
        
        elif len(self.obstacles) == 0 :
            bird = Bird(BIRD)
            self.obstacles(bird)
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect (obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break
        

    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
