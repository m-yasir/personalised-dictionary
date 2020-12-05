import spacy
    
def main():
    POSLIST = [
        'ADJ',
        'ADV',
        # 'SCONJ',
        'NOUN',
        'VERB'
    ]
    COMMON = [
        'are',
        'be',
        'have',
        'do'
    ]
    nlp = spacy.load("en_core_web_md")
    text = input('Enter text you want to search up against your dictionary: ')
    doc = nlp(text)
    dictionaryArr = []
    # Open file in append mode to avoid overwriting
    try:    
        with open('./dictionary.txt', mode='r+', encoding='UTF-8') as f:
            dictionaryArr = [line.strip() for line in f.readlines()]
    except:
        pass
    # Just save up unknowns
    unknowns = set()
    unknowns_disp = set()
    for tok in doc:
        if (not tok.is_stop and tok.pos_ in POSLIST and tok.lemma_ not in dictionaryArr):
            # Not worried about optimsing yet, using up two arrays
            unknowns_disp.add(tok.text)
            unknowns.add(tok.lemma_)

    # Show unknown words to the user
    if (len(unknowns)):
        print('Words that you are not familiar with:')
        for w in unknowns_disp: print(w)
    else:
        print('You are familiar with the words in the text! 🙂')

    # Update dictionary
    # Open file in append mode to avoid overwriting
    with open('./dictionary.txt', mode='a+', encoding='UTF-8') as f:
        f.writelines('\n'.join(unknowns))

if __name__ == "__main__":
    main()
    pass