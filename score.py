import itertools


def left_score(c, n):
    return 0


def right_score(c, n):
    return 0


def middle_score(c, n):
    return 0


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def score(slides):
    for c, n in pairwise(slides):
        ls = left_score(c, n)
        ms = middle_score(c, n)
        rs = right_score(c, n)

    return min(ls, ms, rs)


