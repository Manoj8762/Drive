def sums(num):
    total=0
    for i in range(1,num+1):
        if num%i==0:
            total+=i
        else:
            continue
    return total
print(sums(78))
            