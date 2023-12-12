import time

def delay(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Ждём {seconds} секунд перед выполнением функции {func.__name__}...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay(5)
def my_function():
    print("Тут что-то происходит")


my_function()