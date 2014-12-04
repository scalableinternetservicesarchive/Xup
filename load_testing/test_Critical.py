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

    def my_test(self):
	server_url = self.server_url
	self.get(server_url, description='Get root URL')
	
	self.get(server_url + "/users/sign_up", description="View the user signup page")
	auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
	
	email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"
	username = Lipsum().getUniqWord();

	self.post(self.server_url + "/users",
		params=[['user[name]',username],
	    ['user[email]', email],
	      ['user[password]', 'alphabet'],
	      ['user[password_confirmation]', 'alphabet'],
	      ['authenticity_token', auth_token],
	      ['commit', 'Sign up']],
	    description="Create New User")
	#self.get(server_url + "/new", description="View the new partypage")
	
	#auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')


	#write test: create party, delete party
    def test_create_party(self):
		#my_test()
		server_url = self.server_url
		self.get(server_url, description='Get root URL')
		
		self.get(server_url + "/users/sign_up", description="View the user signup page")
		auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
		
		email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"
		username = Lipsum().getUniqWord();

		self.post(self.server_url + "/users",
			params=[['user[name]',username],
		    ['user[email]', email],
		      ['user[password]', 'alphabet'],
		      ['user[password_confirmation]', 'alphabet'],
		      ['authenticity_token', auth_token],
		      ['commit', 'Sign up']],
		    description="Create New User")
		# end my_test()
		# start create party
		self.get(server_url + "/new", description="View the host party page") # dont now if i need this yet
		auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
	
		partyname = Lipsum().getUniqWord()
		#username = Lipsum().getUniqWord();
		dummyDate = "03/12/2015"
		dummyTime = "22:17"
		dummyLocation = "Del playa drive 6761"
		dummyDecription = "Best party ever"

		self.post(self.server_url + "/parties",
		params=[['party[name]',partyname],
	    ['party[owner]', username],
	      ['party[date]', '03/12/2015'], #'2016-12-03'
	      ['party[time]', '22:17'],
	      ['party[location]', dummyLocation],
	      ['party[description]', dummyDecription],
	      ['authenticity_token', auth_token],
	      ['commit', 'Create Party']], # ['commit', 'Create Party']]
	    description="username created a New Party")
		self.get(server_url, description="back to indexpage")
		# end create party

		# start delete created party
		# self.get(server_url + "/myparties", description="View the myparties page") # dont now if i need this yet
		
		# self.delete(self.server_url + "/parties"),
		# params=['party[name]',partyname],
		# description="username deleted the New Party")
		# end delete created party

		


	# end write test: create party, delete party

    def test_critical_path(self):
	server_url = self.server_url
	self.get(server_url, description='Get root URL')
	self.get(server_url + "/users/sign_up", description="View the user signup page")

	auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
	email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"

	self.post(self.server_url + "/users",
	    params=[['user[email]', email],
	      ['user[password]', 'alphabet'],
	      ['user[password_confirmation]', 'alphabet'],
	      ['authenticity_token', auth_token],
	      ['commit', 'Sign up']],
	    description="Create New User")

	self.get(server_url + "/communities/new", description="View the new communities page")
	auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

	community_name = Lipsum().getSentence()
	self.post(self.server_url + "/communities",
	    params=[['community[name]', community_name],
	      ['authenticity_token', auth_token],
	      ['commit', 'Create Community']],
	    description="Create New Community")
	last_url = self.getLastUrl()

	created_community_id = last_url.split('/')[-1]
	self.get(server_url + "/communities/"+created_community_id, description="View the created community page")

	self.get(server_url + "/submissions/new", description="View the new submissions page")
	auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

	submission_title = Lipsum().getSentence()
	submission_url = "http://www."+Lipsum().getWord() + Lipsum().getUniqWord() + ".com/"
	self.post(self.server_url + "/submissions",
	    params=[['submission[title]', submission_title],
	      ['submission[url]', submission_url],
	      ['submission[community_id]', created_community_id],
	      ['authenticity_token', auth_token],
	      ['commit', 'Create Submission']],
	    description="Create New Submission")
	last_url = self.getLastUrl()
	created_submission_id = last_url.split('/')[-1]

	self.get(server_url + "/comments/new", description="View the new comments page")
	auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

	comment_message = Lipsum().getSentence()
	comment_parent = ''
	submission_id = created_submission_id
	self.post(self.server_url + "/comments",
	    params=[['comment[message]', comment_message],
	      ['comment[submission_id]', submission_id],
	      ['comment[parent_id]', comment_parent],
	      ['authenticity_token', auth_token],
	      ['commit', 'Create Comment']],
	    description="Create New Comment")


    def test_critical_path_readonly(self):
	server_url = self.server_url
	self.get(server_url, description='View root URL')
	#self.get(server_url + "/users/sign_up", description="View the user signup page")
	#self.get(server_url + "/communities/", description="View the communities page")
	#self.get(server_url + "/submissions/", description="View the new submissions page")
	self.get(server_url + "/past", description="View the past page") 
	self.get(server_url + "/closeparties", description="View the closeparties")




if __name__ in ('main', '__main__'):
  unittest.main()
