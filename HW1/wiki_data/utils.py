import requests
from bs4 import BeautifulSoup
import gzip
import pandas as pd


#month page

def get_pageviews(string):
    if "pageviews-" in string:
        return True
    else:
        return False

def get_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    files = [url+i.get("href") for i in soup.find_all("a")]
    return list(filter(get_pageviews,files))


def retrieve_info(file):
    
    with gzip.open(file) as f:
        d = pd.read_csv(f, sep = " ", header = None, usecols = [0,1,2])
        
    return [file[-18:-10],int(sum(d[2].loc[((d[0] == "it")|(d[0] == "it.m")) & (d[1] == "Influenza")]))]    

def write_file(map_obj):
    with open("flu_data.tsv", "w") as f:
        for idx,file in enumerate(map_obj):
            print(idx)
            f.write(file[0] + "\t" + str(file[1]) + "\n")