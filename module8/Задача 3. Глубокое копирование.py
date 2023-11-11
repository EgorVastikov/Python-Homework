import copy

def create_site_for_product(base_site, product_name):
    # Глубокое копирование базового сайта
    new_site = copy.deepcopy(base_site)

    # Замена заголовка и текста в теле сайта
    new_site['html']['head']['title'] = f'Куплю/продам {product_name} недорого'
    new_site['html']['body']['h2'] = f'У нас самая низкая цена на {product_name}'

    return new_site

def main():
    base_site = {
        'html': {
            'head': {
                'title': 'Куплю/продам телефон недорого'
            },
            'body': {
                'h2': 'У нас самая низкая цена на iPhone',
                'div': 'Купить',
                'p': 'Продать'
            }
        }
    }

    num_sites = int(input("Введите количество сайтов: "))
    sites = []

    for i in range(num_sites):
        product_name = input(f"Введите название продукта для сайта {i + 1}: ")
        new_site = create_site_for_product(base_site, product_name)
        sites.append(new_site)
        print(f"Создан сайт для {product_name}:", new_site)

main()
