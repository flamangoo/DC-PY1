salary = 5000  # зарплата, const
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев

while months != 0:
    need_money += spend - salary
    spend = spend + spend * increase
    months -= 1

print(round(need_money))
