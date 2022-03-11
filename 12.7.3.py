money = int(input("Введите сумму, которую хотите положить:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for deposit in per_cent.values():
    result = int(money / 100 * per_cent)
    deposit.append(result)
print(deposit)
print("Максимальная сумма, которая накопится за год", "-", max(deposit))

