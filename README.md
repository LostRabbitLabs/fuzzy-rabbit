# fuzzy-rabbit.py
Auto fuzz URLs to detect weaknesses (leading to additional vulnerabilities) and create screenshots.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>
INSTALL/PRE-REQS:<BR>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>
1. Install pip!<BR>
apt-get install python-pip

2. Install needed Python libs:<BR>
pip install requests<BR>
pip install pyvirtualdisplay<BR>
pip install selenium<BR>

3. GIT CLONE the fuzzy-rabbit script/framework:
git clone https://github.com/LostRabbitLabs/fuzzy-rabbit<BR>

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>
HOW TO USE:<BR>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>

Usage:<BR>
<I>fuzzy-rabbit.py urls.txt</I>
<BR><BR>
Where 'urls.txt' contains 1 URL per line (protocol included):<BR>
http://www.site1.com/<BR>
https://www.site2.com/username=<BR>
http://mail.site3.com/login.php?<BR>

Output images will be in the 'RESULTS' directory. Enjoy!<BR>

-theLostRabbit
<BR><BR>

