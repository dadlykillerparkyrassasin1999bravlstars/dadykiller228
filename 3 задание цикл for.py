n = int(input('Введите число до кторого все числа будут перемножаться   '))
sum = 1
for step in range(1,n+1):
    sum = step*sum
print("Сумма:",sum)