import pytest
import requests

from bs4 import BeautifulSoup


class test_open_graph_standards:

    def test(self, meta, required_tags, found_tags):
        og_assert = True

        # Test list and add found tags to list
        for og_type in required_tags:
            for item in meta:
                if item.get('name') == og_type or item.get('property') == og_type:
                    found_tags.append(og_type)
                else:
                    continue

        # Test found list vs required list
        for item in required_tags:
            if item in found_tags:
                continue
            else:
                print "Item {} not found".format(item)
                og_assert = False
        assert og_assert
