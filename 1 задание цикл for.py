n = int(input('Введите количество чисел   '))
sum = 0
for step in range(n):
    number = int(input("Введите число"))
    sum += number
print("Сумма:",sum)