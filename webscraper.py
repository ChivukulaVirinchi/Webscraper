from bs4 import BeautifulSoup as bs                   # The actual webscraper library
import requests                                       # To import all the data from a website  
import urllib                                         # To manage URLs
import os                                             # To make and delete folders
import pdfkit                                         # To convert the data obtained from HTML files into PDF
import re                                             # To filter the required URLs                                                
from requests.adapters import HTTPAdapter


url = 'https://docs.erpnext.com/docs/user/manual/en'                    
response = requests.get(url)
soup = bs(response.text,'html.parser')
a = soup.findAll('a',{'class':'stretched-link'})

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
print (card)
# for i in range(1,len(card)):

#     dirname = card[i].h3.text.strip()
#     print('creating folder for : ',dirname)
    
#     dirname = '/home/virinchi/code/'
#     if not os.path.isdir(dirname):
#         os.mkdir(dirname)
#     links = (card[i].findAll('a',{'href': re.compile('/docs/user/manual/en/*')}))
    
#     for f in links:
#         html_link = (f['href'])
#         html_res = requests.get('https://docs.erpnext.com' + html_link)
#         # creating files with same name as name in html link 
#         filename =  dirname+html_link+'.pdf'
#         if not os.path.isfile(filename):
#             pdf = pdfkit.from_url(html_res,filename)
#             print(filename)