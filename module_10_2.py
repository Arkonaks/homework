import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            time.sleep(1)
            self.timer()

    def timer(self):
        self.enemies -= self.power
        if self.enemies < 0:
            self.enemies = 0
        self.days += 1
        print(f'{self.name} сражается {self.days} дня (дней)..., осталось {self.enemies} войнов.')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Битвы закончены')
