import pytest
from test_opengraph_standards import TestOpenGraphStandards

og_required = [
    'og:title',
    'og:type',
    'og:url',
    'og:image',
]

og_found = []

def test_it():
    test = TestOpenGraphStandards() #Instansiate object
    og_assert = True
    # Pass in URL
    data = test.get_url("http://nightly.mozilla.org")

    #Test list and add found tags to list
    for og_type in og_required:
        for meta in data:
            if meta.get('name') == og_type or meta.get('property') == og_type:
                og_found.append(og_type)
            else:
                continue

    for item in og_required:
        if item in og_found:
            #og_assert = True
            continue
        else:
            print "Item {} not found".format(item)
            og_assert = False
    assert og_assert
