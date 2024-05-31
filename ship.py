import pygame


class Ship:
    """Класc управления кораблем"""

    def __init__(self, ai_game):  # аргумент - объект игры
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # получаем данные экрана
        self.screen_rect = ai_game.screen.get_rect()
        # загружает изображение корабля
        image = pygame.image.load("images/ship.bmp")
        # подгоняем размер корабля
        self.image = pygame.transform.scale(image, (75, 100))
        self.rect = self.image.get_rect()
        # корабль появляется у нижненго края
        self.rect.midbottom = self.screen_rect.midbottom
        # сохранение вещественной координаты корабля
        self.x = float(self.rect.x)
        # флаги перемещения по умолчанию ложь
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флагов"""
        # при получении флага True, меняет положение корабля
        # сравнивает текущие координаты с краями экрана
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # обновляем rect
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
