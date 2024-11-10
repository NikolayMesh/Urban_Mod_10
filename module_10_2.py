import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.delay = 1
        self.day = 0
        self.counter = 100

    def timer(self, counter, power, delay):
        while self.counter:
            self.day += 1
            self.counter -= self.power
            time.sleep(delay)
            print(f'{self.name} сражается {self.day} дней(дня)..., осталось {self.counter} войнов.')


    def run(self):
        print(f'{self.name}, на нас напали!')
        self.timer(self.name, self.power, self.delay)
        print(f'{self.name}, одержал победу спустя {self.day} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков
first_knight.start()
second_knight.start()
# Ожидание завершения
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')