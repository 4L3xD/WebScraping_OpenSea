from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json


def Request_page(url):
    html = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    url = urlopen(html)
    bs = BeautifulSoup(url, "html.parser")
    return bs

raw_data = Request_page("https://opensea.io/rankings").find('script').text
#print(raw_data)
data = raw_data.replace("window.__wired__=", "")
json_object = json.loads(data)

#with open('data.json', 'w', encoding='latin-1') as f:
#    json.dump(json_object, f, indent=2, ensure_ascii=False)
#print("Created Json File! :)")

array = []
for nfts in json_object["records"]:
    if "client:root" not in nfts:
        nft = json_object["records"][nfts]
        array.append(nft)

links = []
for itens in array:
    for item in itens:
        if item == "name": 
            print(f"Coleção NFT: {itens[item]}")
        if item == "slug":
            url_collection = "https://opensea.io/collection/"
            #print(f"URL: {url_collection + itens[item]}")
            links.append(url_collection + itens[item])

#for link in links:
#    Request_page(link).find().text


#with open('nft.json', 'w', encoding='latin-1') as f:
#    json.dump(array, f, indent=2, ensure_ascii=False)
#print("Created Json File! :)")