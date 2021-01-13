import urllib.parse as parse
import urllib.request as request
import json,os,random
from configuration import config

TOKEN = ''

try: 
    TOKEN = os.getenv('GIPHY_TKN')
except (IndexError, TypeError):
    print( "Giphy token not found. Unable to use API.")
    exit()


def getRandomGif( query, limit=100 ):
    limit = limit

    base = config.links['giphy_search_api']
    params = { 'q': query, 'api_key': TOKEN, 'limit': limit }
    url = '{}?{}'.format( base, parse.urlencode(params) )
    print('url: ' + url)
    data=json.loads(request.urlopen(url).read())
    if(len(data['data']) < limit):
        limit = len(data['data'])
    return data['data'][random.randint(0, limit)-1]['embed_url']