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

open("./loadtestingsteffen/generate_dataset/user_mini.txt") do |users|
    users.read.each_line do |user|
        name, email, ps, psconfirm = user.chomp.split("|")
        user = User.create(name: name, email: email, password: ps, password_confirmation: psconfirm)
        user.profile = Profile.new(first_name: name.split[0], last_name: name.split[1])
    end
end


open("./loadtestingsteffen/generate_dataset/party_mini.txt") do |parties|
    parties.read.each_line do |party|
        pname, name, date, time, location, description = party.chomp.split("|")
        date = DateTime.strptime(date, "%Y-%m-%d")
        time = DateTime.strptime(time, "%H:%M")
        time = DateTime.new(date.year, date.month, date.day, time.hour, time.min, time.sec, date.zone)
        party = Party.create(name: pname, owner: name, date: date, time: time, location: location, description: description)
    end
end
