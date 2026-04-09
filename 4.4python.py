from math import *

try:
     a = float(input("Введите начало a: "))
     b = float(input("Введите конец b: "))
     h = float(input("Введите шаг h (h != 0): "))
except ValueError:
     print("Неккоректное значение, введите числа!")
     exit()
if (a > b and h > 0) or h == 0:
       print("Неккоректное значение h!")
       exit()

print("x\t\tF(x)")

if a > b:
       x = b
       while x <= a:
        if sin(x) == 0: ## ctg = cos/sin
             print(f"{x:.3f}\t\tне определена")
             x -= h
        else:
              result = cos(x) / sin(x) + 1
              print(f"{x:.3f}\t\t{result:.3f}")
              x -= h
if a < b:
       x = a
       while x <= b:
        if sin(x) == 0: ## ctg = cos/sin
             print(f"{x:.3f}\t\tне определена")
             x += h
        else:
              result = cos(x) / sin(x) + 1
              print(f"{x:.3f}\t\t{result:.3f}")
              x += h
