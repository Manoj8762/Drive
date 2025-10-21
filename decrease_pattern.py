def pyramid(n):

    for i in range(n,-1,-1):
        k=i-1
        for j in range(k,-1,-1):
            print("*",end="")
        k=i-2
        print()
    
pyramid(5)