# А.С. Пушкин 2.0

born_year = int(input('Введите год рождения А.С. Пушкин '))
if born_year == 1799:
    born_day = int(input('Введите день рождения А.С. Пушкин '))
    day = ['26', '6']
    if (born_day == 26 or born_day == 6):
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')