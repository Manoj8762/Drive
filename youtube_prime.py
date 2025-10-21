
def check_prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        
        return True

num=[10,20,30,40,50,60,70,80,90]
sum=0
for i in range(2,len(num)):
    if check_prime(i):
        sum+=num[i]
print(sum)
