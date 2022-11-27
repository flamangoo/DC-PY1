INPUT_FILE = 'input.csv'
OUTPUT_FILE = 'output.json'

indent = 4 * ' '


def csv_to_list_dict(input_file, new_line='\n', delimiter=',') -> list[dict]:
    with open(input_file, 'r', encoding='utf-8') as file:
        header = file.readline().replace(new_line, '').split(delimiter)
        for line in file:
            line = line.replace(new_line, '')
            yield dict(zip(header, line.split(delimiter)))


# save dict as json record
def converter_csv_to_json(input_file, output_file, new_line='\n', delimiter=','):
    with open(output_file, 'w', encoding='utf-8') as serial:
        serial.write('[' + new_line)
        is_first_row = True  # flag

        for record in csv_to_list_dict(input_file):
            if not is_first_row:
                serial.write(delimiter + new_line)
            serial.write(indent + '{' + new_line)
            is_first_row = True

            for key, value in record.items():
                if not is_first_row:
                    serial.write(delimiter + new_line)
                serial.write(f'{indent}{indent}"{key}": {value}')
                is_first_row = False

            serial.write(new_line + indent + '}')
            is_first_row = False

        serial.write(new_line + ']')
