spisok = ['Поесть','по работать','поиграть','сходить в магазин']
for l in spisok:
    print(l)
vybor = input('Это список и вы можете Добавить Удалить Показать по номеру Весь список Редактировать Редактировать по названию')
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
    elif vybor == 'Редактировать':
        redaktirovat = int(input('Введите номер который вам нужен-'))#products[0] = “авокадо”
        bubra = redaktirovat - 1
        zamena = input('На какой продукт вы хотите заменить')
        spisok[bubra] = zamena
        print(spisok[bubra])#print(products[0])
    elif vybor == 'Редактировать по названию':
        zamenit = input("Введи слово которое ты хочешь заменить")
        if zamenit in spisok:
            zamenite = input('На что заменить это в списке?')
            number = spisok.index(zamenit)
            spisok[number] = zamenite
            print(spisok[number])
    vybor = input('Это список и вы можете Добавить Удалить Показать по номеру Весь список ')


    