from bs4 import BeautifulSoup
import json
import requests
import re



def link_video(link: str):

    link_video = link
    motherless = link_video[8:18]  # https://motherless.com/
    hotleak = link_video[8:15]  # https://hotleak.vip/
    links = [motherless, hotleak]

    result = requests.get(link_video)
    soup = BeautifulSoup(result.text, "html.parser")

    for link in links:
        match link:
            case "motherless":
                links = soup.find_all("source")
                link_video_to_download = links[0].get("src")
                return link_video_to_download

            case "hotleak":
                links = soup.find_all("div", {"class": "light-gallery-item"})[0][
                    "data-video"
                ]
                link = json.loads(links)
                return link["source"][0]["src"]

    m = re.search(r"https:\/\/.*\.mp4", result.text)
    if m is not None and link_video[8:17] != "spankbang":
        return m.group(0)
    
    return link_video