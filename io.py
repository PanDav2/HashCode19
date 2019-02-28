#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def read_input(iname):
    photos = []
    with open(iname, "r") as fin:
        N = int(fin.readline())
        for i, l in enumerate(fin.readlines()):
            tokens = l.strip().split(' ')
            is_vertical = (tokens[0] == 'V')
            tags = set(tokens[2:])
            photos.append(Photos(id, is_vertical, tags))

    assert N == len(photos)
    return photos


def generate_output(slides, oname):
    with open(oname, "w") as fout:
        fout.write(f"{len(slides)}\n")

        for slide in slides:
            if len(slide) == 1:
                fout.write(f"{slide[0].id}\n")
            elif len(slide) == 2:
                fout.write(f"{slide[0].id} {slide[1].id}\n")
            else:
                assert ValueError("A slide can have at most 2 photos")