class CreateMenuDrinks < ActiveRecord::Migration[5.1]
  def change
    create_table :menu_drinks do |t|
      t.references :drink
      t.references :menu
      t.integer :min_x
      t.integer :min_y
      t.integer :max_x
      t.integer :max_y
      t.string :ocr_string
      t.string :ocr_language

      t.timestamps
    end
  end
end
