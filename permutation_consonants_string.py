def permutation(str):
    vowel="aeiouAEIOU"
    conso_count=0
    for char in str:
        if char not in vowel:
            conso_count+=1
    permut=1
    for i in range(1,conso_count+1):
        permut*=i
    return permut
print(permutation("dvca"))
        
            