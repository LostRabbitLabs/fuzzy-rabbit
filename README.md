# fuzzy-rabbit.py
Auto fuzz URLs to detect weaknesses (leading to additional vulnerabilities) and create screenshots.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
INSTALL/PRE-REQS:

1. Install pip!
apt-get install python-pip

2. Install needed Python libs:
pip install requests
pip install pyvirtualdisplay
pip install selenium


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Usage:<BR>
<I>fuzzy-rabbit.py urls.txt</I>

Where 'urls.txt' contains 1 URL per line (protocol included):<BR>
http://www.site1.com/<BR>
https://www.site2.com/username=<BR>
http://mail.site3.com/login.php?<BR>

Output images will be in the 'RESULTS' directory. Enjoy!

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


