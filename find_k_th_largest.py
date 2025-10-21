def kth(arr,k):
    for i in range(k):
        max_num=float('-inf')
        max_index=-1
        for j in range(len(arr)):
            if arr[j]> max_num:
                max_num=arr[j]
                max_index=j
        arr.pop(max_index)
    return max_num
print(kth([1, 3, 4, 2, 5, 6], 2))