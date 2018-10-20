class Compornent < ApplicationRecord
  has_many :drink_compornents
  has_many :drinks, through: :drink_compornents
  has_many :compornent_docs
end
