from webunit.webunittest import WebTestCase
import unittest

class TestPythonOrg(WebTestCase):
    '''Load the front page of www.python.org
    '''
    def test_home(self):
        page = self.page('http://www.python.org')

def suite():
    l = [
         unittest.makeSuite(TestPythonOrg, 'test'),
    ]
    return unittest.TestSuite(l)

