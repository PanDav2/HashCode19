import itertools


def tags(slide):
    if len(slide) == 1:
        return slide.tags
    p1, p2 = slide
    return p1.tags.union(p2.tags)

def score(transition):
    p1, p2 = transition
    p1tags, p2tags = tags(p1), tags(p2)
    intersection = p1tags.intersection(p2tags)
    sleft = len(p1tags - intersection)
    sright = len(p2tags- intersection)
    return min(sleft, sright, len(intersection))

def totalscore(slides):
    return sum(score(t) for t in zip(slides, slides[1:]))