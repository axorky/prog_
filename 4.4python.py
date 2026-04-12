from math import *
from tabulate import tabulate


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

table = []

if a > b:
       x = b
       while x < a:
        if sin(x) == 0: ## ctg = cos/sin
               table_val = "не определена"
               x -= h
               table.append([round(x, 3), table_val])
        else:
               result = cos(x) / sin(x) + 1
               table_val = round(cos(x) / sin(x) + 1, 3)
               x -= h
               table.append([round(x, 3), table_val])
if a < b:
       x = a
       while x < b:
        if sin(x) == 0: ## ctg = cos/sin
               table_val = "не определена"
               x += h
               table.append([round(x, 3), table_val])
        else:
               result = cos(x) / sin(x) + 1
               table_val = round(cos(x) / sin(x) + 1, 3)
               x += h
               table.append([round(x, 3), table_val])

print(tabulate(table, headers=["x", "f(x)"], tablefmt="grid"))