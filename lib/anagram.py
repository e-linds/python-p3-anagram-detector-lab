class Anagram:
    def __init__ (self, word):
        self.word = word
    
    def match(self, option1, option2="", option3=""):
        selected_words = []
       
        def sortletters(input):
            letters = []
            for letter in input:
                letters.append(letter)
                letters.sort()
            return letters
        
        self_word_sorted = sortletters(self.word)

        def find_anagram(input):
            if input:
                sortletters(input)
                if sortletters(input) == self_word_sorted:
                    selected_words.append(input)
        

        find_anagram(option1)
        find_anagram(option2)
        find_anagram(option3)

        return selected_words
    




