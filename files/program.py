balance = 50000
pin = int(input("enter pin:"))


if pin ==1234:
    print("1, check balance")
    print("2, withdraw mony")

    choice = int(input("enter choice"))
    if choice ==1:
        print ("balance",balance)

    elif choice ==2:
        amount = int(input("enter amount"))

        if amount <=balance:
            balance = balance - amount
            print ("withdrawal successful")
            print ("reamining balance:,balance")

        else:
            print("insufficent balance")
    else:
        print("invalid choice")
        

        

    
                