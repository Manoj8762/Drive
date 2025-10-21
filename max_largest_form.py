def largest(arr):
    digit=[]
    for n in arr:
        temp=[]
        if n==0:
            temp=[0]
        else:
            while n>0:
                temp=[n%10]+temp
                n=n//10
        digit=digit+temp
    print(digit)
    for k in range(len(digit)):
        for m in range(k+1,len(digit)):
            if str(digit[k])+str(digit[m])<str(digit[m])+str(digit[k]):
                digit[k],digit[m]=digit[m],digit[k]
    res="".join([str(d) for d in digit])
    return res
                
print(largest([10, 100, 999, 454, 45, 63, 69]))
