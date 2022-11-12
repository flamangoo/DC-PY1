from random import randint


def get_unique_list_numbers(start: int = -10, end: int = 10, length: int = 15) -> list[int]:
    if start > end:
        raise ValueError('Левая граница не может быть больше правой')
        # start, end = end, start
    if length > end - start:
        raise ValueError('Длина списка не может быть больше количества случайных целых чисел')
    list_ = []
    while len(list_) < length:  # список заполняется до заданного размера
        random_value = randint(start, end)
        if random_value not in list_:
            list_.append(random_value)  # добавляем значение в список, если оно уникальное

    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))  # True
