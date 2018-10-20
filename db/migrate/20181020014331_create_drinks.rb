class CreateDrinks < ActiveRecord::Migration[5.1]
  def change
    create_table :drinks do |t|
      t.integer :min_degree
      t.integer :max_degree
      t.string :image_url
      t.string :shop_url
      t.references :drink_taste
      t.references :grass
      t.references :category
      t.references :source
      t.references :base
      t.references :drink_technique

      t.timestamps
    end
  end
end
