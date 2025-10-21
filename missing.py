def missing(arr):
    n=len(arr)+1
    expected_sum=n*(n+1)//2
    actual_sum=sum(arr)
    miss=expected_sum-actual_sum
    return miss
print(missing([1,3,4,5]))
print(missing([1,2,3,4,5,6,7,8,9]))
print(missing([1,2,3,4,5,6,7,8,9]))
    