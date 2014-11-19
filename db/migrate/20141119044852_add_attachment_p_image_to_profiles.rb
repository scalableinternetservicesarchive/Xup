class AddAttachmentPImageToProfiles < ActiveRecord::Migration
  def self.up
    change_table :profiles do |t|
      t.attachment :p_image
    end
  end

  def self.down
    remove_attachment :profiles, :p_image
  end
end
