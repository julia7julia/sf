per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
tkb = (per_cent['ТКБ'])
skb = (per_cent['СКБ'])
vtb = (per_cent['ВТБ'])
sber = (per_cent['СБЕР'])
money = int(input("сумма вклада: \n"))
dep_tkb = int((per_cent['ТКБ'])*money/100)
dep_skb = int((per_cent['СКБ'])*money/100)
dep_vtb = int((per_cent['ВТБ'])*money/100)
dep_sber = int((per_cent['СБЕР'])*money/100)
deposit = [dep_tkb, dep_skb, dep_vtb, dep_sber]
print('сумма процентов:', deposit)
max_dep = max(deposit)
print('Максимальная сумма, которую вы можете заработать -', max_dep)

