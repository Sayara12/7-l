def merge(*iters):
    for it in iters:
        yield from it
list(merge(a, b, c))
