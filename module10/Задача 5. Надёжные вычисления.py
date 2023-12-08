import math

def calculate_square_root(number):
    try:
        if number < 0:
            raise ValueError("Невозможно вычислить квадратный корень от отрицательного числа")

        return math.sqrt(number)

    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"Произошла ошибка: {e}"

result = calculate_square_root(-4)
print(result)
result = calculate_square_root(16)
print(result)
result = calculate_square_root("abc")
print(result)