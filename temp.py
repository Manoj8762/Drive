def reverse_sentence(sent):
    words = []
    word = ""
    for i in range(len(sent)):
        if sent[i] != " ":
            word += sent[i]
        else:
            if word != "":
                words.append(word)
                word = ""  # ✅ reset here, not +=
    if word != "":
        words.append(word)

    reverse_string = ""
    for i in range(len(words) - 1, -1, -1):
        reverse_string += words[i]
        if i != 0:
            reverse_string += " "
    return reverse_string

print(reverse_sentence("this is a test"))
