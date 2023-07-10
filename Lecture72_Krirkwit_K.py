menuList = []

def showBill():
    print("----Myfood----")
    for number in range(len(menuList)):
        print(menuList[number])


def totalBill():
    total_price = 0
    for number in range(len(menuList)):
        total_price += int(menuList[number][1])
    print(total_price)

while True:
    menuName = input("Please Enter Menu")
    if(menuName.lower() == "exit"):
        break
    MenuPrice = input("Price :")
    menuList.append([menuName,MenuPrice])
print(menuList)

showBill()
totalBill()