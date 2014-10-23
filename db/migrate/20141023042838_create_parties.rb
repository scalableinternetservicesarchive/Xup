class CreateParties < ActiveRecord::Migration
  def change
    create_table :parties do |t|
      t.string :name
      t.string :owner
      t.string :time
      t.string :location
      t.text :description
      t.text :participants

      t.timestamps
    end
  end
end
