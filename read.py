#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse
import re
from re import *

kode = re.compile(r"<tr kode=\"(.*)\" class=\".*\"")
with open("E:/an8/garismiring-an8.github.io/index.html", "r+") as index:
    data = index.read()
    iterator = finditer(kode, data)
    count = 0
    for match in iterator:
        count +=1
    jav = kode.findall(data)
    soup = BeautifulSoup(data, 'html.parser')
    p = soup.find( 'table', attrs={ 'id' : 'xdcc-list' })
    hasil = p.text.strip()
print('')
for x in range(count):
    print(x+1,jav[x])
    print('')
print(hasil)
print('')
