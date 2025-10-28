def count_words(sentence):
    word=""
    words=[]
    val=0
    for c in sentence:
        if c!=" ":
            word+=c
        else:
            if word!="":
                val+=1
                words.append(word)
                word=""
    if word!="":
        words.append(word)
    return val, len(words)
print(count_words("ommonly used in English to indicate the favorable points"))
            
                
            