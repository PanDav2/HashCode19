
from reader import read_input, generate_output
from score import totalscore

def assign_test(photos):
    slides = []
    for p in photos:
        slide = []
        slide.append(p)
        if p.orient:
            continue
        slides.append(tuple(slide))
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
