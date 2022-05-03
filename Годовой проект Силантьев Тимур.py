List = ['поспать']
for elem in List:
    print(elem)
action = input("введите добавить, удалить, показать, редактировать или показать элемент по номеру ")
while(action != "пока"):
    if action == "добавить":
        List.append(input('Введите действие в список '))
        for elem in List:
            print(elem)
    elif action == 'удалить':
        n = int(input('введите номер элемента которое хотите удалить '))
        n = n - 1 
        del List[n]
        for elem in List:
            print(elem)
    elif action == 'показать элемент по номеру':
        n = int(input('введите номер элемента '))
        n = n - 1 
        print(List[n])
    elif action == 'показать':
        for elem in List:
            print(elem)
    elif action == 'редактировать':
        n = input('введите имя элемента который хотите редактировать ')
        if n in List:
            n = int(List.index(n))
            List[n] = input("Введите по новому элемент списка ")
            for elem in List:
                print(elem)
        else:
            n = input('заново введите имя элемента который хотите редактировать ')
    action = input("введите добавить, удалить, показать, редактировать или показать элемент по номеру ")
print('пока')