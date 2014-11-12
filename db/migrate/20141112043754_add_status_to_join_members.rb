class AddStatusToJoinMembers < ActiveRecord::Migration
  def up
    add_column :join_members, :status, :integer
  end

  def down
    remove_column :join_members, :status
  end
end
