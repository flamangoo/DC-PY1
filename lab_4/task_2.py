def get_count_char(str_):  # функция принимает строку
    str_ = str_.lower()
    char_dictionary = {}
    for char in str_:
        if char.isalpha():
            char_dictionary[char] = char_dictionary.get(char, 0) + 1

    return char_dictionary


def get_percents(char_dictionary):  # функция принимает словарь символов
    sum_of_values = sum(char_dictionary.values())
    percents = {}
    for char in char_dictionary:
        percents[char] = char_dictionary[char] / sum_of_values * 100
        error = 100 - sum(percents.values())  # нахождение отклонения от 100%
    percents.update({'err': error})  # добавим ошибку как дополнительный ключ
    # print(sum(percents.values()))
    # print(error)

    return percents


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
counts_char = get_count_char(main_str)
print(get_percents(counts_char))
