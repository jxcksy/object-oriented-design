import read_dictionary

class Word():
 
    def __init__(self, word): # String
        self.word = word # String
        self.score = getScore(word) # int
 
    def getWord(self):
        return self.word # String
 
    def getScore(self):
        return self.score # int
 
    def validateWord(self, word):
        return word in read_dictionary.valid_words:
 
    def getDictionary(self):
        return self.dictionary # dict
