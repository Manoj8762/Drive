def reverser(arrr):
    n=len(arrr)
    for i in range(n//2-1):
        temp=arrr[i]
        arrr[i]=arrr[n-i-1]
        arrr[n-i-1]=temp
    return arrr
print(reverser([1,2,3,4,5,6,7,8,9]))
    