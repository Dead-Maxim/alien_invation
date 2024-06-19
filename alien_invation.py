import sys
import pygame

from settings import Settings
from ship import Ship
from shrek import Shrek
from bullet import Bullet


class AlienInvation:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        # инициализация настроек
        pygame.init()
        # присвоение настроек
        self.settings = Settings()
        # запуск окна игры с указанием размера
        # self.screen = pygame.display.set_mode(
        #    (self.settings.screen_width, self.settings.screen_heiht)
        # )
        # запуск в полноэкранном режиме
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_heiht = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        # название окна
        pygame.display.set_caption("Alien Invation")
        # выводим корабль
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        # выводим Шрека
        self.shrek = Shrek(self)

    def run_game(self):
        """Зауск основного цикла игры"""
        while True:
            # Отслеживание событий клавиатуры и мыши
            self._check_events()
            # стреляем
            self._update_bullets()
            # рисуем экран
            self._update_screen()
            # проверяем надоли двигаться
            self.ship.update()

    def _check_events(self):
        """Отслеживат события на клавиатуре"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # если событие нажатие клавиши
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            # если событие клавиша отпущена
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        """Нажатие клавиш"""
        # если эта клавиша вправо
        if event.key == pygame.K_RIGHT:
            # меняем флаг передвижения вправо на истину
            self.ship.moving_right = True
        # если это клавиша влево
        elif event.key == pygame.K_LEFT:
            # меняем флаг передвижения влево на истину
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        # пробел - стрельба
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        """Отпускание клавиш"""
        # эта клавиша вправо
        if event.key == pygame.K_RIGHT:
            # меняем флаг движения вправо на ложь
            self.ship.moving_right = False
        # эта клавиша влево
        elif event.key == pygame.K_LEFT:
            # меняем флаг движения влево на ложь
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # Удаление снарядов, вышедших за пределы экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _update_screen(self):
        """Отрисовывает экран"""
        # перерисовывание экрана при проходе цикла
        # и напролнение его цветом фона
        self.screen.fill(self.settings.bg_color)
        # рисуем корабль
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Отображение последнего прорисованного экрана
        pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvation()
    ai.run_game()
