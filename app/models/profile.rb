class Profile < ActiveRecord::Base
  has_attached_file :p_image,
  							 :styles => {
									    :medium => '300x300>',
									    :small => '140x140>',
									    :thumb => '64x64!'
  							},
                # Here place code for uploading photos on AWS
  							# :storage => :s3,
	        #   				:s3_credentials => "#{Rails.root}/config/aws.yml",
	        #   				:path => "Xup/:class/:attachment/:id/:style/:filename",
         #    				:bucket => "cs290"
	


  #validates_attachment_content_type :p_image, :content_type => /\Aimage\/.*\Z/
  validates_attachment_content_type :p_image, :content_type => ["image/jpg", "image/jpeg", "image/png", "image/jfif"]

  # only one user to one Profile
  belongs_to :user
end
