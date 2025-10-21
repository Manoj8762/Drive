def prim_check(start,end):
    prime_list=[]
    for num in range(2,end+1):
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            prime_list.append(num)
    return prime_list,sum(prime_list)
print(prim_check(2,45))