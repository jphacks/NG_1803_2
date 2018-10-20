class CreateBaseDocs < ActiveRecord::Migration[5.1]
  def change
    create_table :base_docs do |t|
      t.references :base
      t.integer :language
      t.string :name
      t.text :description

      t.timestamps
    end
  end
end
