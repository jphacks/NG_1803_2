class GoogleVisionAPI
  require 'base64'
  require 'json'
  require 'net/https'
  require 'pp'

  def self.google_vision_api(image_file)
    api_url = "https://vision.googleapis.com/v1/images:annotate?key=#{ENV['CLOUD_VISION_API_KEY']}"

    body = {
        requests: [{
                       image: {
                           content: Base64.strict_encode64(image_file)
                       },
                       features: [
                           {
                               type: 'TEXT_DETECTION',
                               maxResults: 1
                           }
                       ]
                   }]
    }.to_json

    uri = URI.parse(api_url)
    https = Net::HTTP.new(uri.host, uri.port)
    https.use_ssl = true

    request = Net::HTTP::Post.new(uri.request_uri)
    request["Content-Type"] = "application/json"

    return JSON.parse(https.request(request, body).body)
  end

  def self.ocr_menu(image_file)
    res = self.google_vision_api(image_file)
    p res

    width = res['responses'][0]['fullTextAnnotation']['pages'][0]['property']['width']
    height = res['responses'][0]['fullTextAnnotation']['pages'][0]['property']['height']

# OCRの出力結果から，結果を取り出して整形
    blocks = res['responses'][0]['textAnnotations'].slice(1..-1)
    ocr_words = []
    blocks.each do |block|
      text = block['description']
      min_x = block['boundingPoly']['vertices'].map{|point| point['x'] ? point['x']: 0}.min
      min_y = block['boundingPoly']['vertices'].map{|point| point['y'] ? point['y']: 0}.min
      max_x = block['boundingPoly']['vertices'].map{|point| point['x'] ? point['x']: width}.max
      max_y = block['boundingPoly']['vertices'].map{|point| point['y'] ? point['y']: height}.max
      ave_x = (min_x + max_x)/2.0
      ave_y = (min_y + max_y)/2.0
      font_size = [(max_x - min_x), (max_y - min_y)].min

      # 縦書き横書きを判別
      direction = 0 # 0は判別不可能, 方向は1が横向き, -1が縦向き
      if text.length > 1
        if max_x - min_x > max_y - min_y
          direction = 1
        else
          direction = -1
        end
      end

      ocr_word = {
          text: text,
          left: min_x,
          top: min_y,
          right: max_x,
          bottom: max_y,
          ave_x: ave_x,
          ave_y: ave_y,
          font_size: font_size,
          direction: direction
      }
      ocr_words << ocr_word
    end

# 最終的なワードを生成
    words = []

# 許容角度
    deg_scope = 10

# 横書きに対応する

# x軸でソート
    ocr_words.sort_by! {|ocr_word| ocr_word[:left]}
    while true
      # p ocr_words.map{|ocr_word| ocr_word[:text]}

      break if ocr_words.empty?
      # 基準となる文字（列）を取得する
      origin = ocr_words.pop
      # 結合するモノを検索する
      i = ocr_words.length - 1
      connected = false
      while true
        break if (i < 0)
        # 擬似 for(i=0;i<ocr_words.length;i++){
        target = ocr_words[i]

        if origin[:direction] >= 0 && target[:direction] >= 0
          dx = target[:ave_x] - origin[:ave_x]
          dy = target[:ave_y] - origin[:ave_y]
          deg_atan2 = Math.atan2(dy, dx) * 180.0 / Math::PI # -180〜180の値
          if (-deg_scope <= deg_atan2 && deg_atan2 <= deg_scope) && (target[:left] - origin[:right] < origin[:font_size])
            #[origin]+[target]
            ocr_words.delete_at(i)
            # puts "#{origin[:text]}と#{target[:text]} (#{deg_atan2}) ()"
            ocr_word = {
                text: origin[:text] + target[:text],
                left: [origin[:left], target[:left]].min,
                top: [origin[:top], target[:top]].min,
                right: [origin[:right], target[:right]].max,
                bottom: [origin[:bottom], target[:bottom]].max,
            }
            ocr_word[:ave_x] = (ocr_word[:left] + ocr_word[:right])/2
            ocr_word[:ave_y] = (ocr_word[:top] + ocr_word[:bottom])/2
            ocr_word[:font_size] = origin[:font_size]
            ocr_word[:direction] = 1

            ocr_words << ocr_word
            connected = true
            break

          elsif (deg_atan2 <= -(180-deg_scope) || 180-deg_scope <= deg_atan2) && (origin[:left] - target[:right] < origin[:font_size])
            #[target]+[origin]
            ocr_words.delete_at(i)
            # puts "#{origin[:text]}と#{target[:text]} (#{deg_atan2}) ()"
            ocr_word = {
                text: target[:text] + origin[:text],
                left: [origin[:left], target[:left]].min,
                top: [origin[:top], target[:top]].min,
                right: [origin[:right], target[:right]].max,
                bottom: [origin[:bottom], target[:bottom]].max,
            }
            ocr_word[:ave_x] = (ocr_word[:left] + ocr_word[:right])/2
            ocr_word[:ave_y] = (ocr_word[:top] + ocr_word[:bottom])/2
            ocr_word[:font_size] = origin[:font_size]
            ocr_word[:direction] = 1
            ocr_words.insert(i, ocr_word)

            connected = true
            break

          end
        end
        # 擬似 }
        i -= 1
      end
      if connected == false
        words << origin
      end
    end

    return words
  end
end

if __FILE__ == $0
  File.open('./_20181020_130456.JPG', 'r') do |fp|
    res = GoogleVisionAPI.ocr_menu(fp.read)
    puts res
  end

end
