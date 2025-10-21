def maxi(arr):
    max_num=float('-inf')
    for i in arr:
        if max_num<i:
            max_num=i
        else:
            pass
    return max_num
print(maxi([1,2,3,4,5,6,6,7,8,9,5,4,2]))