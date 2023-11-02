def flag_func(shop, item):
    for detail, price in shop:
        if item == detail:
            return True
    return False


def price_detail(shop, item, counter):
    total_price = 0
    while counter != 0:
        for detail, price in shop:
            if item == detail:
                total_price += price
                counter -= 1
    return total_price


shop = [
    ['каретка', 1200],
    ['шатун', 1000],
    ['седло', 300],
    ['педаль', 100],
    ['седло', 1500],
    ['рама', 12000],
    ['обод', 2000],
    ['шатун', 200],
    ['седло', 2700],
]

while True:
    item = input("Введите деталь: ")
    if flag_func(shop, item):
        break
    else:
        print("Такой детали нет")

counter = int(input("Количество деталей: "))
print(f"Общая стоимость: {price_detail(shop, item, counter)}")