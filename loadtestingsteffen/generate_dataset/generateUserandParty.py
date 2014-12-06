from funkload.Lipsum import Lipsum
from random import randrange

userfile = open('user.txt', 'w')
partyfile = open('party.txt', 'w')

for i in xrange(0,10000):
    email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"
    name = Lipsum().getUniqWord()
    password = "asdfasdf"
    userfile.write( '{}|{}|{}|{}\n'.format(name, email, password, password))
    for j in xrange(0,5):
        pname = Lipsum().getUniqWord()
        # date = "2015/{}/{}".format(randrange(1,13), randrange(1,30))
        date = "2015-{}-{}".format(randrange(1,13), randrange(1,28))
        time = "{}:{}".format(randrange(1,24), randrange(0,60))
        # location = Lipsum().getSentence()
        location = "Los Angeles"
        description = Lipsum().getSentence()
        partyfile.write('{}|{}|{}|{}|{}|{}\n'.format(pname, name, date, time, location, description ))

