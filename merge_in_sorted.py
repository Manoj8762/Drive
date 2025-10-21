def mer(ar1,ar2):
    i=j=0
    final=[]
    while len(ar1)>i and len(ar2)>j:
        if ar1[i]<ar2[j]:
            final.append(ar1[i])
            i+=1
        else:
            final.append(ar2[j])
            j+=1
    final.extend(ar1[i:])
    final.extend(ar2[j:])
    return final
print(mer([1, 3, 3, 5, 6], [2, 3, 4, 5, 5, 7]))
            