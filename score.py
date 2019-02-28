import itertools


def left_score(l, r):
    return len(l.tags) - middle_score(l, r)


def right_score(l, r):
    return len(r.tags) - middle_score(l, r)


def middle_score(l, r):
    return len(l.tags.intersection(r.tags))


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def score(slider):
    for l, r in pairwise(slider):
        ls = left_score(l, r)
        ms = middle_score(l, r)
        rs = right_score(l, r)

    return min(ls, ms, rs)


