def string_char_replace(str,c1,c2):
    reverse=""
    for ch in str:
        if ch==c1:
            reverse+=c2
        elif ch==c2:
            reverse+=c1
        else:
            reverse+=ch
    return reverse
print(string_char_replace("apple","a","p"))