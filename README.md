# NASA-desktop-wallpaper

This python script downloads the latest NASA image of the day and sets it as your desktop wallpaper
Notes :
      *Currently this script is only working with the linux gnome desktop enviroment
      *Requires <a href="http://www.crummy.com/software/BeautifulSoup/">BeautifulSoup</a>

This script works on the command line with the following options:
      // some a help menu and show number of possible images to add
      $ python -h
      // set wallpaper to a specific number
      $ python - n <a number> 

This script can also run on start up by adding a file called "wallpaper.desktop" placed in the directory "~/.config/autostart"
// Add the following lines to this file :

[Desktop Entry]
Encoding=UTF-8
Name=Wallpaper_changer
Comment=Images from nasa image of the day
Icon=gnome-info
Exec=python ~/wallpaper.py
Terminal=false
Type=Application
Categories=

X-GNOME-Autostart-enabled=true
X-GNOME-Autostart-Delay=1

Future updates:
 Will include improved performance, multiple os detection, and list image titles.