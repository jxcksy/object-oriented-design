def read_dictionary(filename):

    global valid_words
    valid_words = set()
    
    for word in open(filename):
        word = word.strip()
        valid_words.add(word)