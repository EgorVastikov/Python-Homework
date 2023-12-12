import os

def count_lines_in_python_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            path = os.path.join(directory, filename)
            with open(path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                non_blank_count = 0
                for line in lines:
                    stripped_line = line.strip()
                    if stripped_line and not stripped_line.startswith('#'):
                        non_blank_count += 1
                yield filename, non_blank_count


directory_path = 'путь_к_директории'
for file_name, count in count_lines_in_python_files(directory_path):
    print(f"{file_name}: {count} строк")