def word_shorting(sentence):
    words=[]
    word=''
    for i in range(len(sentence)):
        if sentence[i]!=" ":
            word+=sentence[i]
        
        else:
            if word!='':
                words.append(word)
                word=''
    if word!='':
        words.append(word)

    result=[]
    
    for word in words:
        if len(word)<10:
            result.append(word)
        else:
            result.append(word[0]+str(len(word)-2)+word[-1])
    result=" ".join(result)
    return result
    
print(word_shorting("demonstration is a good thing"))
    
            