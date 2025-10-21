def largest(arr):
    str_num=[str(num) for num in arr]
    for i in range(len(str_num)):
        for j in range(i+1,len(str_num)):
            if str_num[i]+str_num[j]<str_num[j]+str_num[i]:
                str_num[i],str_num[j]=str_num[j],str_num[i]
    result="".join(str_num)
    if result[0]=="0":
        return 0, [0]
    
    return result
largest= largest([8, 60, 546, 548, 1000, 9999])
print(f"{largest}  ")
    
    