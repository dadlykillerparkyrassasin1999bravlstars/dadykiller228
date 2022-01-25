n = int(input('Введите число до кторого все числа будут складываться   '))
sum = 0
for step in range(1,n+1):
    sum += step #либо можно писать sum += step+1
print("Сумма:",sum)