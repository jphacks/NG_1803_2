class CreateDrinkTechniqueDocs < ActiveRecord::Migration[5.1]
  def change
    create_table :drink_technique_docs do |t|
      t.references :drink_technique
      t.integer :language
      t.string :name
      t.text :description

      t.timestamps
    end
  end
end
