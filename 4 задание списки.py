products = ["хлеб","масло","банан","мидоры","огурцы"]
komanda = input("У вас есть список что вы хотите с ним сделать ДОБАВИТЬ что-то, УДАЛИТЬ, показать элемент по номеру  ПОКАЗАТЬ , показать весь список ПОКАЗАТЬПОНОМЕРУ    , ПЕРЕЗАПИСАТЬ команда редактор  ,РЕДАКТИРОВАТЬ")
while komanda != "exit":
    if komanda == "ДОБАВИТЬ":
        prok = input("Введите продукт котрый вы хотите внести в список           ")
        products.append(prok)
        for prod in products:
            print(prod)
    elif komanda == "УДАЛИТЬ":
        ydalit = input("Вот список напишите название которое вы хотите удалить      ")
        products.remove(ydalit)
        for prod in products:
            print(prod)
    elif komanda == "ПОКАЗАТЬ":
        pokazat = input("Сейчас я покажу вам список продуктов")
        for prod in products:
            print(prod)
    elif komanda == "ПОКАЗАТЬПОНОМЕРУ":
        number = int(input("Какой номер вы хотите посмотреть"))
        print(products[number - 1])
    elif komanda == "ПЕРЕЗАПИСАТЬ":
        perezapis = int(input("Какой номер вы хотете презаписать на другой овощ или так далее"))
        OPTAC = input("На какую еду вы хотите поменять?")
        products[perezapis - 1] = OPTAC
    elif komanda == "РЕДАКТИРОВАТЬ":
        print("")
        for prod in products:
            print(prod)
        redaktor = input("Напиги продукт который ты хочешь редактирвать ")
        OPTA = input("На какую еду вы хотите поменять?")
        nova = products.index(redaktor)
        products[nova] = OPTA
    komanda = input("У вас есть список что вы хотите с ним сделать ДОБАВИТЬ что-то, УДАЛИТЬ, показать элемент по номеру  ПОКАЗАТЬ , показать весь список ПОКАЗАТЬПОНОМЕРУ    , ПЕРЕЗАПИСАТЬ команда редактор ")
