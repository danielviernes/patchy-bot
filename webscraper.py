from bs4 import BeautifulSoup
from configuration import config
from functools import lru_cache
import requests


@lru_cache(maxsize=32)
def getValorantVersion():
    url = config.links["valorant-news"]

    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")

    print(soup.prettify()) #debug

    versions = []
    patchNotesTitleSubstr = 'VALORANT PATCH NOTES'

    for newsTitle in soup.findAll('h5', attrs={'class':'NewsCard-module--title--1MoLu'}):
        print( newsTitle ) #debug
        if( patchNotesTitleSubstr in newsTitle.text.upper() ):
            versions.append(newsTitle.text)

    return versions[0].split()[-1]