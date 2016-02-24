#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

class setWallpaper:


    #image title
    image_title = ''
    image_src = ''
    
    def __init__(self, image_title, image_src):
        self.image_title = image_title
        self.image_src = image_src
    
    def download(self, save_dir):
        ''' download the image from site using system wget
        This is easiest solution but wont work on windows !!FIX!!'''    
        try:
            wget = 'wget -O ~/' + save_dir + '/' + self.image_title + ' '+self.image_src
            os.system(wget)
            return 1
        except:
            sys.exit("Problem with wget")
            

    def set_wallpaper(self, full_save_dir):
        ''' Now set the wallpaper, so far only working on gnome desktop
        add support for kde etc'''    
        try:
            img = 'file://' + full_save_dir + self.image_title  
            cmd = 'gsettings set org.gnome.desktop.background picture-uri ' + img
            os.system(cmd)
            return 1
        except:
            sys.exit("Can't change wallpaper settings")    
