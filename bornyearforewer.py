# А.С. Пушкин 3.0

born = int(input('Введите год рождения А.С. Пушкина '))
if born == 1799:
    print('Верно')
else:
    while born != '1799':
        born = input('Неверно! Введите год рождения А.С. Пушкина ')
    print('Наконец-то. Верно!')