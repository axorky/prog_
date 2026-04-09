from math import factorial as fctr

try:
    x = float(input("Введите число x: ")) ## ввод
except ValueError:
    print("Неккоректный ввод числа!")
    exit()
y = 0 ## результат
MP = 1 ## знак

for n in range(1, 14, 2):
    term = MP * (x**n/fctr(n)) 
    y += term  ## считаем сумму
    MP *= -1  ## меняем знак

print(f"Результат уравнения: {y}")