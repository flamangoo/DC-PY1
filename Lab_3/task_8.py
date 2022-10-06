money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
all_money = money_capital + salary

while True:
    if all_money <= 0:
        break
    all_money -= spend
    month += 1
    salary += salary
    spend = spend + increase * spend

print(month)
