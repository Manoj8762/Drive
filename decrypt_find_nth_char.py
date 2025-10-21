def decrypt(string,k):
    num="123456789"
    numbers=[]
    alpha=[]
    dec=''
    for char in string:
        if char in num:
            numbers.append(int(char))
        else:
            alpha.append(char)
    
    print(numbers)
    print(alpha)
    for i in range(0,len(alpha)):
        dec+=alpha[i]*numbers[i]
    
    if 0 <= k < len(dec):
            key = dec[k]
    else:
        key = -1  # or return -1
              
    return dec, key
                    

print(decrypt("A1C3D4" ,9))