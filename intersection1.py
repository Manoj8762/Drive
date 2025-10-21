def inter(a1,a2):
    i=j=0
    inter1=[]
    while len(a1)>i and len(a2)>j:
        if a1[i]<a2[j]:
            i+=1
        elif a1[i]>a2[j]:
            j+=1
        else:
            inter1.append(a1[i])
            i+=1
            j+=1
    return inter1
print(inter([1,9,4,5,6,7,8,],[9,4,5,6,7,7,8]))
            
            
            