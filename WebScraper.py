import random
import requests 
from bs4 import BeautifulSoup

def LinkParser(url):
    AllowParse = requests.get(url=url)

    Parser = BeautifulSoup(AllowParse.content, 'html.parser')

    WebTitle = Parser.find(id="firstHeading")
    print(WebTitle.text)

    AllLinks = Parser.find(id="bodyContent").find_all('a')
    random.shuffle(AllLinks)
    Crawler = 0
    
    for links in AllLinks:
        if links['href'].find("/wiki/"):
            continue

        Crawler = links
        break

    LinkParser("https://en.wikipedia.org" + Crawler['href'])
    
LinkParser("https://en.wikipedia.org/wiki/Dune_(2021_film)")



