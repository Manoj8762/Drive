def maxi(arr):
    max_num=arr[0]
    for i in range(len(arr)-1):
        if arr[i+1]>max_num:
            max_num=arr[i+1]
        else:
            continue
    return max_num
print(maxi([4,5,7,7,9,1,2]))