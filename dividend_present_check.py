def dividend_check(arr,d,q,r):
    indexes=[]
    for i in range(len(arr)):
        if arr[i]==d*q+r:
            indexes.append(i)
            
    if indexes:
        return indexes
    else:
        return -1
    
        

print(dividend_check([15,10,20,20,25,50],5,2,10))
            
    