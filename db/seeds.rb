# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

unless DrinkTaste.find_by(id: 1)
  DrinkTaste.create!(id: 1)
end
unless DrinkTasteDoc.find_by(id: 1)
  DrinkTasteDoc.create!(id: 1,
                        drink_taste_id: 1,
                        language: 0,
                        taste: "中甘辛口"
  )
end
unless Compornent.find_by(id: 1)
  Compornent.create!(id: 1,
                     min_degree: 0,
                     max_degree: 0,
                     shop_url: "",
                     image_url: ""
  )
end
unless CompornentDoc.find_by(id: 1)
  CompornentDoc.create!(id: 1,
                        compornent_id: 1,
                        language: 0,
                        name: "テキーラ",
                        description: "おいしいおさけだよ．たぶんね．"
  )
end
unless Grass.find_by(id: 1)
  Grass.create!(id: 1,
                total_amount: 60,
  )
end
unless GrassDoc.find_by(id: 1)
  GrassDoc.create!(id: 1,
                   grass_id: 1,
                   language: 0,
                   name: "カクテルグラス",
                   grass_type: "ショート"
  )
end

unless Source.find_by(id: 1)
  Source.create!(id: 1,
                 name: "サントリーカクテル検索",
                 url: ""
  )
end

unless Category.find_by(id: 1)
  Category.create!(id: 1,
                   view_type: 1
  )
end

unless CategoryDoc.find_by(id: 1)
  CategoryDoc.create!(id: 1,
                      category_id: 1,
                      language: 0,
                      name: "カクテル"
  )
end

unless Base.find_by(id: 1)
  Base.create!(id: 1,
               image_url: ""
  )
end

unless BaseDoc.find_by(id: 1)
  BaseDoc.create!(id: 1,
                  base_id: 1,
                  language: 0,
                  name: "てきいら",
                  description: "強いお酒だよ"
  )
end
unless Drink.find_by(id: 1)
  Drink.create!(id: 1,
                drink_taste_id: 1,
                min_degree: 25,
                max_degree: 30,
                image_url: "",
                shop_url: "",
                grass_id: 1,
                category_id: 1,
                source_id: 1,
                base_id: 1
  )
end
unless DrinkName.find_by(id: 1)
  DrinkName.create!(id: 1,
                    drink_id: 1,
                    language: 0,
                    name: "マルガリータ",
                    primary: true
  )
end
unless DrinkCompornent.find_by(id: 1)
  DrinkCompornent.create!(id: 1,
                          drink_id: 1,
                          compornent_id: 1,
                          amount_number: 0.5
  )
end
unless DrinkDoc.find_by(id: 1)
  DrinkDoc.create!(id: 1,
                   drink_id: 1,
                   language: 0,
                   description: "とっても美味しいお酒だよ！すごーい！",
                   recipe: "気合いと根性でまぜる",
                   color: "白",
                   location: "",
                   company: ""
  )

end
unless DrinkTechnique.find_by(id: 1)
  DrinkTechnique.create!(id: 1,
                         drink_id: 1,
                         language: 0,
                         name: "シェイク",
                         description: "ふります"
  )
end