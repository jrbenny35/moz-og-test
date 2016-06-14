import pytest
import requests
from bs4 import BeautifulSoup
from test_opengraph_standards import TestOpenGraphStandards

og_required = [
    'og:title',
    'og:type',
    'og:url',
    'og:image',
]

og_found = []

def test():
    # Instansiate object
    test = TestOpenGraphStandards() #Instansiate object

    # Pass in URL
    data = test.get_meta("http://ogp.me/")
    count = 0
    #Test list and add found tags to list
    for og_type in og_required:
        for meta in data:
            if meta.get('property') == og_type:
                count + 1
                og_found.append(og_type)
                break
            else:
                print "Item {} not found.".format(og_type)
                continue
        assert count == 4


    # Final assert testing the 2 lists
    #for item in og_required:
        #if item in og_found:
        #    og_assert = True
        #    break
        #else:
        #    print "Item {} not found".format(item)
        #    og_assert = False
    #assert og_assert
