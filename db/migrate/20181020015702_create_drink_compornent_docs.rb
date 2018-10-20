class CreateDrinkCompornentDocs < ActiveRecord::Migration[5.1]
  def change
    create_table :drink_compornent_docs do |t|
      t.references :drink_compornent
      t.integer :language
      t.string :amount_string

      t.timestamps
    end
  end
end
