def get_count_char(str_):  # функция принимает строку
    str_ = str_.lower()
    default_count = 0
    char_dictionary = {}
    for char in str_:
        if char.isalpha():
            char_dictionary[char] = char_dictionary.get(char, default_count) + 1

    return char_dictionary


def get_percents(char_dictionary):  # функция принимает словарь символов
    sum_of_values = sum(char_dictionary.values())
    dictionary_with_percents = {}
    for char in char_dictionary:
        dictionary_with_percents[char] = round(char_dictionary[char] / sum_of_values * 100, 2)
    #  print(sum(dictionary_with_percents.values()))

    return dictionary_with_percents


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
counts_char = get_count_char(main_str)
print(get_percents(counts_char))
