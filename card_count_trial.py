def level(n):
    if n==0:
        return 0
    if n==1:
        return 2
    card=[0]*(n+1)
    card[1]=2
    for i in range(2,n+1):
        card[i]=((i*2)+(i-1)+(card[i-1]))%1000007
    return card[1:]


print(level(7))