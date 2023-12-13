from typing import Callable

def decorator_with_args_for_any_decorator(decorator):
    def wrapper(*d_args, **d_kwargs):
        def decorator_wrapper(func):
            def func_wrapper(*f_args, **f_kwargs):
                return decorator(func, *d_args, **d_kwargs)(*f_args, **f_kwargs)
            return func_wrapper
        return decorator_wrapper
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    def wrapper(*f_args, **f_kwargs):
        print("Переданные арги и кварги в декоратор:", args, kwargs)
        return func(*f_args, **f_kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)