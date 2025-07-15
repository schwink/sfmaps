# Page through over 100 years of San Francisco history

Public domain topo maps from the USGS

https://www.usgs.gov/core-science-systems/ngp/topo-maps/historical-topographic-map-collection

## How to use

To regenerate the image files, you'll need imagemagick

https://imagemagick.org

`brew install imagemagick`

To pull overlapping areas from the source maps, try this:
(Coordinates are in pixels, within the 1920x1920 aligned images.)

```
# Crop from position 1630,1420 an image of dimension 270x400
./crop.py 1630 1420 270 400 mission_rock/
```

You can append cropped images horizontally with e.g.
```
magick 1899.jpg 1947.jpg 1993.jpg +smush +8  mission_rock.jpg
```
