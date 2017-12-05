from collections import Counter

def checkPassphrases(filename):
    '''Takes in a file with a 'passphrase' on each line.  Passphrases are good
        only if every word in the phrase is unique within the phrase.  Returns
        the number of valid passphrases'''
    with open(filename, 'r') as f:
        phrases = f.readlines()
    valid_phrases = 0
    for phrase in phrases:
        words = phrase.split()
        unq_words = set(words)
        valid_phrases += (len(words) == len(unq_words))
    return valid_phrases

def checkAnagramPassphrases(filename):
    ''' Takes in a file with a 'passphrase' on each line.  Passphrases are good
        only if every word in the phrase is not an anagram of any other word in
        the phrase.  Returns the number of valid passphrases'''
    with open(filename, 'r') as f:
        phrases = f.readlines()
    valid_phrases = 0
    for phrase in phrases:
        # We could essentially create a set of counters if we promise not to
        # mutate them, but this is a premature optimization given the scale of
        # the input
        bags = []
        words = phrase.split()
        fGood = True
       for word in words:
            bag = Counter(word)
            if bag in bags:
                fGood = False
                break
            else:
                bags.append(bag)
        if fGood:
            valid_phrases += 1
    return valid_phrases
print(checkAnagramPassphrases('input.txt'))

