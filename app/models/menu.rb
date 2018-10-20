class Menu < ApplicationRecord
  has_many :menu_images
  has_many :menu_drinks
end
