class Party < ActiveRecord::Base
    validates :name, :owner, :date, :time, :location, :description, presence: true
    validates :name, uniqueness: true
    validates :name, length: { maximum: 20 }

    geocoded_by :location
    #after_validation :geocode
    
    # A party can have many user's
    has_many :user

    has_many :join_members, dependent: :destroy

end
