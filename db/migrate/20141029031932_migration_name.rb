class MigrationName < ActiveRecord::Migration
    def self.up
         change_table :parties do |t|
             t.change :time, :datetime
         end
    end
      
    def self.down
         change_table :parties do |t|
             t.change :time, :string
         end
    end
end
