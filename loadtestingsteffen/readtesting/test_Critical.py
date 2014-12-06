# -*- coding: iso-8859-15 -*-
"""Simple FunkLoad test

$Id$
"""
import unittest
from random import random
from funkload.FunkLoadTestCase import FunkLoadTestCase
from funkload.utils import extract_token
from funkload.Lipsum import Lipsum


class Critical(FunkLoadTestCase):
    """This test use a configuration file Simple.conf."""



    def setUp(self):
      """Setting up test."""
      self.server_url = self.conf_get('main', 'url')


    def readonly_test(self):

		server_url = self.server_url
		self.get(server_url, description="View the main page.")
		self.get(server_url + "/index", description="View the index page.")
		self.get(server_url + "/upcoming", description="View the upcoming party page.")
		self.get(server_url + "/past", description="View the past party page.")
		# self.get(server_url + "/closeparties", description="View the close party page.")
		self.get(server_url + "/users/sign_up", description="View the user signup page")



if __name__ in ('main', '__main__'):
  unittest.main()
