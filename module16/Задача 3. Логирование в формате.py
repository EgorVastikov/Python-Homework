import time
import functools
from datetime import datetime

def log_methods(time_format):
    def class_decorator(cls):
        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value) and not attr_name.startswith("__"):
                setattr(cls, attr_name, log_method(attr_value, time_format))
        return cls

    def log_method(method, time_format):
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            formatted_time = datetime.now().strftime(time_format)
            print(f"Запускается '{method.__qualname__}'. Дата и время запуска: {formatted_time}.")
            result = method(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Завершение '{method.__qualname__}', время работы = {elapsed_time:.3f} s.")
            return result
        return wrapper

    return class_decorator


@log_methods("%b %d %Y — %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result

@log_methods("%b %d %Y - %H:%M:%S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()