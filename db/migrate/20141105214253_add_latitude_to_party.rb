class AddLatitudeToParty < ActiveRecord::Migration
  def change
    add_column :parties, :latitude, :decimal
  end
end
