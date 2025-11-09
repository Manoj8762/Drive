def substr(s1):
    li=[]
    for i in range(len(s1)):
        for j in range(i+1,len(s1)+1):
            print(s1[i:j],end=" ")
    
print(substr("bfw"))
            
