class MenuImagesController < ApplicationController
  def create

    # アップデートしたファイル
    uploaded_file = params[:image_data]

    # ファイルネームを生成する
    file_name = "#{SecureRandom.base58(20)}.jpg"

    # ファイルを保存
    image_path = Rails.root.join('public/menu_images', file_name)
    File.open(image_path, 'w+b') do |fp|
      fp.write uploaded_file.read
    end

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
