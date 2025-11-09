def check_leaf(y):
    if y%4==0:
        print("yes its a leap year")
        if y%100==0:
            print("yes its a leap year")
            if y%400==0:
                print("Its a leap year")
            else:
                print("its not a leap  year")
        else:
            print("its a leap year")
            
    
    else:
        return f"its not a leap year"
print(check_leaf(1600))