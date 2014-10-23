class Party < ActiveRecord::Base
    validates :name, uniqueness: true
    validates :name, length: { maximum: 20 }
end
