class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_count < self.count:
            i = 0 + (self.current_count * self.step)
            self.current_count += 1
            return i

        raise StopIteration()


numbers = take_skip(10, 5)
for number in numbers:
    print(number)