# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)

Party.delete_all
=begin
@d=Date.today

Party.create!(name: 'Isla Vista Halloween',
             owner: 'Lars',
             time: 'Oct-26-2014',
             location: 'Isla Vista',
             description: 'A halloween party',
             participants: 'Steffen',
             date: @d
             )

Party.create!(name: 'Party 1',
             owner: 'Bob',
             time: 'Oct-29-2014',
             location: 'Isla Vista 1',
             description: 'party 1',
             participants: 'Bob, Lars, Steffen, YY',
             date: @d,
             )

=end

user = User.create! :name => 'First User', :email => 'user@example.com', :password => 'asdfasdf', :password_confirmation => 'asdfasdf'
user.confirm!

user.profile = Profile.new(
          first_name: user.name.split[0],
          last_name: user.name.split[1],

        )

user = User.create! :name => 'Second User', :email => 'user2@example.com', :password => 'asdfasdf', :password_confirmation => 'asdfasdf'
user.confirm!

user.profile = Profile.new(
          first_name: user.name.split[0],
          last_name: user.name.split[1],

        )

user = User.create! :name => 'Third User', :email => 'user3@example.com', :password => 'asdfasdf', :password_confirmation => 'asdfasdf'
user.confirm!

user.profile = Profile.new(
          first_name: user.name.split[0],
          last_name: user.name.split[1],

        )


user_list = [
  ["Peter", "user1@abc.com", "asdfasdf", "asdfasdf"],
  ["Mary", "user2@abc.com", "asdfasdf", "asdfasdf"],
  ["Harry", "user3@abc.com", "asdfasdf", "asdfasdf"],
  ["Jack", "user4@abc.com", "asdfasdf", "asdfasdf"]
]

user_list do |name, email, password, password_confirmation|
    User.create(name: name, email: email, password: password, password_confirmation: password_confirmation)
end

party_list = [
  ["Party 1", "Peter", "2016-12-30", "17:00", "Los Angeles", "Good party"],
  ["Party 2", "Peter", "2016-10-30", "17:00", "Los Angeles", "Good party"],
  ["Party 3", "Mary", "2015-12-30", "17:00", "Los Angeles", "Good party"],
  ["Party 4", "Harry", "2015-01-30", "17:00", "Los Angeles", "Good party"],
  ["Party 5", "Harry", "2016-02-30", "17:00", "Los Angeles", "Good party"],
  ["Party 6", "Jack", "2015-11-30", "17:00", "Los Angeles", "Good party"],
  ["Party 7", "Jack", "2014-12-30", "17:00", "Los Angeles", "Good party"],
  ["Party 8", "Jack", "2016-11-30", "17:00", "Los Angeles", "Good party"]
]

party_list do |name, owner, date, time, location, description|
    Party.create(name: name, owner: owner, date: date, time: time, location: location, description: description)
end
