def non_repeat(s):
    uni={}
    for i in range(len(s)):
        if s[i] in uni:
            uni[s[i]]+=1
        else:
            uni[s[i]]=1
    for j in uni:
        if uni[j]==1:
            return j
        else:
            continue
print(non_repeat("aaaabccawwafaa"))
            
        