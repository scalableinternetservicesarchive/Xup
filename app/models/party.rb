class Party < ActiveRecord::Base
    validates :name, :owner, :date, :time, :location, :description, :participants, presence: true
    validates :name, uniqueness: true
    validates :name, length: { maximum: 20 }
end
