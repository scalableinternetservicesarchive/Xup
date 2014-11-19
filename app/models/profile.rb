class Profile < ActiveRecord::Base
  has_attached_file :p_image, styles: {
    medium: '300x300>',
    small: '140x140>',
    thumb: '64x64!'
  }
  validates_attachment_content_type :p_image, :content_type => /\Aimage\/.*\Z/

  # only one user to one Profile
  belongs_to :user
end
