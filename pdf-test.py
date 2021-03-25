from bs4 import BeautifulSoup as bs
import requests
import urllib
import os
import pdfkit
import re

html_link = ('abc.html')
html_res = open(html_link, 'r')
    
# creating files with same name as name in html link 
filename = html_link+'.pdf'
if not os.path.isfile(filename):
    pdf = pdfkit.from_url(html_res,filename)
    print(filename)