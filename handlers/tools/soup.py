from bs4 import BeautifulSoup
import json
import requests
import re


def soup(site_link: str) -> str:
    """This funtion return a link of the video."""

    link_video = site_link
    #link_video =  my_sites.link_video(site_link)

    print(link_video)

    return link_video