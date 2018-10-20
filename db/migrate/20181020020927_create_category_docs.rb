class CreateCategoryDocs < ActiveRecord::Migration[5.1]
  def change
    create_table :category_docs do |t|
      t.references :category
      t.integer :language
      t.string :name

      t.timestamps
    end
  end
end
