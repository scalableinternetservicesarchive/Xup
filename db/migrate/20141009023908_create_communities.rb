class CreateCommunities < ActiveRecord::Migration
  def change
    create_table :communities do |t|
      t.string :me

      t.timestamps
    end
  end
end
