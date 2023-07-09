menuList = []
priceList = []

def showBill():
    print("----Myfood----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])

def totalBill():
    print(sum(priceList))


while True:
    menuName = input("Please Enter Menu")
    if(menuName.lower() == "exit"):
        break
    MenuPrice = int(input("Price :"))
    menuList.append(menuName)
    priceList.append(MenuPrice)
print(menuList, priceList)
showBill()
totalBill()