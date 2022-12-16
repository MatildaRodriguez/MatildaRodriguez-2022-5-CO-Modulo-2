import pygame

from dino_runner.utils.constants import FONT_STYLE


class Element:
  def __init__(self):
    self.element = 0
    
  def update(self):
    self.element += 1
    
  def draw(self, screen):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(f'Score: {self.element}', True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    screen.blit(text, text_rect)
    
  def reset(self):
    self.element = 0
    
  def set_element(self, value):
    self.element = value