from bs4 import BeautifulSoup as bs
import requests
import urllib
import os
import pdfkit
import re
import time
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

url = 'https://docs.erpnext.com/docs/user/manual/en'
response = requests.get(url)
soup = bs(response.text,'html.parser')
a=soup.findAll('a',{'class':'stretched-link'})

lb1 = soup.findAll('a',{'href': re.compile('^/')})
lb2 = soup.findAll('link',{'href': re.compile('^/')})
lb3 = soup.findAll('script',{'src': re.compile('^/')})
lb4 = soup.findAll('script',{'href': re.compile('https://')})
lb5 = soup.findAll('link',{'href': re.compile('https://')})

for i in lb1:
    i['href'] = i['href'].replace('?ver=1616352305.528987', '') 
    i['href'] = 'https://docs.erpnext.com' + i['href']
for i in lb2:
    i['href'] = i['href'].replace('?ver=1616352305.528987', '') 
    i['href'] = 'https://docs.erpnext.com' + i['href']

for i in lb3:
    i['src'] =i['src'].replace('?ver=1616352305.528987', '') 
    i['src'] = 'https://docs.erpnext.com' + i['src']

for i in lb4:
    i['href'] =i['href'].replace('?ver=1616352305.528987', '') 

for i in lb5:
    i['href'] =i['href'].replace('?ver=1616352305.528987', '') 



for element in a:
 name = element['href'].split('/')
 if name[2] == 'frappe.io':
     continue
 else:  name = element['href'].split('/')[5]
  
 link = element['href']
 directory = '/home/virinchi/code/python/python-beautiful-soup/webscraper/'
 print('saving : ',name)
 
card = soup.findAll('div',{'class':'card'})
for i in range(1,len(card)):
    # stripping topic heading name from the grid-box   
    dirname = card[i].h3.text.strip()
    print('creating folder for : ',dirname)
    
    # Creating a directory with same name as topic heading (replacing
    #spaces with underscore as spaces can create problem in creating folder)   
    dirname = '/home/virinchi/code/'
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    links = (card[i].findAll('a',{'href': re.compile('/docs/user/manual/en/*')}))
    
    for f in links:
        html_link = (f['href'])
        html_res = requests.get('https://docs.erpnext.com' + html_link)
        # creating files with same name as name in html link 
        filename =  dirname+html_link+'.pdf'
        if not os.path.isfile(filename):
            pdf = pdfkit.from_url(html_res,filename)
            print(filename)