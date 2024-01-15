"""Word Finder: finds random words from a dictionary."""
""" >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """


import random

class WordFinder:
    def __int__(self, path):
        dict_file= open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        return[w.strip() for w in dict_file]
    
    def random(self):
        return random.choice(self.words)
    
class RandomWordFinder(WordFinder):
    def parse(self, dict_file):
        return[w.strip() for w in dict_file
               if w.strip() and not w.startswith("#")]
