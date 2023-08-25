class dictionary_iter:
    def __init__(self, items):
        self.items = list(items.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.items):
            item = self.items[self.idx]
            self.idx += 1
            return item

        raise StopIteration()

result = dictionary_iter({"name": "Peter",
"age": 24})
for x in result:
    print(x)