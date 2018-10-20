class CreateMenuImages < ActiveRecord::Migration[5.1]
  def change
    create_table :menu_images do |t|
      t.references :menu
      t.references :user
      t.string :image_url
      t.text :row
      t.integer :lat
      t.integer :lon
      t.integer :alt

      t.timestamps
    end
  end
end
