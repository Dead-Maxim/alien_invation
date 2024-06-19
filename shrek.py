import pygame
from pygame.sprite import Sprite


class Shrek(Sprite):
    """Класc шрека"""

    def __init__(self, ai_game):  # аргумент - объект игры
        """Инициализирует шрека и задает его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        # загружает изображение шрека
        image = pygame.image.load("images/shrek.bmp")
        # подгоняем размер шрека
        self.image = pygame.transform.scale(image, (75, 100))
        self.rect = self.image.get_rect()
        # шрек появляется в центре
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # сохранение горизонтальной позиции
        self.x = float(self.rect.x)

    def blitme(self):
        """Рисует шрека в текущей позиции"""
        self.screen.blit(self.image, self.rect)
