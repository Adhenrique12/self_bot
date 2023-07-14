from bs4 import BeautifulSoup 
import json
import requests
import re

result = requests.get("https://hotleak.vip/subgirl0831/video/9404832")
soup = BeautifulSoup(result.text, "html.parser")

with open('output.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("HotLeak")
links = soup.find_all("div", {"class": "light-gallery-item"})[0][
                    "data-video"
                ]
link = json.loads(links)
print(link["source"][0]["src"])