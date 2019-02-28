
from reader import read_input, generate_output
from score import totalscore, score
import numpy as np
import random

import time


def vh(file):
    photos = read_input(f"./data/{file}")
    v = [p for p in photos if p.orient]
    h  = [p for p in photos if not p.orient]
    return v, h

def reorder(slides):
    s = slides.pop()
    ns = [s]
    while len(slides) > 0:
        scores = [score((s, s2)) for s2 in slides[:50]]
#         print(scores)
        index  = scores.index(max(scores))
        s = slides.pop(index)
        ns.append(s)
    return ns

def assign_test(photos):
    slides = []
    tslide = []
    for p in photos:
        slide = []
        if p.orient:
            tslide.append(p)
            if len(tslide) == 2:
                slides.append(tuple(tslide))
                tslide = []
        else :
            slide.append(p)
            slides.append(slide)
    return slides


def assign_beam_search(photos):
    # Random sampling of N slides
    N = 5000
    verticals = np.array([p.orient for p in photos]).nonzero()[0]
    selected = np.unique(np.random.randint(0, len(photos), size=N))

    vertices = [
        (photos[sel],)
        for sel in selected
        if not photos[sel].orient  # horizontal
    ]

    incomplete_slides = [
        photos[sel]
        for sel in selected
        if not photos[sel].orient
    ]

    # Compute NxN scores
    dists = np.zeros((selected.shape[0], selected.shape[0]), dtype=int)
    for i in range(len(vertices)):
        for j in range(i, len(vertices)):
            dists[i, j] = score((vertices[i], vertices[j]))

    # Use graph
    # Start with highest score
    pos = np.argmax(dists)
    src = int(pos / dists.shape[0] )
    slides = [vertices[src]]
    while True:
        dst = np.argmax(dists[src])
        dists[:, src] = 0  # Make sure src is never reused
        if dists[src, dst] == 0:
            pos = np.argmax(dists)
            src, dst = int(pos / dists.shape[0]), pos % dists.shape[0]  # random unused
            if dists[src, dst] == 0:
                break
        src = dst
        slides.append(vertices[src])
    return slides


def assign_metropolis_hastings(slides):
    budget = 50000 #len(slides) # generations
    swaps = np.random.randint(1, len(slides) -1, size=(budget, 2))

    best = [s for s in slides]
    currscore = totalscore(slides)
    for swapid in range(budget):
        i, j = swaps[swapid]
        slides[i], slides[j] = slides[j], slides[i]
        newscore = (currscore
            + score((slides[i-1], slides[j]))
            + score((slides[j], slides[i+1]))
            + score((slides[j-1], slides[i]))
            + score((slides[i], slides[j+1]))
            - score((slides[i-1], slides[i]))
            - score((slides[i], slides[i+1]))
            - score((slides[j-1], slides[j]))
            - score((slides[j], slides[j+1])))

        if newscore > currscore:
            best = [s for s in slides]
        if float(newscore / (1e-8 + currscore)) < random.random():
            # revert
            slides[i], slides[j] = slides[j], slides[i]
        else:
            currscore = newscore

    return best


def assign_metropolis_hastings_2(slides):
    budget = 5000 #len(slides) # generations

    best = [s for s in slides]
    currscores = [score(t) for t in zip(slides, slides[1:])]
    tscore = sum(currscores)
    for _ in range(budget):
        cut = min(range(len(currscores)), key=lambda x: currscores[x])
        new_transition_score = score((slides[-1], slides[0]))
        newscore = tscore + new_transition_score - currscores[cut]

        if newscore > tscore:
            best = [s for s in slides]
        if float(newscore / (1e-8 + tscore)) > random.random():
            currscores = currscores[cut:-2] + [new_transition_score] + currscores[:cut]
            slides = slides[cut:] + slides[:cut]
            tscore = newscore
    return best



files = [
    'a_example.txt',
    'b_lovely_landscapes.txt',
    'c_memorable_moments.txt',
    'd_pet_pictures.txt',
    'e_shiny_selfies.txt'
]

for file in files:
    v, h = vh(file)
    vs = [(i, k) for i,k in zip(v[0::2], v[1::2])]
    vs.extend([(hs,) for hs in h])
    reorder_start = time.time()
    vs = reorder(vs)
    print("Reorder - done ", time.time() - reorder_start)
    mh_start = time.time()
    slides = assign_metropolis_hastings_2(vs)
    print("Metropolis - done ", time.time() - mh_start)
    print(len(slides))
    print(file, totalscore(slides))
    generate_output(slides, f"./out/{file}.out")
