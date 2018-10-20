class CreateDrinkTastes < ActiveRecord::Migration[5.1]
  def change
    create_table :drink_tastes do |t|

      t.timestamps
    end
  end
end
