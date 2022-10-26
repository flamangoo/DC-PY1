def delete(list_, index=None):
    if index is None:
        index = len(list_)
    if index == len(list_):
        f_delete = list_[:index - 1]
    else:
        f_delete = list_[:index] + list_[index + 1:]

    return f_delete


print(delete([0, 0, 1, 2], index=0))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]
