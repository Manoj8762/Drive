def revers(arr):
    n=len(arr)
    for i in range(n//2-1):
        temp=arr[i]
        arr[i]=arr[n-i-1]
        arr[n-i-1]=temp
    return arr
print(revers([1,2,3,4,5,6,6,7,7,8]))
    
    