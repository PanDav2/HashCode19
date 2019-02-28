
from reader import read_input, generate_output

def assign_test(photos):
    slides = []
    for p in photos:
        slide = []
        slide.append(p)
        if p.orient:
            continue
        slides.append(slide)
    return slides

files = [
    'a_example.txt',
    'b_lovely_landscapes.txt',
    'c_memorable_moments.txt',
    'd_pet_pictures.txt',
    'e_shiny_selfies.txt'
]

file = 'a_example.txt'
photos = read_input('./data/' + file)
slides = assign_test(photos)
generate_output(slides, './out/' + file + '.out')

print(slides)
