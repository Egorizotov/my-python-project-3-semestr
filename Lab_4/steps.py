# steps.py
from behave import given, when, then
import sys
import os

# Добавляем путь к исходному коду
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import AreaCalculating

@given('тип фигуры "{shapetype}" и стороны {a}, {b}, {c}')
def step_given_triangle_sides(context, shapetype, a, b, c):
    context.shapetype = shapetype
    context.a = int(a)
    context.b = int(b)
    context.c = int(c)

@given('тип фигуры "{shapetype}" и сторона {a}')
def step_given_square_side(context, shapetype, a):
    context.shapetype = shapetype
    context.a = int(a)
    context.b = 0
    context.c = 0

@given('тип фигуры "{shapetype}" и стороны {a}, {b}')
def step_given_rectangle_sides(context, shapetype, a, b):
    context.shapetype = shapetype
    context.a = int(a)
    context.b = int(b)
    context.c = 0

@when('вычисляется площадь')
def step_when_calculate_area(context):
    try:
        context.result = AreaCalculating(context.shapetype, context.a, context.b, context.c)
        context.exception = None
    except Exception as error:
        context.result = None
        context.exception = error

@then('результат должен быть {expected_result}')
def step_then_check_result(context, expected_result):
    assert context.result == int(expected_result), f"Ожидалось: {expected_result}, Получено: {context.result}"

@then('должен вернуться ValueError')
def step_then_check_value_error(context):
    assert context.result == ValueError or context.exception is not None, "Ожидался ValueError, но функция завершилась успешно"
