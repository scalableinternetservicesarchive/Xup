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

