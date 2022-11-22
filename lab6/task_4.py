import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename, 'r', encoding='utf-8') as file:
        form = []
        for line in file:
            line = line.replace(new_line, '')  # убираем символ переноса строки
            form.append(line.split(delimiter))  # формируем список по разделителю
    for i in range(len(form)):
        form[i] = dict(zip(form[0], form[i]))  # объединение элементов

    return form


print(json.dumps(csv_to_list_dict(INPUT_FILE)[1:], indent=4, ensure_ascii=False))
