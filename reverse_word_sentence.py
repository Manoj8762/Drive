def reverse_word_sentence(sentence):
    words=[]
    word=""
    for i in range(len(sentence)):
        if sentence[i]!=" ":
            word+=sentence[i]
        else:
            if word!="":
                words.append(word)
                word=""
    if word!="":
        words.append(word)
    reverse_string=""
    for i in range(len(words)-1,-1,-1):
        reverse_string+=words[i]
        
        if i!=0:
            reverse_string+=" "
    return reverse_string
print(reverse_word_sentence("this is a test"))
        