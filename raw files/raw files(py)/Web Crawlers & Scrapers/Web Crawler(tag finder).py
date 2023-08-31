import requests
from bs4 import BeautifulSoup
URL = input("write the site which you want to get the code of that: ")
TAG = input("do you want to tag a code(y/n): ")
if TAG=="n":
    o = requests.get(URL)
    soup = BeautifulSoup(o.content)
    print(soup.prettify())
    input()
if TAG=="y":
    TAG1 = input("write the code which you want to tag(for example: p): ")
    o = requests.get(URL)
    soup = BeautifulSoup(o.content)
    print(soup.find_all(TAG1))
    input()