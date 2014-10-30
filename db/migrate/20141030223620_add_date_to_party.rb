class AddDateToParty < ActiveRecord::Migration
  def self.up
    add_column :parties, :date, :datetime
  end

  def self.down
    remove_column :parties, :date
  end
end
