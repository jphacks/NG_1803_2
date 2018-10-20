class DrinkTaste < ApplicationRecord
  has_many :drinks
  has_many :drink_taste_docs
end
