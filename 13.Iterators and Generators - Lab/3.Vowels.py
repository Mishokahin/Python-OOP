class vowels:
    def __init__(self, word):
        self.word = word
        self.ALL_VOWELS = ["a", "e", "i", "o", "u", "y"]
        self.IDX = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.IDX < len(self.word)-1:
            self.IDX += 1
            if self.word[self.IDX].lower() in self.ALL_VOWELS:
                return self.word[self.IDX]

        raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)