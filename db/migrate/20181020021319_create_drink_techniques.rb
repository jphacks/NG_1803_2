class CreateDrinkTechniques < ActiveRecord::Migration[5.1]
  def change
    create_table :drink_techniques do |t|
      t.references :drink
      t.integer :language
      t.string :name
      t.text :description

      t.timestamps
    end
  end
end
