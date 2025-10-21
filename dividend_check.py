def dividend_index(arr,d,q,r):
    dividend=d*q+r
    if dividend in arr:
        return arr.index(dividend)
    else:
        return -1
print(dividend_index([15,10,20,30,25,50], 5, 2, 5))