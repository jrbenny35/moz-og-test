import requests
import pytest
from bs4 import BeautifulSoup


class TestOpenGraphStandards:

    # Load url and parse it
    @pytest.fixture
    def get_url(self, url):
        og_site = requests.get(url)
        soup = BeautifulSoup(og_site.content, "html.parser")
        return soup.find_all("meta")
