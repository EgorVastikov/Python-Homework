import json

diff_list = ['services', 'staff', 'datetime']

def compare_jsons(old_data, new_data, keys):
    result = {}
    for key in keys:
        if old_data['data'][key] != new_data['data'][key]:
            result[key] = new_data['data'][key]
    return result

with open('json_old.json', 'r', encoding='utf-8') as file:
    json_old = json.load(file)

with open('json_new.json', 'r', encoding='utf-8') as file:
    json_new = json.load(file)

result = compare_jsons(json_old, json_new, diff_list)

print(result)

with open("result.json", "w", encoding='utf-8') as file:
    json.dump(result, file, indent=4)

with open("result.json", "r", encoding='utf-8') as file:
    loaded_data = json.load(file)
    print(loaded_data)