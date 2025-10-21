def bubble(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>=arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        else:
            continue
    return arr
print(bubble([4,5,7,7,9,1,2]))
            