class reverse_iter:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.items) > 0:
            return self.items.pop()

        raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)