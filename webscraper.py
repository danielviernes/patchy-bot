from bs4 import BeautifulSoup
from configuration import config
from functools import lru_cache
import requests
import re


@lru_cache(maxsize=32)
def getValorantVersion():
    url = config.links["valorant-news"]

    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")

    versions = []
    patchNotesTitleSubstr = 'VALORANT PATCH NOTES'

    for newsTitle in soup.findAll('h5', attrs={'class':'NewsCard-module--title--1MoLu'}):
        if( patchNotesTitleSubstr in newsTitle.text.upper() ):
            versions.append(newsTitle.text)
            break

    return versions[0].split()[-1]

@lru_cache(maxsize=32)
def getValorantPatchNotes():
    url = config.links["valorant-news"]

    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")

    notes = []

    for a in soup.findAll('a', attrs={'href':re.compile(r'valorant-patch-notes-')}):
        print(a['href']) #debug
        notes.append(a['href'])

    return config.links['valorant'] + notes[1]
    