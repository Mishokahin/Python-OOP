class countdown_iterator:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        while self.start > -1:
            i = self.start
            self.start -= 1
            return i

        raise StopIteration()


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")