import numpy as np
import matplotlib.pyplot as plt

# ВВОД ДАННЫХ
print("Решение задачи линейного программирования графическим методом")
print("=" * 50)

# Целевая функция
print("\nВведите целевую функцию:")
print("Пример: 2*x + 3*y")
a = float(input("Коэффициент перед x: "))
b = float(input("Коэффициент перед y: "))
direction = input("max или min? ")

# Количество ограничений (без x>=0 и y>=0, они добавятся автоматически)
n = int(input("\nСколько основных ограничений (без x>=0, y>=0)? "))

constraints = []
print("\nВведите ограничения (каждое с новой строки):")
for i in range(n):
    print(f"\nОграничение {i + 1}:")
    a_i = float(input("Коэффициент перед x: "))
    b_i = float(input("Коэффициент перед y: "))
    op = input("Знак (<=, >=, =): ")
    c_i = float(input("Правая часть: "))
    constraints.append([a_i, b_i, op, c_i])

# ВСЕГДА добавляем условия неотрицательности
constraints.append([1, 0, '>=', 0])  # x >= 0
constraints.append([0, 1, '>=', 0])  # y >= 0

# РЕШЕНИЕ
print("\n" + "=" * 50)
print("РЕШЕНИЕ:")

# Создаем график
fig, ax = plt.subplots(figsize=(8, 6))

# Строим ограничения
x_vals = np.linspace(0, 20, 400)
for i, (a_i, b_i, op, c_i) in enumerate(constraints):
    if b_i != 0:  # Не вертикальная линия
        y_vals = (c_i - a_i * x_vals) / b_i
        ax.plot(x_vals, y_vals, label=f'{a_i}*x + {b_i}*y {op} {c_i}')
    else:  # Вертикальная линия x = c/a
        if a_i != 0:
            x_val = c_i / a_i
            ax.axvline(x=x_val, label=f'x {op} {c_i / a_i:.1f}')

# НАХОДИМ ВСЕ ВОЗМОЖНЫЕ ТОЧКИ ПЕРЕСЕЧЕНИЯ
all_points = []

# 1. Пересечения основных линий между собой (кроме осей)
for i in range(len(constraints) - 2):  # -2 чтобы не считать пересечения с осями
    for j in range(i + 1, len(constraints) - 2):  # только основные ограничения
        a1, b1, op1, c1 = constraints[i]
        a2, b2, op2, c2 = constraints[j]

        # Пропускаем, если линии параллельны (оба коэффициента нулевые для одной переменной)
        if (a1 == 0 and a2 == 0) or (b1 == 0 and b2 == 0):
            continue

        determinant = a1 * b2 - a2 * b1

        if abs(determinant) > 0.0001:
            x = (c1 * b2 - c2 * b1) / determinant
            y = (a1 * c2 - a2 * c1) / determinant
            all_points.append((x, y))

# 2. Пересечения с осями для основных ограничений
for i in range(len(constraints) - 2):  # только основные ограничения
    a_i, b_i, op, c_i = constraints[i]

    # Пересечение с осью X (y=0)
    if a_i != 0:
        x = c_i / a_i
        all_points.append((x, 0))

    # Пересечение с осью Y (x=0)
    if b_i != 0:
        y = c_i / b_i
        all_points.append((0, y))

# 3. Добавляем начало координат
all_points.append((0, 0))

# 4. Фильтруем точки: должны удовлетворять ВСЕМ ограничениям
valid_points = []
print("\nВсе возможные точки пересечения:")
for i, (x, y) in enumerate(all_points):
    # Проверяем все ограничения
    valid = True
    for a_i, b_i, op, c_i in constraints:
        left_side = a_i * x + b_i * y

        if op == '<=':
            if left_side > c_i + 0.001:
                valid = False
                break
        elif op == '>=':
            if left_side < c_i - 0.001:  # Здесь должно быть строгое условие!
                valid = False
                break
        elif op == '=':
            if abs(left_side - c_i) > 0.001:
                valid = False
                break

    if valid and x >= 0 and y >= 0:
        valid_points.append((x, y))
        print(f"Точка {chr(65 + i)}: ({x:.2f}, {y:.2f})")

# Удаляем дубликаты (округляем до 2 знаков)
unique_points = []
for point in valid_points:
    rounded = (round(point[0], 2), round(point[1], 2))
    if rounded not in unique_points:
        unique_points.append(rounded)

# Вычисляем целевую функцию в вершинах
print("\nАнализ вершин области:")
best_F = float('inf') if direction == 'min' else -float('inf')
best_point = None
results = []

for i, (x, y) in enumerate(unique_points):
    F_val = a * x + b * y
    results.append((x, y, F_val))
    print(f"Вершина {chr(65 + i)}: ({x:.2f}, {y:.2f}) -> F = {F_val:.2f}")

    if direction == 'min' and F_val < best_F:
        best_F = F_val
        best_point = (x, y)
    elif direction == 'max' and F_val > best_F:
        best_F = F_val
        best_point = (x, y)

# Вывод результата
if best_point:
    print(f"\nОПТИМАЛЬНОЕ РЕШЕНИЕ:")
    print(f"x = {best_point[0]:.2f}")
    print(f"y = {best_point[1]:.2f}")
    print(f"F = {best_F:.2f}")

    # Закрашиваем область
    if len(unique_points) >= 3:
        # Сортируем точки для правильного многоугольника
        # Находим центр
        center_x = sum(p[0] for p in unique_points) / len(unique_points)
        center_y = sum(p[1] for p in unique_points) / len(unique_points)

        # Сортируем по углу относительно центра
        sorted_points = sorted(unique_points,
                               key=lambda p: np.arctan2(p[1] - center_y, p[0] - center_x))

        polygon = plt.Polygon(sorted_points, alpha=0.3, color='yellow')
        ax.add_patch(polygon)

    # Отмечаем все вершины
    for i, (x, y) in enumerate(unique_points):
        ax.plot(x, y, 'ko', markersize=8)
        ax.text(x + 0.2, y + 0.2, chr(65 + i), fontweight='bold')

    # Оптимальная точка
    ax.plot(best_point[0], best_point[1], 'r*', markersize=15, label='Оптимум')

    # Линия уровня
    if b != 0:
        y_level = (best_F - a * x_vals) / b
        ax.plot(x_vals, y_level, 'k--', linewidth=2, label=f'F = {best_F:.1f}')
else:
    print("\nНе удалось найти решение")

# Настройка графика
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(f'F = {a}*x + {b}*y -> {direction}')
ax.grid(True, alpha=0.3)
ax.legend(loc='best')

# Автоматически определяем границы
if unique_points:
    xs = [p[0] for p in unique_points]
    ys = [p[1] for p in unique_points]
    ax.set_xlim(0, max(xs) * 1.2 + 1)
    ax.set_ylim(0, max(ys) * 1.2 + 1)
else:
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)

plt.tight_layout()
plt.show()