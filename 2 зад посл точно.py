products = ["хлеб","масло","банан","мидоры","огурцы"]
komanda = input("У вас есть список что вы хотите с ним сделать ДОБАВИТЬ что-то, УДАЛИТЬ, показать элемент по номеру  ПОКАЗЭЛ , показать весь список ЧЕКНУТЬСПИС     ")
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
    elif komanda == "ПОКАЗЭЛ":
        