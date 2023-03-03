from nltk.corpus import wordnet

synonyms = []
antonyms = []


def synonym(userinput):
    for syn in wordnet.synsets(userinput):
        for l in syn.lemmas():
            synonyms.append(l.name()+'\n')

    return synonyms
    synonyms.clear()


def antonym(userinput):
    for syn in wordnet.synsets(userinput):
        for j in syn.lemmas():
            if j.antonyms():
                antonyms.append(j.antonyms()[0].name()+'\n')

    return antonyms
    antonyms.clear()


def definition(userinput):
    syns = wordnet.synsets(userinput)
    worddefin = []
#    worddefin = syns[0].definition()
    for i in syns:
        worddefin.append(i.definition()+'\n')
    return worddefin



