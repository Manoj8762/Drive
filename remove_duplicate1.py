def dup(arr):
    uni=set()
    final=[]
    for i in arr:
        if i not in uni:
            uni.add(i)
            final.append(i)
        else:
            continue
    return final
print(dup([1,1,2,1,1,12,1,45,45,78,7,8]))