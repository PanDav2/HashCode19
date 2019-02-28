import itertools


def tags(slide):
    if len(slide) == 1:
        return slide.tags
    p1, p2 = slide
    return p1.tags.union(p2.tags)


def left_score(l, r):
    return len(tags(l)) - middle_score(l, r)


def right_score(l, r):
    return len(tags(r)) - middle_score(l, r)


def middle_score(l, r):
    return len(tags(l).intersection(tags(r)))


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


