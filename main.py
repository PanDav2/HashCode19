
from reader import read_input, generate_output
from score import totalscore


def vh(file):
    photos = read_input(f"./data/{file}")
    v = [p for p in photos if p.orient]
    h  = [p for p in photos if not p.orient]
    return v, h



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

files = [
    'a_example.txt',
    'b_lovely_landscapes.txt',
    'c_memorable_moments.txt',
    'd_pet_pictures.txt',
    'e_shiny_selfies.txt'
]

for file in files:
    v, h = vh(file)
    vs = [(i, k) for i, k in zip(v[0::2], v[1::2])]
    vs.extend([[hs] for hs in h])
    print(vs)
    generate_output(vs, f"./out/{file}.out")
