"""FunkLoad test to create sevral Users"""
import unittest

import random
from funkload.FunkLoadTestCase import FunkLoadTestCase
from funkload.utils import extract_token
from funkload.Lipsum import Lipsum


class CreateUser(FunkLoadTestCase):
    """This test uses createUser.conf."""

    def setUp(self):
        """Setting up test."""
        self.server_url = self.conf_get('main', 'url')

    def test_signup_path(self):
        server_url = self.server_url
        # Get homepage
        # error here
        self.get(server_url, description="View the landing page")


        # Fill out manual signup form
        username = Lipsum().getUniqWord()
        email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
      
        self.addMetadata(**{'auth_token': auth_token})

        # for x in range(0, 3):
        #     self.get(self.server_url + '/users/check_username.json',
        #              params=[['username', Lipsum().getWord()]],
        #              description='Check username availability')
        #     self.get(self.server_url + '/users/check_email.json',
        #              params=[['username', Lipsum().getWord() + "@" + Lipsum().getWord()]],
        #              description='Check email availability')
        #     self.get(self.server_url + '/users/check_password.json',
        #              params=[['username', Lipsum().getWord()]],
        #              description='Check password availability')

        
        self.post(self.server_url + "/users/sign_up",
                  params=[['user[name]', username],
                          ['user[email]', email],
                          ['user[password]', 'alphabet'],
                          ['user[password_confirmation]', 'alphabet'],
                          #['authenticity_token', auth_token],
                          ['commit', 'Sign up']
                          ],
                  description="Create New User")
        self.get(self.server_url, description="View the homepage after signup")

  def my_test(self):
      server_url = self.server_url
      self.get(server_url + "/past", description="View the past page")
      self.get(server_url, description='Get root URL')
      self.get(server_url + "/users/sign_up", description="View the user signup page")
      auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
      email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"

      self.post(self.server_url + "/users",
        params=[['user[name]',Lipsum().getUniqWord()],
          ['user[email]', email],
            ['user[password]', 'alphabet'],
            ['user[password_confirmation]', 'alphabet'],
            ['authenticity_token', auth_token],
            ['commit', 'Sign up']],
          description="Create New User")

      self.get(server_url + "/index", description="View the indexpage2")
      auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')



if __name__ in ('main', '__main__'):
    unittest.main()