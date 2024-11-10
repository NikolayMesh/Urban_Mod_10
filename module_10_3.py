import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            randon_add = random.randint(50, 500)
            with self.lock:
                self.balance += randon_add
                print(f"Пополнение: {randon_add}. Баланс: {self.balance}")
                if self.balance >= 500:
                    print("Баланс достиг 500 или более, разблокировка.")
            time.sleep(0.001)  # Имитация времени выполнения операции

    def take(self):
        for i in range(100):
            randon_take = random.randint(50, 500)
            print(f'Запрос на {randon_take}')
            with self.lock:
                if self.balance >= randon_take:
                    self.balance -= randon_take
                    print(f'Снятие: {randon_take}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
            time.sleep(0.001)  # Имитация времени выполнения операции


# Создание объекта класса Bank
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}')