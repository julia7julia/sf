quantity = int(input('количество билетов:'))
if quantity != 0:
    for i in range(quantity):
        age = int(input('введите возраст:'))
        a=0
        b=0
        c=0
        if 0 <= age < 18:
            a = a+1
            print(a)
        elif 18 <= age < 25:
            b=b+1
            print(b)
            cost2 = price2 * b
        elif 25 <= age < 100:
            c=c+1
            print(c)
            cost3 = price3 * c
price1=0
price2=990
price3=1390
cost1 = price1*a
cost2=price2*b
print(cost2)
cost3=price3*c
print(cost3)
total_cost=cost1+cost2+cost3
print(total_cost)

