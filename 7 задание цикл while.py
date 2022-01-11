comanda = input("Введите команду")
while comanda != "exit":
    if comanda == "+":
        number = int(input("Введите первое слагаемое"))
        numberr = int(input("Введите второе число"))
        print(number + numberr)
    elif comanda == "-":
        num = int(input("Введите уменьшаемое"))
        numm = int(input("Введите вычитаемое"))
        print(num - numm)
    elif comanda == "*":
        n = int(input("Введите первый множитель"))
        nn = int(input("Введите второй множитель"))
        print(n * nn)
    elif comanda == "/":
        m = int(input("Введите делимое"))
        mm = int(input("Введите делитель"))
        print(m / mm)         
    comanda = input("Введите команду")
    