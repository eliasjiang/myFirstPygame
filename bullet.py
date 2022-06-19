import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """manage the class of the Bullet"""

    def __init__(self, ai_game):
        """create a bullet object in where the ship stand"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a rectangle as bullet at(0,0),then set the right position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # set the position of the bullet using float
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
