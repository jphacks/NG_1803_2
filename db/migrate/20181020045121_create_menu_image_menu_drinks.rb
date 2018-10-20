class CreateMenuImageMenuDrinks < ActiveRecord::Migration[5.1]
  def change
    create_table :menu_image_menu_drinks do |t|
      t.references :menu_image
      t.references :menu_drink
      t.decimal :min_x
      t.decimal :max_x
      t.decimal :min_y
      t.decimal :min_y

      t.string :min_x_bg
      t.string :max_x_bg
      t.string :min_y_bg
      t.string :max_y_bg

      t.boolean :scanable
      t.string :ocr_string
      t.integer :ocr_language

      t.timestamps
    end
  end
end
