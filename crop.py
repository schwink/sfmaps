#!/usr/bin/python3

# Crop out a matching area from each of the resized maps

import argparse
import subprocess
import os

def run_magick(args):
    print(args)
    subprocess.run(['magick'] + args)

def crop(path_in, path_out, left, top, width, height, caption=None):
    # The images being selected from have dimensions 1920x1920
    # left, top: Coordinates (from the top left corner) of the top left corner of the crop in pixels
    # width, height: Dimensions of the crop in pixels

    args = [
        'convert',
        path_in,
        '-gravity',
        'NorthWest',
        '+repage',
        '-crop',
        '{}x{}!+{}+{}'.format(width, height, left, top),
        '+repage',
    ]

    if caption:
        args += [
            '-pointsize',
            '16',
            '-undercolor',
            'white',
            '-fill',
            'black',
            '-annotate',
            '+4+4',
            caption,
        ]
        
    args += [
        path_out
    ]
    run_magick(args)


IMAGES = {
    '1895': 'CA_San Francisco_298889_1895_62500.jpg',
    '1899': 'CA_San Francisco_298890_1899_62500.jpg',
    '1915': 'CA_San Francisco_298896_1915_62500.jpg',
    '1947': 'CA_San Francisco North_300059_1947_24000.jpg',
    '1950': 'CA_San Francisco North_300060_1950_24000.jpg',
    '1956': 'CA_San Francisco North_363065_1956_24000.jpg',
    '1993': 'CA_San Francisco North_295005_1993_24000.jpg',
}


def main():
    parser = argparse.ArgumentParser(
        prog='select',
        description='Crop sets of map images')
    parser.add_argument('left', type=int)
    parser.add_argument('top', type=int)
    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)
    parser.add_argument('output_dir', type=str)

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    for (year, image) in IMAGES.items():
        input_path = image
        output_path = '{}/{}.jpg'.format(args.output_dir, year)
        crop(
            input_path,
            output_path,
            args.left,
            args.top,
            args.width,
            args.height,
            caption=year
        )


if __name__ == '__main__':
    main()
