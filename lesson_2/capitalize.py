def titlize(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) > 2 or word.lower() == 'i':
            word = word.capitalize()
            new_words.append(word)
        else:
            new_words.append(word)
    
    return ' '.join(new_words)

title = 'hello world of programming i am sam'
print(titlize(title))