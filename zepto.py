#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import print_function
from HTMLParser import HTMLParser
import urllib
import sys


class MyHTMLParser(HTMLParser):
    def init(self):
        gotWeekendDieShot = 0


    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if( attr[1] is not None and "//www.reddit.com/submit" in attr[1]):
            	if(len(attr[1].split(')', 1))>1 and self.gotWeekendDieShot == 1):
                    print(attr[1].split('(', 1)[1].split(')')[0])
                    self.gotWeekendDieShot = 0

    def handle_data(self, data):
    	if ("die-shot" in data.encode('cp1252')):
            print(data.encode('cp1252').split(':')[0], end='')
            self.gotWeekendDieShot = 1

parser = MyHTMLParser()
num = 1
while True:
    url = "https://zeptobars.com/en/?p="+str(num)
    num += 1
    page = urllib.urlopen(url).read()
    page = page.decode('cp1252','ignore')
    if len(page) <= 5000:
    	break
    parser.feed(page)
