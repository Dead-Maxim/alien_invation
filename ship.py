import pygame


class Ship:
    """Класc управления кораблем"""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # загружает изображение корабля
        image = pygame.image.load("images/ship.bmp")
        # подгоняем размер корабля
        self.image = pygame.transform.scale(image, (75, 100))
        self.rect = self.image.get_rect()
        # корабль появляется у нижненго края
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
