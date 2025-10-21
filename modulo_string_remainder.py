def remainder(str):
    num=int(str)
    
    for n in range(0,10):
        if num%11==n:
            return n
        else:
            continue

print(remainder("1345"))