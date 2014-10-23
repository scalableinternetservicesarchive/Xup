class CreateSubmissions < ActiveRecord::Migration
  def change
    create_table :submissions do |t|
      t.string :title
      t.string :url
      t.references :community

      t.timestamps
    end
  end
end
