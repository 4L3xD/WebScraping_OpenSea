from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json

html = Request("https://opensea.io/rankings", headers={'User-Agent': 'Mozilla/5.0'})

url = urlopen(html)
bs = BeautifulSoup(url, "html.parser")
#print(bs.prettify())

raw_data = bs.find('script').text
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

for itens in array:
    for item in itens:
        if item == "name": 
            print(f"Coleção NFT: {itens[item]}")
        if item == "slug":
            print(f"URL: {itens[item]}")

#with open('nft.json', 'w', encoding='latin-1') as f:
#    json.dump(array, f, indent=2, ensure_ascii=False)
#print("Created Json File! :)")