row=5
for i  in range(row):
    for j in range(row-i-1):
        print(" "  ,end="")
    for j in range(2*i+1):
        print("*", end='')
    print()
#row=5
#for i in range(row):
 #   print(" " *(row-i-1)+"*"*(2*i+1))