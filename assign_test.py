def assign_test(photos):
    slides = []
    for p in photos:
        slide = []
        slide.append(p)
        if p.orient:
            continue
        slides.append(slide)
    return slides


