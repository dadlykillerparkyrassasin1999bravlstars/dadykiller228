n = int(input('Введите число до которого все четные числа будут складываться'))
number = 0
for step in range(0 , n):
    if step % 2 == 0:
        number = step+number
        print(number)