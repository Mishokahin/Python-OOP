from typing import List


class BaseStack:
    def __init__(self):
        self.data: List[str] = []

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        return f'[{", ".join(reversed(self.data))}]'


class AddToStack(BaseStack):
    def push(self, element: str):
        self.data.append(element)


class RemoveFromStack(BaseStack):
    def pop(self):
        return self.data.pop()


class TopOfTheStack(BaseStack):
    def top(self):
        return self.data[-1]


class Stack(AddToStack, RemoveFromStack, TopOfTheStack):
    pass
