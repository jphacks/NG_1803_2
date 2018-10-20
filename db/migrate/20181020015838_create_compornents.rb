class CreateCompornents < ActiveRecord::Migration[5.1]
  def change
    create_table :compornents do |t|
      t.integer :min_degree
      t.integer :max_degree
      t.string :shop_url
      t.string :image_url

      t.timestamps
    end
  end
end
