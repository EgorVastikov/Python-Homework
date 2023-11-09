from collections import defaultdict

def process_orders(order_count):
    orders = defaultdict(lambda: defaultdict(int))
    for _ in range(order_count):
        order_data = input("Заказ: ").split()
        customer, pizza, quantity = ' '.join(order_data[:-2]), order_data[-2], int(order_data[-1])
        orders[customer][pizza] += quantity
    return orders

def print_orders(orders):
    for customer in sorted(orders):
        print(f"{customer}:")
        for pizza, quantity in sorted(orders[customer].items()):
            print(f"{pizza}: {quantity}")


order_count = int(input("Введите количество заказов: "))
customer_orders = process_orders(order_count)
print_orders(customer_orders)