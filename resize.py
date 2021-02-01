#!/usr/bin/python3

# Crop and resize maps to show a standard view of the city

import subprocess

def run_convert(args):
    print(args)
    subprocess.run(['/usr/local/bin/convert'] + args)


# First knit together the 1993 map
run_convert([
    'originals/CA_San Francisco North_295005_1993_24000.jpg',
    '-gravity',
    'SouthWest',
    '-crop',
    '2710x3400+280+440',
    '+repage',
    '1993_right.jpg'
])
run_convert([
    'originals/CA_Point Bonita_294258_1993_24000.jpg',
    '-gravity',
    'SouthWest',
    '-crop',
    '2710x3400+273+438',
    '+repage',
    '1993_left.jpg',
])
run_convert([
    '1993_left.jpg',
    '1993_right.jpg',
    '+append',
    '1993_joined.jpg'
])
