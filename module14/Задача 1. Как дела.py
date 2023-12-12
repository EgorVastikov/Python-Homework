import functools

def how_are_you(func):
    @functools.wraps(func)
    def wrapper():
        response = input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        return func()
    return wrapper

@how_are_you
def test():
    print("<Тут что-то происходит...>")


test()