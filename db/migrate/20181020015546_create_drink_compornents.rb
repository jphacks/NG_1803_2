class CreateDrinkCompornents < ActiveRecord::Migration[5.1]
  def change
    create_table :drink_compornents do |t|
      t.references :drink
      t.references :compornent
      t.decimal :amount_number

      t.timestamps
    end
  end
end
