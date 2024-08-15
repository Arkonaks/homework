n = int(input("Введите число от 3 до 20: "))
result = ''

for a in range(1, n):
    for b in range(1, n):
        if n % (a + b) == 0:
            result += (f"{a}{b}")

if n < 3 or n > 20:
    print('Введенно неправльное число')
else:
    print(f"Ваш пароль: {result}")