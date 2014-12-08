# -*- coding: iso-8859-15 -*-
"""Simple FunkLoad test

$Id$
"""
import unittest
from random import random
import random
from funkload.FunkLoadTestCase import FunkLoadTestCase
from funkload.utils import extract_token
from funkload.Lipsum import Lipsum


class Critical(FunkLoadTestCase):
    """This test use a configuration file Simple.conf."""

    def view_stuff(self):
        server_url = self.server_url
        print "watching upcoming"
        self.get(server_url + "/upcoming", description="View the upcoming page")
        print "watching indexpage"
        self.get(server_url + "/index", description="View the index page")

        self.get(server_url + "/users/sign_up", description="View the user signup page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"
        name = Lipsum().getUniqWord()
        print "posting user"
        self.post(self.server_url + "/users",
                params=[['user[name]',name],
                ['user[email]', email],
                  ['user[password]', 'alphabet'],
                  ['user[password_confirmation]', 'alphabet'],
                  ['authenticity_token', auth_token],
                  ['commit', 'Sign up']],
                description="Create New User")
            

            #self.get(server_url + "/index", description="View the indexpage2")
            #auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        self.get(server_url + "/new", description="view party page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        print "posting party"
        self.post(self.server_url + "/parties",
                params=[['party[name]', Lipsum().getUniqWord()],
                  ['party[owner]', name],
                  ['party[date]', '2016-12-03'],
                  ['party[time]', '17:00'],
                  ['party[location]',Lipsum().getUniqWord()],
                  ['party[description]',Lipsum().getUniqWord()],
                  ['authenticity_token', auth_token],
                  ['commit', 'Sign up']],
                description="Create New party")
            
        last_url = self.getLastUrl()

        created_party_id = last_url.split('/')[-1]

        self.get(server_url + "/invitetoparty/"+created_party_id, description="View invite page ")
        print "watching invite"






    def setUp(self):
      """Setting up test."""
      self.server_url = self.conf_get('main', 'url')

    def view_close_parties(self):
    	server_url = self.server_url
    	self.get(server_url + "/closeparties", description="Watching the close parties")
    

    def join_a_party(self):
        server_url = self.server_url    
        self.get(server_url, description='Get root URL')
        self.get(server_url + "/users/sign_up", description="View the user signup page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"
        name = Lipsum().getUniqWord()
        self.post(self.server_url + "/users",
                params=[['user[name]',name],
                ['user[email]', email],
                  ['user[password]', 'alphabet'],
                  ['user[password_confirmation]', 'alphabet'],
                  ['authenticity_token', auth_token],
                  ['commit', 'Sign up']],
                description="Create New User")

        last_url = self.getLastUrl()
        party_to_join=1
        user_id = last_url.split('/')[-1]
        self.get(server_url + "/index", description="watching parties to join")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        self.post(self.server_url + "/join_members",
                params=[['party_id', party_to_join],['user_id',user_id],['authenticity_token', auth_token]],
                  
                description="Joining party")

    def create_a_close_parties(self):
        print 'begin'
        #creates many parties close to UCSB
        server_url = self.server_url
        self.get(server_url + "/users/sign_up", description="View the user signup page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"
        name = Lipsum().getUniqWord()
        print 'create a user'
        self.post(self.server_url + "/users",
                params=[['user[name]',name],
                ['user[email]', email],
                  ['user[password]', 'alphabet'],
                  ['user[password_confirmation]', 'alphabet'],
                  ['authenticity_token', auth_token],
                  ['commit', 'Sign up']],
                description="Create New User")
        print 'go to party page '
        self.get(server_url + "/new", description="create party page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
       
        rand = random.random()
        
        ran=rand/10
        
        lat=34.42
            
        lon=119.8+ran
        print 'posting a party'
        self.post(self.server_url + "/parties",
            params=[['party[name]', Lipsum().getUniqWord()],
              ['party[owner]', name],
              ['party[date]', '2016-12-03'],
              ['party[time]', '17:00'],
              ['party[location]',''+str(lat)+', -'+str(lon)],
              ['party[description]',Lipsum().getUniqWord()],
              ['authenticity_token', auth_token],
              ['commit', 'Sign up']],
            description="Create New party")
        print 'all done'

    def accept_all_invites(self):
        server_url = self.server_url

        #This needs to be a created user
        user_mail='st@st.com'
        # If it is an autogenerated user this is the password
        password='asdfasdf'

        
        self.get(server_url + "/users/sign_in", description="Go to log in page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        self.post(self.server_url + "/users/sign_in",
            params=[['user[email]', user_mail],
              ['user[password]', password],
              ['authenticity_token', auth_token],
              ['commit', 'Log in']],
            description="Create New User")

        last_url = self.getLastUrl()
        user_id = last_url.split('/')[-1]

        self.get(server_url + "/myinvites", description="going to watch my invites")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

        party_range=16
        
        for i in range (1,party_range):
            self.post(self.server_url + "/partyrequest/join",
                    params=[['party_id', i],['user_id',user_id],['authenticity_token', auth_token]],
                      
                    description="Joining party")


    def accept_a_invite(self):
        
        server_url = self.server_url
        #This needs to be a created user
        user_mail='bcbotc@lineatus.com'
        # If it is an autogenerated user this is the password
        password='alphabet'
        
        print 'Goin to sign_in page'
        self.get(server_url + "/users/sign_in", description="Go to log in page")
        print 'on the page'
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        print 'sending post now'
        self.post(self.server_url + "/users/sign_in",
            params=[['user[email]', user_mail],
              ['user[password]', password],
              ['authenticity_token', auth_token],
              ['commit', 'Log in']],
            description="Create New User")

        last_url = self.getLastUrl()
        user_id = last_url.split('/')[-1]
        print 'going to myinvites'
        self.get(server_url + "/myinvites", description="going to watch my invites")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

        #the id of a party you have been invited to
        party_id =27

        print 'accepting a party invite'
        self.post(self.server_url + "/partyrequest/join",
                    params=[['party_id', party_id],['user_id',user_id],['authenticity_token', auth_token]],
                    description="Accetping the invite")

        print 'all done'



    def join_all_parties(self):
        
        server_url = self.server_url    
        self.get(server_url, description='Get root URL')
        self.get(server_url + "/users/sign_up", description="View the user signup page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"
        name = Lipsum().getUniqWord()
        self.post(self.server_url + "/users",
                params=[['user[name]',name],
                ['user[email]', email],
                  ['user[password]', 'alphabet'],
                  ['user[password_confirmation]', 'alphabet'],
                  ['authenticity_token', auth_token],
                  ['commit', 'Sign up']],
                description="Create New User")

        last_url = self.getLastUrl()
        party_range=3
        user_id = last_url.split('/')[-1]
        self.get(server_url + "/index", description="watching parties to join")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        for i in range (1,party_range):
            self.post(self.server_url + "/join_members",
                    params=[['party_id', i],['user_id',user_id],['authenticity_token', auth_token]],
                      
                    description="Joining party")




    def invite_a_user(self):
       	server_url = self.server_url	
    	
    	self.get(server_url + "/users/sign_up", description="View the user signup page")
    	auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
    	email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"
    	name = Lipsum().getUniqWord()
    	self.post(self.server_url + "/users",
    			params=[['user[name]',name],
    		    ['user[email]', email],
    		      ['user[password]', 'alphabet'],
    		      ['user[password_confirmation]', 'alphabet'],
    		      ['authenticity_token', auth_token],
    		      ['commit', 'Sign up']],
    		    description="Create New User")
    		

    		#self.get(server_url + "/index", description="View the indexpage2")
    		#auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
    	self.get(server_url + "/new", description="create party page")
    	auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

    	self.post(self.server_url + "/parties",
    		    params=[['party[name]', Lipsum().getUniqWord()],
    		      ['party[owner]', name],
    		      ['party[date]', '2016-12-03'],
    		      ['party[time]', '17:00'],
    		      ['party[location]',Lipsum().getUniqWord()],
    		      ['party[description]',Lipsum().getUniqWord()],
    		      ['authenticity_token', auth_token],
    		      ['commit', 'Sign up']],
    		    description="Create New party")
    		
    	last_url = self.getLastUrl()

    	created_party_id = last_url.split('/')[-1]

        userid=1
    		

    	self.post(self.server_url + "/createasinvite/",
    		    params=[['party_id', created_party_id],['user_id',userid],['authenticity_token',auth_token]],
    		      
    		    description="Create New party")


    def create_a_user(self):
        
        server_url = self.server_url
        self.get(server_url + "/users/sign_up", description="View the user signup page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"
        name = Lipsum().getUniqWord()
        self.post(self.server_url + "/users",
            params=[['user[name]',name],
            ['user[email]', email],
              ['user[password]', 'alphabet'],
              ['user[password_confirmation]', 'alphabet'],
              ['authenticity_token', auth_token],
              ['commit', 'Sign up']],
            description="Create New User")

    def create_many_parties(self):
        server_url = self.server_url
       
        #This needs to be a created user
        user_mail='e@a.com'
        username='oijijojio'
        # If it is an autogenerated user this is the password
        password='asdfasdf'
        
        print 'Goin to sign_in page'
        self.get(server_url + "/users/sign_in", description="Go to log in page")
        print 'on the page'
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        print 'sending post now'
        self.post(self.server_url + "/users/sign_in",
            params=[['user[email]', user_mail],
              ['user[password]', password],
              ['authenticity_token', auth_token],
              ['commit', 'Log in']],
            description="Create New User")
        

        #self.get(server_url + "/index", description="View the indexpage2")
        #auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        self.get(server_url + "/new", description="create party page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        party_amount=10

        for i in range (party_amount):
            print 'making the party'

            self.post(self.server_url + "/parties",
                params=[['party[name]', Lipsum().getUniqWord()],
                  ['party[owner]', username],
                  ['party[date]', '2016-12-03'],
                  ['party[time]', '17:00'],
                  ['party[location]',Lipsum().getUniqWord()],
                  ['party[description]',Lipsum().getUniqWord()],
                  ['authenticity_token', auth_token],
                  ['commit', 'Sign up']],
                description="Create New party")


    def create_and_delete_party(self):
		
		server_url = self.server_url
		self.get(server_url + "/users/sign_up", description="View the user signup page")
		auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
		email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"
		name = Lipsum().getUniqWord()
		self.post(self.server_url + "/users",
			params=[['user[name]',name],
		    ['user[email]', email],
		      ['user[password]', 'alphabet'],
		      ['user[password_confirmation]', 'alphabet'],
		      ['authenticity_token', auth_token],
		      ['commit', 'Sign up']],
		    description="Create New User")
		

		#self.get(server_url + "/index", description="View the indexpage2")
		#auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
		self.get(server_url + "/new", description="create party page")
		auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

		self.post(self.server_url + "/parties",
		    params=[['party[name]', Lipsum().getUniqWord()],
		      ['party[owner]', name],
		      ['party[date]', '2016-12-03'],
		      ['party[time]', '17:00'],
		      ['party[location]',Lipsum().getUniqWord()],
		      ['party[description]',Lipsum().getUniqWord()],
		      ['authenticity_token', auth_token],
		      ['commit', 'Sign up']],
		    description="Create New party")
		
		last_url = self.getLastUrl()

		created_party_id = last_url.split('/')[-1]

		self.get(server_url + "/myparties", description="Going to my parties page")
		auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
		

		self.delete(self.server_url + '/parties/'+created_party_id, description="Delete the party",)
		self.get(server_url + "/", description="Back to index page")

		

    def my_test(self):


		server_url = self.server_url
		self.get(server_url + "/past", description="View the past page")
		self.get(server_url + "/past", description="View the past page again")
		self.get(server_url, description='Get root URL')
		self.get(server_url + "/users/sign_up", description="View the user signup page")
		auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
		email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"
		name = Lipsum().getUniqWord()
		self.post(self.server_url + "/users",
			params=[['user[name]',name],
		    ['user[email]', email],
		      ['user[password]', 'alphabet'],
		      ['user[password_confirmation]', 'alphabet'],
		      ['authenticity_token', auth_token],
		      ['commit', 'Sign up']],
		    description="Create New User")
		

		#self.get(server_url + "/index", description="View the indexpage2")
		#auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
		self.get(server_url + "/new", description="View the past page2")
		auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

		self.post(self.server_url + "/parties",
		    params=[['party[name]', Lipsum().getUniqWord()],
		      ['party[owner]', name],
		      ['party[date]', '2016-12-03'],
		      ['party[time]', '17:00'],
		      ['party[location]',Lipsum().getUniqWord()],
		      ['party[description]',Lipsum().getUniqWord()],
		      ['authenticity_token', auth_token],
		      ['commit', 'Sign up']],
		    description="Create New party")
		self.get(server_url, description="back to indexpage")





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
    	self.get(server_url, description='View root URL3')
    	#self.get(server_url + "/users/sign_up", description="View the user signup page")
    	#self.get(server_url + "/communities/", description="View the communities page")
    	#self.get(server_url + "/submissions/", description="View the new submissions page")
    	self.get(server_url + "/past", description="View the past page") 
    	self.get(server_url + "/closeparties", description="View the closeparties")



    def fast_test(self):
    	server_url = self.server_url
    	self.get(server_url , description="View the past page")

    def fast_test2(self):
    	server_url = self.server_url
    	
    	self.get(server_url , description="View the past page again")
    	fast_test(self)






if __name__ in ('main', '__main__'):
  unittest.main()
