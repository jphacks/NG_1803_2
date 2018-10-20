class MenuImagesController < ApplicationController
  def new
    res = ""
    image_path = Rails.root.join('public/menu_images', '_20181020_130456.JPG')

    File.open(image_path, 'r') do |fp|
      res = GoogleVisionAPI.ocr_menu(fp.read)
    end

    puts res

    render json: res

  end
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

    # ファイルを開いてOCRを行う
    res = ""
    File.open(image_path, 'r') do |fp|
      res = GoogleVisionAPI.ocr_menu(fp.read)
    end

    puts res

    render json: {
      menu_items_menu_drinks: [
        {
          menu_drink_id: 1,
          drink_names: ['ザ・プレミアム・モルツ 香るエール', 'The Premium Malt\'s' , '优质麦芽'],
          points: [0, 0.01, 0.1, 0.15],
          language: 0,
          option: []
        }
      ]
    }
  end
end
