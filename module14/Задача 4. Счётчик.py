def count_calls(func):
    def wrapper(n):
        if not hasattr(wrapper, 'call_count'):
            wrapper.call_count = 0
        wrapper.call_count += 1
        return func(n)

    return wrapper

@count_calls
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(9))
print(fib.call_count)