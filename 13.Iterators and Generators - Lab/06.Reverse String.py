def reverse_text(word):
    idx = len(word) -1
    while idx > -1:
        yield word[idx]
        idx -= 1

for char in reverse_text("step"):
    print(char, end='')