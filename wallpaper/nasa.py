#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2
import os
import sys

class nasa:

    #all images found around this url
    images_domain = 'http://apod.nasa.gov/apod/'
    
    def __init__(self):
        '''set some basic variables'''
        
    def html_source(self, url):   
        '''download source code of page with img links'''
        try:
            html = urllib2.urlopen(url)
            return BeautifulSoup(html)
        except:
            sys.exit("Unable to open url, Check network settings") 
                        
                          
    def find_link(self, soup, img_num=0):
        '''
        extract link to page holding image we want
        '''
       
        link = soup.findAll('a')[int(img_num) + 3]
        return [ self.images_domain + link['href'], link.text]
       
             
    
    def find_img(self, html):
        '''extract image src from html'''
        try:
            return self.images_domain + html.find('img')['src']
        except:
            ''' 
            sometimes nasa posts a video instead of an image
            if this happens restart script and down 1 down list
            '''
            return 'refresh'
            

    def format_title(self, src, title):
        '''reformat the title to use for image name'''
        extension = src[-4:]
        return title.replace(' ', '') + extension
     
    def number_images(self, soup):
        return len(soup.findAll('a')) - 14        
