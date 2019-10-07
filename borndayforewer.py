# А.С. Пушкин 4.0

while True:
    born_year = int(input('Введите год рождения А.С. Пушкин '))
    if born_year == 1799:
        while True:
            born_day = int(input('Введите день рождения А.С. Пушкин '))
            day = ['26', '6']
            if (born_day == 26 or born_day == 6):
                print('Верно')
                break
            else:
                print('Неверный день рождения')
        break
    else:
        print('Неверный год рождения')