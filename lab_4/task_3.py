def delete(list_, index=-1):  # удаляется последний элемент по умолчанию, если индекс в вызове не указан
    if index < 0:
        index = len(list_) + index  # переопределение для отрицательного индекса
    f_delete = list_[:index] + list_[index + 1:]  # общий случай

    return f_delete


print(delete([0, 0, 1, 2], index=0))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]
