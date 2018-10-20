class CreateDrinkNames < ActiveRecord::Migration[5.1]
  def change
    create_table :drink_names do |t|
      t.references :drink
      t.integer :language
      t.string :name
      t.boolean :primary

      t.timestamps
    end
  end
end
