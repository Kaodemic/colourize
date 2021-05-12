import cv2
import json
import numpy as np
from average import averagePixels
from set_wall import apply_wallpaper
from findFace import find_any_face

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