import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_count():
    """Проверка корректности ввода количества элементов"""
    while True:
        try:
            count = int(input("Введите количество элементов (1-10000): "))

            if 1 <= count <= 10000:
                return count

            print("Ошибка: число должно быть в диапазоне от 1 до 10000.")

        except ValueError:
            print("Ошибка: необходимо ввести целое число.")

# Ввод данных
count = get_count()

# Генерация данных
numbers = [random.randint(-10000, 10000) for _ in range(count)]

series = pd.Series(numbers)

# Анализ данных (Pandas)
min_value = series.min()
max_value = series.max()
sum_value = series.sum()
std_value = series.std()
duplicates = series.duplicated().sum()

# Анализ данных (NumPy)
mean_value = np.mean(numbers)
median_value = np.median(numbers)

# Использование Math
variance = np.var(numbers)
std_math = math.sqrt(variance)

# Вывод результатов
print("\nРезультаты анализа\n")

print("Количество элементов:", len(series))
print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Сумма элементов:", sum_value)

print("Среднее значение (NumPy):", round(mean_value, 2))
print("Медиана (NumPy):", median_value)

print("Среднеквадратическое отклонение (Pandas):",
      round(std_value, 2))

print("Среднеквадратическое отклонение (Math + NumPy):",
      round(std_math, 2))

print("Количество повторяющихся элементов:",
      duplicates)

# Фрагмент данных
print("\nПервые 10 элементов набора:")
print(series.head(10))

# DataFrame
df = pd.DataFrame({
    "Исходные данные": series
})

df["По возрастанию"] = (
    series.sort_values()
    .reset_index(drop=True)
)

df["По убыванию"] = (
    series.sort_values(ascending=False)
    .reset_index(drop=True)
)

# Подготовка данных
rounded = series.apply(
    lambda x: round(x, -2)
)

# Визуализация
fig = plt.figure(figsize=(14, 10))

plt.subplot(3, 1, 1)
plt.plot(series)
plt.title("Линейный график исходного набора данных")
plt.xlabel("Номер элемента")
plt.ylabel("Значение")
plt.grid()

plt.subplot(3, 1, 2)
plt.hist(rounded, bins=30)
plt.title("Гистограмма распределения данных")
plt.xlabel("Значение")
plt.ylabel("Количество")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(df["По возрастанию"])
plt.plot(df["По убыванию"])
plt.title("Сравнение отсортированных данных")
plt.xlabel("Номер элемента")
plt.ylabel("Значение")
plt.legend(["Возрастание", "Убывание"])
plt.grid()

plt.tight_layout()
plt.show()