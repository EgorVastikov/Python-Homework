import datetime
import traceback

def logging(func):
    def wrapper(*args, **kwargs):
        try:
            print(f"Вызывается функция: {func.__name__}")
            print(f"Документация: {func.__doc__}")
            return func(*args, **kwargs)
        except Exception as e:
            with open('function_errors.log', 'a', encoding='utf-8') as error_log:
                error_log.write(f"{datetime.datetime.now()} - Ошибка в функции {func.__name__}: {e}\n")
                error_log.write(traceback.format_exc() + "\n")
            print(f"Ошибка в функции {func.__name__} записаны в 'func_errors.log'")

    return wrapper



@logging
def test_function(x, y):
    return x + y


@logging
def another_function():
    """Эта функция вызывает ошибку."""
    raise ValueError("Пример ошибки")



test_function(2, 3)
another_function()