class DrinkCompornent < ApplicationRecord
  has_many :drink_compornent_docs

  belongs_to :drink
  belongs_to :compornent
end
