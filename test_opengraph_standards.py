import requests
from bs4 import BeautifulSoup


class TestOpenGraphStandards:

    og_required = [
        'og:title',
        'og:type',
        'og:url',
        'og:image',
    ]

    og_found = []

    #site = requests.get("http://ogp.me/")

    @pytest.fixture
    def test_for_og_standards(self, url):
        for og_type in self.og_required:
            for meta in url:
                if meta.get('property') == og_type:
                    self.og_found.append(og_type)
                else:
                    continue

    @pytest.fixture
    def test_required(self):
        for item in self.og_required:
            assert item in self.og_found, "Item: {} was not found".format(item)
            return True


    @pytest.fixture
    def get_url(self, url):
        site_url = url
        og_site = requests.get(site_url)
        soup = BeautifulSoup(og_site.content, "html.parser")
        og_data = soup.find_all("meta")
        return og_data

test = TestOpenGraphStandards()

data = test.get_url("http://mozilla.com")
test.test_for_og_standards(data)
print test.test_required()
