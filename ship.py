import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('C:/Users/jiang-work/PycharmProjects/myFirstPygame/image/gieo784eT.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        #在飞船属性x中储存小数值
        self.x = float(self.rect.x)
        #移动标志
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """adjust the position of the ship"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed

        self.rect.x = self.x


    def blitme(self):
        self.screen.blit(self.image, self.rect)

