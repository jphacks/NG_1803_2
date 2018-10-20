class CreateCompornentDocs < ActiveRecord::Migration[5.1]
  def change
    create_table :compornent_docs do |t|
      t.references :compornent
      t.integer :language
      t.string :name
      t.text :description

      t.timestamps
    end
  end
end
