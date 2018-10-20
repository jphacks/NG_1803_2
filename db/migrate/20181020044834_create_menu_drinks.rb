class CreateMenuDrinks < ActiveRecord::Migration[5.1]
  def change
    create_table :menu_drinks do |t|
      t.references :drink
      t.references :menu
      t.decimal :min_x
      t.decimal :min_y
      t.decimal :max_x
      t.decimal :max_y
      t.string :ocr_string
      t.string :ocr_language

      t.timestamps
    end
  end
end
