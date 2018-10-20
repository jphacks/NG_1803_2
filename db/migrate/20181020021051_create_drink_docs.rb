class CreateDrinkDocs < ActiveRecord::Migration[5.1]
  def change
    create_table :drink_docs do |t|
      t.references :drink
      t.integer :language
      t.text :description
      t.text :recipe
      t.string :color
      t.string :location
      t.string :company

      t.timestamps
    end
  end
end
