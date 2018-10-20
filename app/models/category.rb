class Category < ApplicationRecord
  has_many :drinks
  has_many :category_docs
end
