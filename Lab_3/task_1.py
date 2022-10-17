src = not False and True or False and not True

# result = True or False --> избавляемся от отрицаний
# result = True --> избавляемся от логического "ИЛИ"

result = True

print(src == result)
