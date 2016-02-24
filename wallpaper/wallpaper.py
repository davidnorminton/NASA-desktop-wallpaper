#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author David Norminton
# <davidnorminton@gmail.com>
# last updated : 24 - 02 -16
# This has a, "do whatever you want with it license", so run wild.
import nasa
import set_wallpaper
import sys


#url to find list of images
list_url = 'http://apod.nasa.gov/apod/archivepix.html'
# image position on NASAs list
image_number = 0
#Directory where images will be saved(just name no slashes)
save_directory = 'Pictures'
# full save directory(including before and after slashes)
full_save_directory = '/home/mort/Pictures/'


def details(list_url, image_number=0):
   '''
   First create an instance of nasa class and use its functionality,
   to download nasa's landing page for it's image of the day,
   then follow the top link to another html where we can extract the image
   src from. Then format the images title to be used later for the filename.
   '''
   nasa_img = nasa.nasa() 
   # get page source of nasa images landing page
   soup = nasa_img.html_source(list_url) 
   # get top page link
   top_page_link = nasa_img.find_link(soup, image_number)
   #store title of image which is returned in position 1 of array
   image_title = top_page_link[1]
   # follow top link to get latest page of image results
   latest_page_html = nasa_img.html_source(top_page_link[0])
   # retrieve top image src from page
   image_src = nasa_img.find_img(latest_page_html)
   if image_src == 'refresh':
       details(list_url, int(image_number)+1)
   # Format title to be used later for filename
   filesafe_title = nasa_img.format_title(image_src, image_title)
   return [filesafe_title, image_src]
   
def setWallpaper(sys_set):
   '''
   At this point we have an images location and a file safe title for the image
   Now we need to download the file, and set our wallpaper
   '''
   download = sys_set.download(save_directory)
   wallpaper = sys_set.set_wallpaper(full_save_directory)

def number_images(list_url):
   nasa_image = nasa.nasa()      
   soup = nasa_image.html_source(list_url) 
   return nasa_image.number_images(soup)
   
       
def main(args, list_url):
   if len(args) == 1:
       image_details = details(list_url, image_number)
       sys_set = set_wallpaper.setWallpaper(image_details[0], image_details[1])         
       setWallpaper(sys_set)
   if len(args) > 1:
       total = number_images(list_url)     
   if args[1] == '-n':
       if len(args) != 3 or (args[2].isdigit() == False) or int(args[2]) > int(total):
          print usage(total)
       else:
           image_details = details(list_url, args[2])
           sys_set = set_wallpaper.setWallpaper(image_details[0], image_details[1])         
           setWallpaper(sys_set)               
               

def usage(total_images):
    msg  = "\n"
    msg += "Set your background to the latest NASA image of the day\n"
    msg += "Usage :\n"
    msg += "$ python wallpaper.py -n <int>\n"
    msg += "ie $ python wallpaper.py -n 123\n"
    msg += "Possible images from 0 - %s\n" % str(total_images)  
    msg += "Argument must be an integer and between the threshold." 
    return msg   
    
     
if __name__=='__main__':        
   # create an instance of nasa class and pass to main
   main(sys.argv, list_url)
