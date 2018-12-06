import requests
from bs4 import BeautifulSoup

def get_wiki_links(url):
    '''This function takes the out links of a page given in url.
        /wiki is the starting tag of wikipedia pages
        PMID is the tag for counting the citations in a page (we are not interested about it)'''
    page_response = requests.get(url)
    soup = BeautifulSoup(page_response.content, "html.parser")
    links = []
    for link in soup.find_all('a'):
        temp = str(link.get('href'))
        if temp[0:5] == "/wiki" and "PMID" not in temp and ":" not in temp and "secolo" not in temp:
            try:
                int(temp[-4:])
            except:
                links.append("https://it.wikipedia.org" + temp)
    return links
