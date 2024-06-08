import pygame


class Shrek:
    """Класc шрека"""

    def __init__(self, ai_game):  # аргумент - объект игры
        """Инициализирует шрека и задает его начальную позицию"""
        self.screen = ai_game.screen
        # получаем данные экрана
        self.screen_rect = ai_game.screen.get_rect()
        # загружает изображение корабля
        image = pygame.image.load("images/shrek.bmp")
        # подгоняем размер шрека
        self.image = pygame.transform.scale(image, (150, 200))
        self.rect = self.image.get_rect()
        # шрек появляется в центре
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Рисует шрека в текущей позиции"""
        self.screen.blit(self.image, self.rect)
