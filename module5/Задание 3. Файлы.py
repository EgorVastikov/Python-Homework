file_name = input("Название файла: ")

if file_name[0] in '@№$%^&*()':
    print("Название файла не должно начинаться с одного из специальных символов: @, №, $, %, ^, &, *, (.")
elif not (file_name.endswith('.txt') or file_name.endswith('.docx')):
    print("Файл должен заканчиваться расширением .txt или .docx.")
else:
    print("Файл назван верно.")