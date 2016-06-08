import requests
from bs4 import BeautifulSoup

og_required = {
    'og:title',
    'og:type',
    'og:url',
}

site = requests.get("http://ogp.me/")
soup = BeautifulSoup(site.content, "html.parser")

og_data = soup.find_all("meta")

def test_for_og_standards():
    for og_type in og_required:
        for meta in og_data:
            if meta.get('property') == og_type:
                print meta.get('content')
            else:
                continue

test_for_og_standards()
