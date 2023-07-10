system_Menu = {"ข้าวมันไก่": 45, "ข้าวหมูทอด": 40, "ข้าวขาหมู": 35, "ข้าวมันไก่ทอด": 50}
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
    menuList.append([menuName,system_Menu[menuName]])
print(menuList)
showBill()
totalBill()