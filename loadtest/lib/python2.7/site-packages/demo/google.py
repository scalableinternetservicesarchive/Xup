from webunit.webunittest import WebTestCase
import unittest

class TestGoogle(WebTestCase):
    def setUp(self):
        self.server = 'www.google.com'

    def test_home(self):
        page = self.page('/')

    def test_form_good(self):
        page = self.page('/')
        page = page.getForm(0, self.page, {'q': 'Python Rules',
           'btnG': 'Google Search'})

    def test_form_bad(self):
        page = self.page('/')
        page = page.getForm(0, self.assertContent,
            {'q': 'eereerererre', 'btnG': 'Google Search'},
            'did not match any documents')

def suite():
    l = [
         unittest.makeSuite(TestGoogle, 'test'),
    ]
    return unittest.TestSuite(l)

