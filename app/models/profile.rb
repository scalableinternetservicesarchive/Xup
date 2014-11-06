class Profile < ActiveRecord::Base
  # only one user to one Profile
  belongs_to :user
end
