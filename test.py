from bs4 import BeautifulSoup as bs
import requests
import urllib
import os
import pdfkit
import re


f = open('abc.html','r')
soup = bs(f, 'html.parser')
a = soup.findAll('a',{'href': re.compile('^/')})
b = soup.findAll('link',{'href': re.compile('^/')})
c = soup.findAll('script',{'src': re.compile('^/')})
d = soup.findAll('script',{'href': re.compile('https://')})
e = soup.findAll('link',{'href': re.compile('https://')})

for i in a:
    i['href'] = i['href'].replace('?ver=1616352305.528987', '') 
    i['href'] = 'https://docs.erpnext.com' + i['href']
for i in b:
    i['href'] = i['href'].replace('?ver=1616352305.528987', '') 
    i['href'] = 'https://docs.erpnext.com' + i['href']

for i in c:
    i['src'] =i['src'].replace('?ver=1616352305.528987', '') 
    i['src'] = 'https://docs.erpnext.com' + i['src']

for i in d:
    i['href'] =i['href'].replace('?ver=1616352305.528987', '') 
    i['href'] = 'https://docs.erpnext.com' + i['href']

for i in e:
    i['href'] =i['href'].replace('?ver=1616352305.528987', '') 
    i['href'] = 'https://docs.erpnext.com' + i['href']


sys.stdout = open('abc.html','w')
print(soup)
sys.stdout.close()
    