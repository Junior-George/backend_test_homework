from math import sqrt

message = (
    "Добро пожаловать в самую лучшую программу для вычисления "
    " квадратного корня из заданного числа"
)


def Calculate_Square_Root(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        return
    print(
        f"Мы вычислили корень квадратный из введенного вами числа. "
        f"Это будет: {Calculate_Square_Root(your_number)}"
    )


print(message)
calc(25.5)
