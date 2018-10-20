class DrinkTechnique < ApplicationRecord
  has_many :drink_technique_docs
  has_many :drinks
end
