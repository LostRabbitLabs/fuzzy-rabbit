#!/usr/bin/python
import requests
import socket
import sys
from pyvirtualdisplay import Display
from selenium import webdriver
import time

# usage = ./fuzzy-rabbit.py urls.txt
# where urls.txt:
# http://www.dom1.com/login?
# https://dom2.com/username=
# https://dom3.com:8080/cgi-bin/a.php?

input_filename1 = sys.argv[1]

user_agent = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/547.46 Chrome/36.0.1987.187 Safari/547.46'}

urls = []
fuzzy_items_full = []

########################  1) open files for input - list of urls/fuzzy_items #######################
with open(input_filename1, "r") as infile:
    for line in infile:
        line = line.rstrip()
        line = line.replace("&", "&amp;")
        urls.append(line)
    infile.close()

with open("all-fuzzing.txt", "r") as infile2:
    for lines in infile2:
        lines = lines.rstrip()
        lines = lines.replace("&", "&amp;")
        fuzzy_items_full.append(lines)
    infile2.close()

########################  2) loop thru urls and make screenshots of fuzzy_urls ########
for hosts in urls:
    try:
        fullurl_http = (hosts)
    except:
        pass
        print "!! error with fullurl_http = (hosts)"
    searchid = str(time.time())
    filename1 = "RESULTS/HTTP-FUZZY-" + searchid  + ".png"
    output_filename = "RESULTS/HTTP-FUZZY-" + searchid  + ".txt"
    display = Display(visible=0, size=(1024, 768))
    display.start()
    browser = webdriver.Firefox()
    browser.accept_untrusted_certs = True
    try:
        browser.get(fullurl_http)
        browser.get_screenshot_as_file(filename1)
    except:
        pass
        print "\n"
        print "!! error screenshot http"
    try:
        count = 0
        for fuzzy_items in fuzzy_items_full:
            print count
            print "\n"
            print fuzzy_items
            print "\n\n"
            count_str = str(count)
            filename2 = "RESULTS/HTTP-FUZZY-" + searchid  + "-fuzz-" + count_str + ".png"
            fullurl_http_fuzz1 = fullurl_http + fuzzy_items
            browser.get(fullurl_http_fuzz1)
            try:
                with open(output_filename, "a") as fuzzy_urls:
                    fuzzy_urls.write(count_str + ":  " + fullurl_http_fuzz1 + "\n")
            except:
                pass
                print "error SAVING output file !!!!!"
            print "\n"
            print fullurl_http_fuzz1
            print "\n"
            try:
                browser.get_screenshot_as_file(filename2)
            except:
                pass
                print" !!! no screenshot for you !!! - ERROR browser.get_screenshot_as_filename2"
            count = count + 1
    except:
        pass
        print "\n"
        print "!! error fully_items_full loop"


browser.close()
display.stop()

print "\n\nCOMPLETE!!\n"

sys.exit()

