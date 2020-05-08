import requests
import json
baseurl="https://api.upcitemdb.com/prod/trial/lookup"
param={"upc":"888462323772"}

response=requests.get(baseurl,params=param)

print(response.url)

content=response.content
info=json.loads(content)

item=info['items']
iteminfo=item[0]
title=iteminfo['title']
brand=iteminfo['brand']
print(title)
print(brand)