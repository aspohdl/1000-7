import random
day = 1
satiety = 15
money = 30
hp = 30
progress = 40
while True:
    while True:
        if progress < 0 or satiety < 0 or money < 0 or hp < 0:
            break
        if progress >= 100 and money >= 100:
            print('Вы победили')
            break
        if progress >= 100:
            uspev=100
        if satiety >= 100:
            satiety = 100
        if hp >= 100:
            hp = 100
        if money >= 100:
            money = 100
        if day == 1 or day == 2 or day == 3:
            print(f'Здоровье: {hp} Деньги: {money} Успеваемость: {progress} Сытость: {satiety}')
            print(f'Сейчас день, выберите действие: '
                  f'\n1) Сходить на пары (Успеваемость: +5 Сытость: -10 Деньги: от 0 до 5 Здоровье: -5)'
                  f'\n2) Сходить на работу (Деньги: +15 Успеваемость: -5 Сытость: -15 Здоровье -5)'
                  f'\n3) Закрыть долги по учёбе (Успеваемость: от +10 до +30 Сытость: от -10 до -30 Здоровье: от 0 до -10)'
                  f'\n4) Перекусить (Сытость: +20)'
                  f'\n5) Пойти на пробежку (Здоровье +15)')
            action = int(input())
            if action == 1:
                satiety -= 10
                hp -= 5
                progress += 5
                print(f'Здоровье: {hp}\nДеньги: {money} \nУспеваемость: {progress} \nСытость: {satiety}')
                print('Идти на пары:\n1) Пешком\n2) Транспорт')
                lessons = int(input())
                if lessons == 1:
                    hp -= 5
                    satiety -= 15
                elif lessons == 2:
                    money -= 5
                else:
                    print('Вы нажали не ту кнопку')
                    break
            elif action == 2:
                money += 15
                progress -= 5
                satiety -= 15
                hp -= 5
            elif action == 3:
                print(f'Здоровье: {hp}\nДеньги: {money} \nУспеваемость: {progress} \nСытость: {satiety}')
                print('Какие предметы закрыть:\n'
                      '1) Лёгкие (Успеваемость: +10 Сытость: -10)'
                      '\n2) Сложные (Успеваемость: +20 Сытость: -20)'
                      '\n3) Самые трудные (Успеваемость: +30 Сытость: -30)')
                close = int(input())
                if close == 1:
                    progress += 10
                    satiety -= 10
                elif close == 2:
                    progress += 20
                    satiety -= 20
                    hp -= 5
                elif close == 3:
                    progress += 30
                    satiety -= 30
                    hp -= 10
                else:
                    print('Вы нажали не ту кнопку')
                    break
            elif action == 4:
                satiety += 20
            elif action == 5:
                hp += 15
            else:
                print('Вы нажали не ту кнопку')
                break
            day += 1
            if day == 4:
                day = 0
        elif day == 0:
            print(f'Здоровье: {hp}\nДеньги: {money} \nУспеваемость: {progress} \nСытость: {satiety}')
            print(f'Сейчас ночь, выберите действие: \n1) Спать (Здоровье: +10 Сытость: +5)'
                  f'\n2) Учить уроки (Успеваемость: +10 Здоровье: -5)')
            action = int(input())
            if action == 1:
                hp += 10
                satiety -= 5
            elif action == 2:
                progress += 10
                hp -= 5
            else:
                print('Вы нажали не ту кнопку')
                continue
            day += 1
        else:
            print('Вы нажали не ту кнопку')
            break

    if progress < 0 or satiety < 0 or money < 0 or hp < 0:
        print('Вы проиграли')
        break
    if progress >= 100 and money >= 100:
        break

    print('Вы хотите выйти из игры?\nДа/Нет')
    x = input()
    if x == 'Да':
        break
    else:
        continue
print('Игра окончена')