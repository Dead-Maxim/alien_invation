import pygame


class Ship:
    """Класc управления кораблем"""

    def __init__(self, ai_game):  # аргумент - объект игры
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = ai_game.screen
        # получаем данные экрана
        self.screen_rect = ai_game.screen.get_rect()
        # загружает изображение корабля
        image = pygame.image.load("images/ship.bmp")
        # подгоняем размер корабля
        self.image = pygame.transform.scale(image, (75, 100))
        self.rect = self.image.get_rect()
        # корабль появляется у нижненго края
        self.rect.midbottom = self.screen_rect.midbottom
        # флаги перемещения по умолчанию ложь
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флагов"""
        # при получении флага True, меняет положение корабля
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
