from math import factorial as fct
try:
    p = float(input(("Введите значение p (Число которое должно быть меньше модуля числа на числовом ряду): ")))
except (ValueError, TypeError):
    print("Неправильный ввод числа p!")
    
total_sum = 0.0
n = 0 # начало ряда (первый член ряда)
max_iterations = int(input(("Введите максимальное число итераций для вычисления суммы: ")))
# Счетчик итераций для защиты от бесконечного цикла
iteration_count = 0
a = 0
while iteration_count < max_iterations:
    if abs(a) >= p:
        total_sum += a
    a = 10**n / fct(n)
    # Переход к следующему члену ряда
    n += 1
    iteration_count += 1
    total_sum += a
# Проверка на достижение максимального количества итераций
print(f"Предупреждение: достигнут лимит итераций ({max_iterations}).")
print(f"Ваша сумма членов числового ряда: {total_sum}")