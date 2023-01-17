quantity = int(input('количество билетов:'))
a = 0
b = 0
c = 0
for i in range(quantity):
    age = int(input('введите возраст:'))
    if 0 <= age < 18:
       a = a+1
    elif 18 <= age < 25:
       b = b+1
    elif 25 <= age < 100:
       c = c+1
    else:
        print('Возраст указан неверно!')
price1 = 0
price2 = 990
price3 = 1390
cost1 = price1*a
cost2 = price2*b
cost3 = price3*c
total_cost = cost1+cost2+cost3
if quantity >= 3:
    print('Сумма к оплате:', total_cost*0.9)
else:
    print('Сумма к оплате:', total_cost)
    
