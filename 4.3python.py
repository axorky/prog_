try:
    p = float(input(("Введите значение p (Число которое должно быть меньше модуля числа на числовом ряду): ")))
except (ValueError, TypeError):
    print("Неправильный ввод числа p!")
    
def fct(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

total_sum = 0.0
max_iterations = int(input(("Введите максимальное число итераций для вычисления суммы: ")))
# Счетчик итераций для защиты от бесконечного цикла
for n in range(1, max_iterations+1):
    a = 10**n / fct(n)
    n += 1
    if abs(a) >= p:
        total_sum += a
# Проверка на достижение максимального количества итераций
print(f"Предупреждение: достигнут лимит итераций ({max_iterations}).")
print(f"Ваша сумма членов числового ряда: {total_sum:.3f}")