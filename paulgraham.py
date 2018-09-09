import requests
import re
import os
from bs4 import BeautifulSoup

prefix = "http://www.paulgraham.com/"
url = prefix + "articles.html"

# gets all of the URL's from links
def parse_list_page():
    res = requests.get(url)
    content = res.text
    soup  = BeautifulSoup(content, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        links.append(link['href'])
    return links

# gets each essay and saves it in the './essays' directory
def get_essay_text(urls):
    curr_files = set(f for f in os.listdir('./essays'))
    for i, url_end in enumerate(urls):
        if url_end not in curr_files and url_end[0:5] != "https":
            print("getting " + url_end)
            essay_url= prefix + url_end
            essay_page = requests.get(essay_url)
            with open('essays/'+url_end, "w") as f:
                f.write(essay_page.text)
    print("finished!")


if __name__ == "__main__":
    urls = parse_list_page()
    get_essay_text(urls)
