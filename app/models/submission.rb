class Submission < ActiveRecord::Base
belongs_to :community
validates :title, length: {minimum: 5}

vlidates :url, :url => true

end
