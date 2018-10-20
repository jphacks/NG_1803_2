class Drink < ApplicationRecord
  has_many :drink_compornents
  has_many :compornents, through: :drink_compornents
  has_many :drink_names
  has_many :drink_docs
  has_many :drink_techniques

  belongs_to :drink_taste
  belongs_to :grass, optional: true
  belongs_to :category
  belongs_to :source
  belongs_to :base
  belongs_to :drink_technique, optional: true
end
