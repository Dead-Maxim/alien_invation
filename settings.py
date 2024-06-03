class Settings():
    """Класс настроек игры"""
    # параметры экрана
    def __init__(self):
        # ширина игрового окна
        self.screen_width = 1200
        # высота игрового окна
        self.screen_heiht = 800
        # цвет фона RGB от 0 до 255
        self.bg_color = (230, 230, 230)
        # скорость перемещения корабля
        self.ship_speed = 1.5
        # параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullrt_color = (60, 60, 60)
