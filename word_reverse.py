def reverser(sentence):
    words=[]
    word=''
    for i in range(len(sentence)):
        if sentence[i]!=" ":
            word+=sentence[i]
        else:
            if word!="":
                words.append(word)
                word=''
    if word!="":
        words.append(word)
    reverse_str=''
    for i in range(len(words)-1,-1,-1):
        reverse_str+=words[i]
        if i!=0:
            reverse_str+=" "
    return reverse_str
print(reverser("this is a test"))
             