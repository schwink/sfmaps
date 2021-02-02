#!/usr/bin/python3

# Crop and resize maps to show a standard view of the city

import subprocess

def run_magick(args):
    print(args)
    subprocess.run(['/usr/local/bin/magick'] + args)

def crop(path_in, path_out, bottom, left, right, rotate=0):
    # bottom: pixels bottom edge to 37 degrees 45 minutes north
    # left: pixels left edge to 122 degrees 30 seconds west
    # right: pixels right edge to 122 degrees 22 minutes 30 seconds west

    width = int(subprocess.run(
        args=[
            'identify',
            '-format',
            '%w',
            path_in
        ],
        capture_output=True,
        encoding='utf-8'
    ).stdout)

    # We not have a reference point west of 122 degrees 30 seconds
    # But we want to crop two minutes farther west
    pixels_per_minute_latitude = (width - left - right) / 22
    crop_x = left - (3 * pixels_per_minute_latitude)
    crop_width = pixels_per_minute_latitude * 25

    args = [
        'convert',
        path_in,
        '-gravity',
        'SouthWest',
    ]

    if rotate != 0:
        args = args + ['-rotate', '{}'.format(rotate)]

    args = args + [
        '-crop',
        '{}x{}+{}+{}'.format(crop_width, crop_width, crop_x, bottom),
        '+repage',
        '-resize',
        '{}x{}'.format(1920, 1920),
        path_out
    ]
    run_magick(args)

# First knit together the 1993 map
run_magick([
    'convert',
    'originals/CA_San Francisco North_295005_1993_24000.jpg',
    '-gravity',
    'SouthWest',
    '-crop',
    '2710x3400+280+440',
    '+repage',
    '1993_right.jpg'
])
run_magick([
    'convert',
    'originals/CA_Point Bonita_294258_1993_24000.jpg',
    '-gravity',
    'SouthWest',
    '-crop',
    '2710x3400+273+438',
    '+repage',
    '1993_left.jpg',
])
run_magick([
    'convert',
    '1993_left.jpg',
    '1993_right.jpg',
    '+append',
    '1993_joined.jpg'
])

# Crop and resize everything
crop(
    'originals/CA_San Francisco North_300059_1947_24000.jpg',
    'CA_San Francisco North_300059_1947_24000.jpg',
    bottom=657,
    left=510,
    right=224
)
crop(
    'originals/CA_San Francisco North_300060_1950_24000.jpg',
    'CA_San Francisco North_300060_1950_24000.jpg',
    bottom=422,
    left=468,
    right=188
)
crop(
    'originals/CA_San Francisco North_363065_1956_24000.jpg',
    'CA_San Francisco North_363065_1956_24000.jpg',
    bottom=418,
    left=495,
    right=229
)
crop(
    '1993_joined.jpg',
    'CA_San Francisco North_295005_1993_24000.jpg',
    bottom=0,
    left=2710,
    right=0
)

crop(
    'originals/CA_San Francisco_298889_1895_62500.jpg',
    'CA_San Francisco_298889_1895_62500.jpg',
    bottom=195,
    left=216,
    right=1276
)
crop(
    'originals/CA_San Francisco_298890_1899_62500.jpg',
    'CA_San Francisco_298890_1899_62500.jpg',
    bottom=206,
    left=243,
    right=1280,
    rotate=-0.15
)
crop(
    'originals/CA_San Francisco_298896_1915_62500.jpg',
    'CA_San Francisco_298896_1915_62500.jpg',
    bottom=182,
    left=308,
    right=1232
)
