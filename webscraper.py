from bs4 import BeautifulSoup as bs
import requests
import urllib
import os
import pdfkit
url = 'https://www.bankexamstoday.com/2015/08/banking-awareness-questions-pdf.html'
response = requests.get(url)
soup = bs(response.text,'html.parser')
a=soup.findAll('a',{'class':'pdf'})

for element in a:
 name = element['href'].split('/')[4]
 link = element['href']
 directory = '/home/virinchi/code/python/python-beautiful-soup/webscraper/'
 print('saving : ',name)
 pdfFile = urllib.request.urlopen(link)
 file = open(directory+name, 'wb')
 file.write(pdfFile.read())
 file.close()
grid_box = soup.findAll('div',{'class':'grid-box'})
for i in range(1,len(grid_box)):
    # stripping topic heading name from the grid-box   
    dirname = grid_box[i].h2.text.strip()
    print('creating folder for : ',dirname)
    
    # Creating a directory with same name as topic heading (replacing
    #spaces with underscore as spaces can create problem in creating folder)   
    
    dirname = '/home/virinchi/code/python/python-beautiful-soup/webscraper/'+dirname.replace(' ','_')
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
links = (grid_box[i].findAll('a'))
for f in links:
        html_link = (f['href'])
        html_name = f.text.replace(' ','_').strip()
        html_res = requests.get(html_link)
        
    # creating files with same name as name in html link 
        filename =  dirname+'/'+html_name+'.pdf'
        
        if not os.path.isfile(filename):
            pdf = pdfkit.from_url(html_link,filename)
            print('created_file : '+dirname+'/'+html_name+'.pdf'+' successfully')