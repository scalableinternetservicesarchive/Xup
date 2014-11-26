class PaperclipImage < ActiveRecord::Base
  # attr_accessible :p_image
  has_attached_file :p_image, styles: {
    medium: '300x300>',
    small: '140x140>',
    thumb: '64x64!'
  }
  validates_attachment_content_type :p_image, :content_type => /\Aimage\/.*\Z/

end
