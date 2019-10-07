# Викторина

victorin = 'да'
while victorin != 'нет':
    point = 0

    question_1 = int(input('Введите год рождения Л.Н Толстого ')) # Верный ответ 1828
    if question_1 == 1828:
        point += 1

    question_2 = int(input('Введите год рождения М.А. Булгакова '))  # Верный ответ 1891
    if question_2 == 1891:
        point += 1

    question_3 = int(input('Введите год рождения Ф.М. Достоевского '))  # Верный ответ 1821
    if question_3 == 1821:
        point += 1

    question_4 = int(input('Введите год рождения А.П. Чехова '))  # Верный ответ 1860
    if question_4 == 1860:
        point += 1

    question_5 = int(input('Введите год рождения И.С. Тургенева '))  # Верный ответ 1818
    if question_5 == 1860:
        point += 1

    percent = int(point * 100 / 5)
    print('Правильных ответов:', point, 'Допущено ошибок:', 5 - point)
    print("Процент правильных ответов:", percent, 'Процент ошибок:', 100 - percent)

    victorin = input('Повторить? да \ нет')

print('Спасибо за участие!')

