class MenuImagesController < ApplicationController
  def create
    render json: {
      menu_items_menu_drinks: [
        {
          menu_drink_id: 0,
          drink_names: ['ザ・プレミアム・モルツ 香るエール', 'The Premium Malt\'s' , '优质麦芽'],
          points: [0, 10, 100, 150],
          language: 0,
          option: []
        }
      ]
    }
  end
end
