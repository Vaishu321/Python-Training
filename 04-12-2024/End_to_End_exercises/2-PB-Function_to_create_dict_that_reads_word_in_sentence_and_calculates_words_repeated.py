sent=input("Enter a sentence: ")

def no_of_words_in_sentence(sentence):
    d = {}
    sentence = sentence.split()
    for i in sentence:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    print(d)

no_of_words_in_sentence(sent)