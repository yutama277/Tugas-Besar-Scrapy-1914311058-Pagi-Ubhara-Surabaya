from urllib.request import urlopen
from bs4 import BeautifulSoup
link = "https://www.worldnovel.online/"
html = urlopen(link).read()
soup = BeautifulSoup(html, 'html.parser')
recent_added = soup.find("tbody")
for q in recent_added.findAll('a', href=True):
    print(q.text)
    print(q['href'])