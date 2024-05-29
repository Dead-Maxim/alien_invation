import sys
import pygame

from settings import Settings
from ship import Ship
from shrek import Shrek


class AlienInvation:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        # инициализация настроек
        pygame.init()
        # присвоение настроек
        self.settings = Settings()
        # запуск окна игры с указанием размера
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_heiht)
        )
        # название окна
        pygame.display.set_caption("Alien Invation")
        # выводим корабль
        self.ship = Ship(self)
        # выводим Шрека
        self.shrek = Shrek(self)

    def run_game(self):
        """Зауск основного цикла игры"""
        while True:
            # Отслеживание событий клавиатуры и мыши
            self._check_events()
            # рисуем экран
            self._update_screen()

    def _check_events(self):
        """Отслеживат события на клавиатуре"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 1
                elif event.key == pygame.K_LEFT:
                    self.ship.rect.x -= 1

    def _update_screen(self):
        """Отрисовывает экран"""
        # перерисовывание экрана при проходе цикла
        # и напролнение его цветом фона
        self.screen.fill(self.settings.bg_color)
        # рисуем корабль
        self.ship.blitme()
        # рисуем Шрека
        self.shrek.blitme()
        # Отображение последнего прорисованного экрана
        pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvation()
    ai.run_game()
