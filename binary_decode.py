alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits=[]

def decode(str):
    digit=0
    for char in str:
        if char !="0":
            digit+=1
        else:
            if digit!=0:
                digits.append(digit)
                digit=0
    if digit!=0:
        digits.append(digit)
    print(digits)
    decodes=""
    for d in digits:
        if 1<=d<=26:
            decodes+=alpha[d-1]
        else:
            decodes+="?"
    return decodes

print(decode("11101011110"))