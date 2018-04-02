from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.reddit.com/r/news/")
bsObj = BeautifulSoup(html.read());
print(bsObj.p)


for link in bsObj.find_all('a'):
    print(link.get('href'))
