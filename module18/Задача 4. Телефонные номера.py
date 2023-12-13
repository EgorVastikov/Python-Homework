phone_numbers = ['9999999999', '999999-999', '99999x9999']

def check_phone_numbers(phone_numbers):
    for index, number in enumerate(phone_numbers, start=1):
        if len(number) == 10 and number[0] in ['8', '9'] and number.isdigit():
            print(f'{index}-й номер: всё в порядке')
        else:
            print(f'{index}-й номер: не подходит')


check_phone_numbers(phone_numbers)