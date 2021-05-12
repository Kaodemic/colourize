import ctypes
import os
import platform

def apply_wallpaper(fn):
    if platform.system() == "Windows":
        return ctypes.windll.user32.SystemParametersInfoW( 20 , 0 , os.path.abspath( fn ) , 0 )
    if platform.system() == "Linux":
        try:
            return os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+os.path.abspath( fn ))
        except:
            return os.system("gconftool-2 --type=string --set /desktop/gnome/background/picture_filename "+os.path.abspath( fn ))
