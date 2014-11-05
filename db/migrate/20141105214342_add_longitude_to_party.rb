class AddLongitudeToParty < ActiveRecord::Migration
  def change
    add_column :parties, :longitude, :decimal
  end
end
