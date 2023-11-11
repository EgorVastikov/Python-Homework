def flexible_sum(*args):
    def sum_nested(item):
        if isinstance(item, list):
            return sum(sum_nested(sub_item) for sub_item in item)
        else:
            return item

    return sum(sum_nested(arg) for arg in args)


print(flexible_sum(1, 2, 3, 4, 5))