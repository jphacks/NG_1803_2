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
  def ruimoji
    @drink_names = DrinkName.where(language: 0).map{|drink_name| drink_name.name}
    ruimoji = Ruimoji.new
    ruimoji.build(@drink_names)
    ruimoji_db_path = Rails.root.join('public/ruimoji', 'ruimoji.data')
    ruimoji.serialize(ruimoji_db_path)

    render json: "Done!"
  end
  def ruimoji_search
    ruimoji = Ruimoji.new
    ruimoji.build(DrinkName.where(language: 0).map{|drink_name| drink_name.name})
    result = ruimoji.search(params[:text], 0.6)
    menu_items_menu_drink = {}
    if result.empty? == false
      found_drink_name = DrinkName.find_by(name: result[0], language: 0)
      found_drink = found_drink_name.drink
      menu_items_menu_drink = {
          menu_drink_id: found_drink.id,
          drink_names: found_drink.drink_names.order(:language).map{|drink_name| drink_name.name},
          language: 0,
          option: [],
          points: [0, 0, 0, 0]
      }

    end
    render json: [result, menu_items_menu_drink]
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
    items = []
    File.open(image_path, 'r') do |fp|
      items = GoogleVisionAPI.ocr_menu(fp.read)
    end

    p items

    menu_items_menu_drinks = []

    # Ruimojiデータの取得
    ruimoji = Ruimoji.new
    ruimoji.build(DrinkName.where(language: 0).map{|drink_name| drink_name.name})

    items.each do |item|
      # 各テキストで，曖昧検索を行う
      result = ruimoji.search(item[:text], 0.6)
      p [item[:text], result]

      if result.empty? == false
        # 認識できたアイテム
        found_drink_name = DrinkName.find_by(name: result[0], language: 0)
        found_drink = found_drink_name.drink

        menu_items_menu_drink = {
            menu_drink_id: found_drink.id,
            drink_names: found_drink.drink_names.order(:language).map{|drink_name| drink_name.name},
            language: 0,
            option: [],
            points: [item[:left], item[:top], item[:right], item[:bottom]]
        }

        menu_items_menu_drinks << menu_items_menu_drink

      else
        # 認識できませんでした…
      end
    end


    render json: {
      menu_items_menu_drinks: menu_items_menu_drinks
    }
  end
end
