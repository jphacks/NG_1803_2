class CreateDrinkTechniques < ActiveRecord::Migration[5.1]
  def change
    create_table :drink_techniques do |t|

      t.timestamps
    end
  end
end
