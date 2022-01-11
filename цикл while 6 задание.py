pokypka = int(input("Введите сумму на котрую вы закупились"))
bonus = pokypka / 10
while bonus <= 1000:
    pokypka = int(input("Введите сумму на которую вы закупились"))
    bonus = bonus + pokypka / 10
print("Бонусы накопились можно тратить")