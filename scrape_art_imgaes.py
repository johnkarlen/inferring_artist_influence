import os
import urllib3
import requests
from bs4 import BeautifulSoup
from io import StringIO
import re
import string

for letter in list(string.ascii_lowercase):
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://www.artchive.com/artchive/' + letter + '/')

    soup = BeautifulSoup(r.data, "lxml")
    for link in soup.find_all('a'):
        if link.get('href') in ['/artchive/', 'greek']:
            continue
        artist = link.get('href')
        artist_url = 'http://www.artchive.com/artchive/' + letter + '/' + artist
        artist_r = http.request('GET', artist_url)
        artist_soup = BeautifulSoup(artist_r.data, "lxml")
        paint_idx = artist_soup.find_all('a')
        if len(paint_idx) < 50:
            continue
        for pic in paint_idx:
            if pic.get('href') == '/artchive/' + letter:
                continue
            pname = re.search("\.jpg$", pic.get('href'))
            if pname:
                path = 'imgs/' + artist + pic.get('href')
                os.makedirs(os.path.dirname(path), exist_ok=True)
                f = open(path, 'wb')
                print(artist_url + pic.get('href'))
                f.write(requests.get(artist_url + pic.get('href')).content)
                f.close()
