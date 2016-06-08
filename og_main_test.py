import pytest
from test_opengraph_standards import TestOpenGraphStandards

def test_it():
    test = TestOpenGraphStandards() #Instansiate object

    #Pass in URL
    data = test.get_url("http://ogp.me/")

    #pass url and test
    test.test_for_og_standards(data)
