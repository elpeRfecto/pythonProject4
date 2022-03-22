#pt = price tickets
tickets = input("Сколько билетов хотите приобрести?: ")
age_visitors = int(input("Введите Ваш возраст: "))
for i in tickets:
    if int(i) > 3:
        pt1 = (990 * int(i)) - (990 * int(i) * 0.1)
        pt2 = (1390 * int(i)) - (1390 * int(i) * 0.1)
    elif int(i) == 2:
        pt1 = 990 * int(i)
        pt2 = 1390 * int(i)
    elif int(i) == 3:
        pt1 = 990 * int(i)
        pt2 = 1390 * int(i)
    else:
        pt1 = 990
        pt2 = 1390
if age_visitors < 18:
    print("Вход бесплатный")
elif age_visitors in range(18, 25):
    if int(i) > 3:
        print("Сумма к оплате с учетом скидки", pt1, "руб")
    else:
        print("Полная стоимость", pt1, "руб")
else:
    age_visitors >= 25
    if int(i) > 3:
        print("Сумма к оплате с учетом скидки", pt2, "руб")
    else:
        print("Полная стоимость", pt2, "руб")