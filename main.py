
from reader import read_input, generate_output
from score import totalscore


def assign_test(photos):
    slides = []
    tslide = []
    for p in photos:
        slide = []
        if p.orient:
            tslide.append(p)
            if len(tslide) == 2:
                slide = tslide
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
    photos = read_input(f"./data/{file}")
    slides = assign_test(photos)
    generate_output(slides, f"./out/{file}.out")
    print(file, totalscore(slides))
