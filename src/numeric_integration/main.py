import numpy as np
import matplotlib.pyplot as plt
from numeric_integration.utils import format
from math import cos, pi


def rectangle(f, a: int, b: int, n: int) -> float:
    dx = (b-a)/n
    xs = [a + dx*i for i in range(0, n)]

    res: float = 0

    for x in xs:
        res += f(x)*dx #type: ignore

    return res


def trapezoid(f, a: int, b: int, n: int) -> float:
    dx = (b-a)/n
    xs = [a + dx*i for i in range(0, n)]

    res: float = 0

    for x in xs:
        res += 0.5 * (f(x)+f(x+dx))*dx


    return res


def simpson(f, a: int, b: int, n: int) -> float:
    dx = (b-a)/n
    xs = [a + dx*i for i in range(0, n)]

    res: float = 0

    for x in xs:
        res += (f(x)+4*f(x+dx*0.5)+f(x+dx))*dx/6


    return res


a = 0
b = 1
fnc = (lambda x: np.e**x**2)

N_POINTS = 9
ns = [2**i for i in range(0, N_POINTS)]
def calculate_error_for_f_on_func(f, func, a, b):
    errors = []
    for i in range(0, N_POINTS):
        errors.append(abs(f(func, a, b, 2**i) - f(func, a, b, 2**(i+1))))

    return errors

y_rect = calculate_error_for_f_on_func(rectangle, fnc, a, b)
y_trap = calculate_error_for_f_on_func(trapezoid, fnc, a, b)
y_simpson = calculate_error_for_f_on_func(simpson, fnc, a, b)


fig, ax = plt.subplots()
format(fig, ax)

ax.loglog(ns, y_rect, c='b', label='Прямоугольник')
ax.loglog(ns, y_trap, c='r', label='Трапеция')
ax.loglog(ns, y_simpson, c='g', label='Площадь под параболой (Симпсон)')

ax.set_xlabel('Число разбиений n', color='#ffffff')
ax.set_ylabel('Оценка ошибки |I(n) − I(2n)|', color='#ffffff')
ax.legend(facecolor='#111117', edgecolor='#ffffff', labelcolor='#ffffff')

plt.show()
