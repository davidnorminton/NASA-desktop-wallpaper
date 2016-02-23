<h1> NASA desktop wallpaper</h1>
<p>
This python script downloads the latest NASA image of the day and sets it as your desktop wallpaper
Notes :
<p>
<ul>
    <li> *Currently this script is only working with the linux gnome desktop enviroment</li>
    <li> *Requires <a href="http://www.crummy.com/software/BeautifulSoup/">BeautifulSoup</a></li>
    <li> *Also requires python 2.6</li>
</ul>
This script works on the command line with the following options:<br />
<pre>
<code>
// some a help menu and show number of possible images to add
 $ python -h
</code>
</pre>
<pre>
<code>
// set wallpaper to a specific number<br />
 $ python - n <a number> <br />
</code>
</pre>
<p>
This script can also run on start up by adding a file called "wallpaper.desktop" placed in the directory 
"~/.config/autostart"
</p>
// Add the following lines to this file :
<pre>
<code>
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
</code>
</pre>
<h3>Future updates:</h3>
<p>Will include improved performance, multiple os detection, and list image titles.</p>
