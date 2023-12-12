def find_errors_in_log_files(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for line in file:
                if 'ERROR' in line:
                    output_file.write(line)


input_log_file = 'file.log'
output_file = 'error_file.log'

find_errors_in_log_files(input_log_file, output_file)