import requests
from bs4 import BeautifulSoup
url ="https://scrapingclub.com/exercise/list_basic/?page=1"
response=requests.get(url)

soup=BeautifulSoup(response.text,"lxml")


pages=soup.find("ul",class_="pagination")
urls=[]
links=pages.find_all("a",class_="page-link")

for link in links:
    pNum=int(link.text) if link.text.isdigit() else None
    if pNum!= None:
        x=link.get('href')
        urls.append(x)
print(urls)
count=1
for x in urls:
    newurl=url+x
    response=requests.get(newurl)
    soup=BeautifulSoup(response.text,"lxml")
    items=soup.find_all("div",class_="col-lg-4 col-md-6 mb-4")
   
    for i in items:
        itemName=i.find("h4",class_="card-title").text.strip("\n")
        itemPrice=i.find("h5").text
        print(" %s ) Price:%s, ItemName: %s"%(count,itemPrice,itemName))
        count+=1