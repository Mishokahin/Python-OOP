def genrange(start, end):
    i = start
    n = end
    while i <= n:
        yield i
        i += 1