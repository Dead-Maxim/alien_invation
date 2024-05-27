import sys
import pygame


class AlienInvation:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        # инициализация настроек
        pygame.init()
        # запуск окна игры с указанием размера
        self.screen = pygame.display.set_mode((1200, 800))
        # название окна
        pygame.display.set_caption("Alien Invation")
        # цвет фона RGB от 0 до 255
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Зауск основного цикла игры"""
        while True:
            # Отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # перерисовывание экрана при проходе цикла
            # и напролнение его цветом фона
            self.screen.fill(self.bg_color)
            # Отображение последнего прорисованного экрана
            pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvation()
    ai.run_game()
