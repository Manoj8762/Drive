def count_unique(string,uni):
    uniq=set()
    counting=0
    for i in string:
        if i not in uniq:
            counting+=1
            uniq.add(i)
        else:
            continue
    return counting,uni
print(count_unique("ababcc",3))
            