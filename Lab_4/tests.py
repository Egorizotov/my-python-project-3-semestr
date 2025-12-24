# tests.py
from main import AreaCalculating

def TestInputFigure():
    try:
        AreaCalculating(1, 1, 1, 1)
    except ValueError:
        pass  # Ожидалось, что будет вызвано исключение
    else:
        assert False, "Ожидалось ValueError"

def TestInputNumbers():
    assert AreaCalculating("rectangle", -1, 1, 1) == ValueError
    assert AreaCalculating("rectangle", -1, -1, 1) == ValueError
    assert AreaCalculating("square", 1, 1, -1) == ValueError

def TestResult():
    assert AreaCalculating("triangle", 3, 4, 5) == 6
    assert AreaCalculating("square", 3, 0, 0) == 9
    assert AreaCalculating("rectangle", 5, 12, 0) == 60

TestInputFigure()
TestInputNumbers()
TestResult()
