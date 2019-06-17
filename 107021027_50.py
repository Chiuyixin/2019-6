

from bs4 import BeautifulSoup
import requests
import os

url='http://fpsother.tripod.com/yi/content.htm'
html=requests.get(url)
html.encoding='big5'

Except_link='http'
sp=BeautifulSoup(html.text,'html.parser')

file_path='C:/Users/chiu yu-en/Desktop/程式碼/Novel.107021027'

if not os.path.exists(file_path):
    os.mkdir(file_path)
    
url_Base='http://fpsother.tripod.com/yi/'
links=sp.find_all('a')
for link in links:
    href=link.get('href')
    if not Except_link in(href):
        #print(url_Base + href)
        href_txt = href.replace(".htm","")
        FileName=file_path+'/'+href_txt+'_倚天屠龍記.txt'
        
        one_Article_url=url_Base+href
        one_Article_html=requests.get(one_Article_url)
        one_Article_html.encoding='big5'
        one_Article_sp=BeautifulSoup(one_Article_html.text,'html.parser')
        sentens=one_Article_sp.select('p')
        f = open (FileName,'wb') 
        for senten in sentens:
            #print (senten.text)      
            One_Article_Binary = senten.text.encode('big5','ignore')
        
            f.write(One_Article_Binary)
            
        f.close()     
    