#!/usr/bin/env python3

import sys
import colorsys
import pywal as wal


def main(argv):
    n = int(argv[0])
    colors = wal.colors.get(argv[1])["colors"]
    ncolors = min(len(colors.keys()), n)
    for color in [colors[f"color{i}"] for i in range(ncolors)]:
        print(color)
    # for color in sorted([colors[f'color{i}'] for i in range(ncolors)], key=get_hsv)[::-1]:
    #     print(color)


def get_hsv(rgb):
    """
    Transforms RGB color -> HSV color
    """
    rgb = rgb.lstrip("#")  # in case you have Web color specs
    r, g, b = (int(rgb[i : i + 2], 16) / 255 for i in range(0, 5, 2))
    return colorsys.rgb_to_hsv(r, g, b)


if __name__ == "__main__":
    main(sys.argv[1:])
