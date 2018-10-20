class MenuDrink < ApplicationRecord
  has_many :menu_image_menu_drinks
  has_many :menu_images, through: :menu_image_menu_drinks

  belongs_to :drink
  belongs_to :menu
end
