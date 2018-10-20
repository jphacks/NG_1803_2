class CreateDrinkTasteDocs < ActiveRecord::Migration[5.1]
  def change
    create_table :drink_taste_docs do |t|
      t.references :drink_taste
      t.integer :language
      t.string :taste

      t.timestamps
    end
  end
end
