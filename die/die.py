from random import randint

class Die:
    """Класс представляющий один кубик."""
    def __init__(self, num_sides=6):
        """По умолчанию используется шестигранный кубик"""
        self.num_sides = num_sides

    def roll(self):
        """Возвращая случайное число от 1 до количества граней"""
        return randint(1, self.num_sides)