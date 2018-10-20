class CreateGrassDocs < ActiveRecord::Migration[5.1]
  def change
    create_table :grass_docs do |t|
      t.references :grass
      t.integer :language
      t.string :name
      t.string :grass_type

      t.timestamps
    end
  end
end
