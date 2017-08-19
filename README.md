# fuzzy-rabbit.py
Auto fuzz URLs to detect weaknesses (leading to additional vulnerabilities) and create screenshots.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>
INSTALL/PRE-REQS:<BR>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>
1. Install python:<BR>
apt-get install python

2. Install pip!<BR>
apt-get install python-pip
pip install --upgrade pip

3. Install needed Python libs:<BR>
pip install requests<BR>
pip install pyvirtualdisplay<BR>
pip install selenium<BR>
apt-get install xvfb<BR>
pip install virtualenv<BR>

4. Install Geckodriver! & BROWSER!<BR>
wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz<BR>

tar zxvf geckodriver-v0.18.0-linux64.tar.gz<BR>
chmod 655 geckodriver<BR>
cp geckodriver /usr/bin/geckdriver<BR>

apt-get install iceweasel<BR>
** can now use apt-get install firefox<BR>

5. GIT CLONE the fuzzy-rabbit script/framework:<BR>
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

