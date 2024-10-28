import time
import random
import threading

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            x = random.randint(50, 500)
            with self.lock:
                self.balance += x
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
                print(f'Пополнение {x}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            y = random.randint(50, 500)
            print(f'Запрос на {y}.')
            if y <= self.balance:
                print(f'Снятие {y}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

if __name__ == "__main__":
    bk = Bank()

    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')
