username = input("enter username")
Password = input("enter password")
Username = input("enter username")
if Username == username:
    password = input("enter password")
    if password == Password:
        print("login complete")
        print("welcome to Orangina shop")
        print("menu")
        print("1. Latte", 20, "THB")
        print("2. Americano", 15, "THB")
        print("3. Capuccino", 25, "THB")
        print("4. Ice Latte", 25, "THB")
        print("5. Ice Americano", 20, "THB")
        print("6. Ice Cappuccino", 30, "THB")
        print("7. Orangina add shot", 35, "THB")
        Order = int(input("plese select your order"))
        if Order == 1:
            print("Latte selected")
            Amount = int(input("how many drinks do you want?"))
            print("Latte", Amount , "has been ordered")
            price = 20 * Amount
            print(price, "THB")
        elif Order == 2:
            print("Americano selected")
            Amount = int(input("how many drinks do you want?"))
            print("Americano", Amount, "has been ordered")
            price = 15 * Amount
            print(price)
        elif Order == 3:
            print("Capuccino selected")
            Amount = int(input("how many drinks do you want?"))
            print("Capuccino", Amount, "has been ordered")
            price = 25 * Amount
            print(price, "THB")
        elif Order == 4:
            print("Ice Latte selected")
            Amount = int(input("how many drinks do you want?"))
            print("Ice Latte", Amount, "has been ordered")
            price = 25 * Amount
            print(price, "THB")
        elif Order == 5:
            print("Ice Americano selected")
            Amount = int(input("how many drinks do you want?"))
            print("Ice Americano", Amount, "has been ordered")
            price = 20 * Amount
            print(price, "THB")
        elif Order == 6:
            print("Ice Capuccino selected")
            Amount = int(input("how many drinks do you want?"))
            print("Ice Capuccino", Amount, "has been ordered")
            price = 30 * Amount
            print(price, "THB")
        elif Order == 7:
            print("Orangina add shot selected")
            Amount = int(input("how many drinks do you want?"))
            print("Orangina add shot selected", Amount, "has been ordered")
            price = 35 * Amount
            print(price, "THB")
        else:
            print("error")
    else:
        print("password wrong")
else:
    print("username wrong")


