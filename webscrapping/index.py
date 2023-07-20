import requests
import bs4
res = requests.get("https://en.wikipedia.org/wiki")
# print(type(res))

soup = bs4.BeautifulSoup(res.text, 'html5lib')
# print("The object type:", soup)

soup.select('.mw-footer')
for i in soup.select('.mw-footer'):

    i.select(".noprint")
    for i1 in i.select(".noprint"):
        print(i1)
