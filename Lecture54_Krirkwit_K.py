def loginUsername():
    username = input("enter username")
    if username == "Krirkwit":
        return loginPassword()
    else:
        return loginUsername()
def loginPassword():
    password = input("enter password")
    if password == "1234":
        print("login complete")
        return(showMenu())
    else:
        return loginPassword()
def showMenu():
    print("ishop")
    print("1. Vat calculator")
    print("2. price calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return(vatCalculator(total_price = float(input("enter price"))))
    elif userSelected ==2:
        return(priceCalculator())
    else:
        print("error")
    return userSelected
def vatCalculator(total_price):
    vat = 7
    result = total_price + (total_price * vat / 100)
    return result
def priceCalculator():
    price1 = float(input("enter price 1"))
    price2 = float(input("enter price 2"))
    return vatCalculator(price1 + price2)

print(loginUsername())
