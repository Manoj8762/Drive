
def k_th_largest(arr,k):
    ar1=arr.copy()
    for i in range(k):
      
        max_val=float('-inf')
        max_index=-1
        for j in range(len(ar1)):
            if ar1[j]> max_val:
                max_val=ar1[j]
                max_index=j
        ar1.pop(max_index)
    print(max_val)
    count=0
    for l in arr:
        
        if l==int(max_val):
            count+=1
        else:
            continue
        
    return f" k_th_max value {max_val} and count is { count}"
print(k_th_largest([1,2,3,4,5,6,7,8,8,8,9],2))