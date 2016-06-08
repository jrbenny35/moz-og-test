import requests
import pytest
from bs4 import BeautifulSoup


class TestOpenGraphStandards:

    # Required og tags
    og_required = [
        'og:title',
        'og:type',
        'og:url',
        'og:image',
    ]

    # Stors og tags found on page
    og_found = []

    # Test if the page has required tags
    @pytest.fixture
    def test_for_og_standards(self, url):
        for og_type in self.og_required:
            for meta in url:
                if meta.get('property') == og_type:
                    self.og_found.append(og_type)
                else:
                    continue

        # Run test against requred list every time
        self.test_required()

    # Test if the tags found match required tags
    @pytest.fixture
    def test_required(self):
        for item in self.og_required:
            assert item in self.og_found, "Item: {} was not found".format(item)
            return True

    # Load url and parse it
    @pytest.fixture
    def get_url(self, url):
        og_site = requests.get(url)
        soup = BeautifulSoup(og_site.content, "html.parser")
        return soup.find_all("meta")
