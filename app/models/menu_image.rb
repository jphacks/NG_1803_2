class MenuImage < ApplicationRecord
  has_many :menu_image_menu_drinks
  has_many :menu_drinks

  belongs_to :menu
end
