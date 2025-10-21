def oper(s1,s2,op):
    l1=0
    l2=0
    for _ in s1:
        l1+=1
    for _ in s1:
        l2+=1
    if l1<l2:
        d=l2-l1
        s1=0*d+s1
    elif l2<l1:
        d=l1-l2
        s2=0*d+s2
    resu=""
    for i in range(len(s1)):
        if op=="AND":
            if s1[i]=="1" and s2[i]=="1":
                resu+="1"
            else:
                resu+="0"
        elif op=="OR":
            if (s1[i]=="1" or s2[i]=="0" )or( s2[i]=="0" or  s1[i]=="1") or( s2[i]=="1" or  s1[i]=="1"):
                resu+="1"
            else:
                resu+="0"
        elif op =="XOR":
            if (s1[i]=="1" or s2[i]=="0" )or( s2[i]=="0" or  s1[i]=="1"):
                resu+="1"
            else:
                resu+="0"
        else:
            resu="0"
    return resu
print(oper('1001','111','OR'))
                
            
            