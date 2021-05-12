#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Tran Khanh"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
from logzero import logger

import cv2
import json
import numpy as np
from average import averagePixels
from set_wall import apply_wallpaper
from findFace import find_any_face


def main(args):
    """ Main entry point of the app """
    logger.info("hello world")
    logger.info(args)

    try:
    pix = averagePixels( find_any_face() )
    fb , fg , fr = pix.split(',')

    with open('Wallpapers_lookup.json') as f:
        Wallpapers_lookup = {} or json.load(f)
    
    THRESHOLD = 64

    for val in Wallpapers_lookup:
        ib, ig , ir = Wallpapers_lookup[ val ].split(',')
        dif = abs( int( fb ) - int( ib ) ) + abs( int( fg ) - int( ig ) ) + abs ( int( fr ) - int( ir ) )

        if dif < THRESHOLD:
            # print( val )
            apply_wallpaper( f'Wallpapers/{val}' )
            break
    else:
        val = random.choice( list ( Wallpapers_lookup ) )
        # print( val )
        apply_wallpaper( f'Wallpapers/{val}' )
        print("No match found hence a random wallpaper is being applied")
        
    except Exception as e:
        print(e)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)