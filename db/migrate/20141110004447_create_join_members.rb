class CreateJoinMembers < ActiveRecord::Migration
  def change
    create_table :join_members do |t|
      t.references :user, index: true
      t.belongs_to :party, index: true

      t.timestamps
    end
  end
end
