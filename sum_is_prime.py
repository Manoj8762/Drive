def number(a):
    string=str(a)
    sum=0
    for i in string:
        sum+=int(i)
        
    if sum<=1:
        return False
    else:
        for i in range(2,int(sum**0.5)+1):
            if sum%i==0:
                return False
        else:
            return True
print(number(123))
            
        