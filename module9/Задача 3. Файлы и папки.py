import os

def get_directory_size_and_count(path):
    total_size = 0
    total_files = 0
    total_dirs = 0

    for root, dirs, files in os.walk(path):
        total_files += len(files)
        total_dirs += len(dirs)
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)

    return total_dirs, total_files, total_size

path_to_directory = input("Введите путь к каталогу: ")
total_dirs, total_files, total_size = get_directory_size_and_count(path_to_directory)

print(f"Всего подкаталогов: {total_dirs}")
print(f"Всего файлов: {total_files}")
print(f"Общий размер каталога: {total_size / 1024} Килобайт")