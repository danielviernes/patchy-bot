from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from configuration import config
from functools import lru_cache

driver = webdriver.Chrome(executable_path=r"C:/Development/tools/chromedriver/chromedriver.exe")

@lru_cache(maxsize=32)
def getValorantVersion():
    driver.get(config.links["valorant-news"])

    content = driver.page_source
    soup = BeautifulSoup(content)

    versions = []
    patchNotesTitleSubstr = 'VALORANT PATCH NOTES'

    for newsTitle in soup.findAll('h5', attrs={'class':'NewsCard-module--title--1MoLu'}):
        print( newsTitle )
        if( patchNotesTitleSubstr in newsTitle.text.upper() ):
            versions.append(newsTitle.text)

    return versions[0].split()[-1]