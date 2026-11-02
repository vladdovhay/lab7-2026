import math

# Читання координат та відстані до (0,0)
try:
    with open("coordinates.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    points = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x, y = line.split(",")
        points.append((float(x), float(y)))

    print("Відстані до початку координат:")
    for x, y in points:
        print(f"({x}, {y}) -> {math.hypot(x, y):.2f}")
except FileNotFoundError:
    print("Файл coordinates.txt не знайдено!")
    exit()
except ValueError:
    print("У файлі некоректні дані!")
    exit()
except IOError:
    print("Помилка читання файлу coordinates.txt")
    exit()

# Точки в радіусі -> points_in_radius.txt
try:
    radius = float(input("Введіть радіус: "))
    with open("points_in_radius.txt", "w", encoding="utf-8") as out:
        for x, y in points:
            if math.hypot(x, y) <= radius:
                out.write(f"{x},{y}\n")
    print("Точки в межах радіуса записано у файл points_in_radius.txt")
except ValueError:
    print("Радіус має бути числом!")
except IOError:
    print("Помилка запису у файл points_in_radius.txt")

# 6-7. Найближча точка до (1,1) у файлі користувача
filename = input("Введіть ім'я файлу: ")

try:
    with open(filename, "r", encoding="utf-8") as user_file:
        user_lines = user_file.readlines()

    nearest = None
    min_dist = None
    for line in user_lines:
        line = line.strip()
        if not line:
            continue
        x, y = line.split(",")
        x, y = float(x), float(y)
        dist = math.hypot(x - 1, y - 1)
        if min_dist is None or dist < min_dist:
            min_dist = dist
            nearest = (x, y)

    if nearest is None:
        print("Файл порожній!")
    else:
        print(f"Найближча точка до (1,1): ({nearest[0]}, {nearest[1]})")
except FileNotFoundError:
    print(f"Файл {filename} не знайдено!")
except ValueError:
    print("У файлі некоректні дані!")
except IOError:
    print(f"Помилка читання файлу {filename}")