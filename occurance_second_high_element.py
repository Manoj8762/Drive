def second_largest(arr):
    first=second=float('-inf')
    for i in range(len(arr)):
        if arr[i]>first:
            second=first
            first=arr[i]
        elif arr[i]>second and arr[i]<first:
            second=arr[i]
    count=0
    for num in arr:
        if num==second:
            count+=1
    return f"second largest elment {second} and count is:  {count}"
    
print(second_largest([1,2,3,4,5,6,7,7,8,8]))