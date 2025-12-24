# main.py
import math

def AreaCalculating(shapetype, a, b, c):
    if isinstance(shapetype, str) and a > 0 and b >= 0 and c >= 0:
        if shapetype == "rectangle":
            return a * b
        elif shapetype == "square":
            return a * a
        elif shapetype == "triangle":
            if a + b > c and a + c > b and b + c > a:  # Проверка на треугольное неравенство
                per = (a + b + c) / 2
                return int(math.sqrt((per * (per - a) * (per - b) * (per - c))))
            else:
                return ValueError("Invalid sides for a triangle")
        else:
            return ValueError("Invalid shape type")
    else:
        return ValueError("Invalid input values")

# Пример использования
print(AreaCalculating("triangle", 3, 4, 5))  # Должно вернуть 6
print(AreaCalculating("square", 3, 0, 0))    # Должно вернуть 9
print(AreaCalculating("rectangle", 5, 12, 0)) # Должно вернуть 60
