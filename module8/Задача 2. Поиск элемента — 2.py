def find_key(dictionary, key, depth=None, current_depth=0):
    if depth is not None and current_depth > depth:
        return None

    if key in dictionary:
        return dictionary[key]

    for k, v in dictionary.items():
        if isinstance(v, dict):
            found = find_key(v, key, depth, current_depth + 1)
            if found is not None:
                return found

    return None

# Пример словаря
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

test_key = "head"
print(f"Поиск ключа '{test_key}' без ограничения глубины:", find_key(site, test_key))

test_key = "head"
print(f"Поиск ключа '{test_key}' с ограничением глубины 0:", find_key(site, test_key, depth=0))
