spisok = ['Поесть','по работать','поиграть','сходить в магазин']
for l in spisok:
    print(l)
vybor = input('Это список и вы можете Добавить Удалить Показать по номеру Весь список ')
while vybor != 'exit':
    if vybor == 'Добавить':
        delo = input('Введи дело которое хочешь сделать ')
        spisok.append(delo)
        for l in spisok:
            print(l)
    elif vybor == 'Удалить':
        delet = input('Какое дело хочешь удалить?')
        spisok.remove(delet)
        for l in spisok:
            print(l)
    elif vybor == 'Показать по номеру':
        pokazat = int(input('Введите номер который вам нужен'))
        print(spisok[pokazat - 1])
    elif vybor == 'Весь список':
        for l in spisok:
            print(l)
    vybor = input('Это список и вы можете Добавить Удалить Показать по номеру Весь список ')