def frequency(str):
    freq={}
    str=list(str)
    str.sort()
    for char in str:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    result=""
    for ch in freq:
        result+=f"{ch}{freq[ch]}"
    return result
print(frequency("aavsqgvhgsc"))