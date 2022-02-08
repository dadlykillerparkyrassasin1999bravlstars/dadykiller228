print("Вася пошел гулять но по пути на него наала гопата. Помоги Васе либо гопота отожмет у него все деньги")
vybor = input("BEWAT , BIT , KRICHAT")
while vybor != "BEWAT" and vybor != "BIT" and vybor !="KRICHAT":
    vybor = input("BEWAT , BIT , KRICHAT")
if vybor == "BEWAT":
    print("Вася бежит а за ним бегут гопники и их надо обдурить")
    vybor = input("CPRIT , BEWAT")
    while vybor != "CPRIT" and vybor != "BEWAT":
        vybor = input("CPRIT , BEWAT")
    if vybor == "CPRIT":
        print("Вася сумел уйти от погони гопников")
    elif vybor == "BEWAT":
        print("Вася выдохля его догнали и отжали деньги")
if vybor == "BIT":
        print("Вася решил драться")
        print("Вася нашел в кармане HOK и PISTOL")
    vybor = input("HOK" , "PISTOL")
    while vybor != "HOK" and vybor != "PISTOL":
        vybor = input("HOK" , "PISTOL")
    if vybor == "HOK":
        print("Вася достал нож но во время драки")
        print("Но нож у Васи забрали и пырнули его")
    elif vybor == "PISTOL":
        print("Пистолет у Васи оказался бракованным и поэтому гопники очень легок побили Васю и украли деньги")