robonumber = int(input('Отгадай число которе я загадал'))
while robonumber != 99:
    robonumber = int(input('Это не то число введите дргое'))
    if robonumber > 99:
        print('Число больше задуманного')
    elif robonumber < 99:
        print('Число меньше задуманного')
    elif robonumber == 99:
        print('Молодец ты ввел правильное число')
