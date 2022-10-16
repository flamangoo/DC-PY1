money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05  # также можно положить increase = 1.05, чтобы записать spend *= increase
month = 0  # количество месяцев, которое можно прожить

while money_capital >= spend:
    money_capital -= spend  # или money_capital -= spend - salary без 9 строки
    money_capital += salary
    spend = spend + spend * increase
    month += 1

print(month)
