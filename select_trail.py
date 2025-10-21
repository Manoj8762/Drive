def bubble(arr):
    n=len(arr)
    for i in range(n-1):
        #min_index=i
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            else:
                continue
           
            
                
            
    return arr
print(bubble([7,6,5,4,3,2,1]))