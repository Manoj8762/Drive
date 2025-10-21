def prime_index(arr):
    prime_list=[]
    prime_index_number_sum=0
    
    for num in range(2,len(arr)):
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
            
            
        if is_prime:
            prime_list.append(num)
                
    print(prime_list)
    for i in prime_list:
        prime_index_number_sum+=arr[i]
    return prime_index_number_sum

print(prime_index([10,20,30,40,50,60,70,80,90]))