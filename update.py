import cv2
import json
from glob import glob
import numpy as np
from average import averagePixels

list_of_files = glob( "Wallpapers/*.*" )

with open('Wallpapers_lookup.json') as f:
    Wallpapers_lookup = {} or json.load(f)

for file in list_of_files:
    
    fn = file.replace( "Wallpapers\\",'' )

    if not fn in Wallpapers_lookup:
        wallpaper = cv2.imread( file, -1 )
        Wallpapers_lookup[ fn ] =  averagePixels( wallpaper )
    
with open('Wallpapers_lookup.json','w') as f:
    json.dump(Wallpapers_lookup, f)