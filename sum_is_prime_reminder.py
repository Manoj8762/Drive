def is_prime(total):
    if total>1:
        for i in range(2,int(total**0.5)+1):
            if total%i==0:
                return False
        else:
            return True
    
    
num=152
total=0
if num>=1:
    while num>=1:
        total+=num%10
        num=num//10
else:
    False
print(f"{total} and {is_prime(total)}")
        