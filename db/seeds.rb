# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

require "csv"

CSV.foreach('db/DB_demo/DrinkTaste.csv', headers: true) do |row|
  unless DrinkTaste.find_by(id: row[0])
    DrinkTaste.create!(id: row[0])
  end
end

CSV.foreach('db/DB_demo/DrinkTasteDoc.csv', headers: true) do |row|
  unless DrinkTasteDoc.find_by(id: row[0])
    DrinkTasteDoc.create!(id: row[0],
                          drink_taste_id: row[1],
                          language: row[2],
                          taste: row[3]
    )
  end
end

CSV.foreach('db/DB_demo/Compornent.csv', headers: true) do |row|
  unless Compornent.find_by(id: row[0])
    Compornent.create!(id: row[0],
                       min_degree: row[1],
                       max_degree: row[2],
                       shop_url: row[3],
                       image_url: row[4]
    )
  end
end

CSV.foreach('db/DB_demo/CompornentDoc.csv', headers: true) do |row|
  unless CompornentDoc.find_by(id: row[0])
    CompornentDoc.create!(id: row[0],
                          compornent_id: row[1],
                          language: row[2],
                          name: row[3],
                          description: row[4]
    )
  end
end

CSV.foreach('db/DB_demo/Grass.csv', headers: true) do |row|
  unless Grass.find_by(id: row[0])
    Grass.create!(id: row[0],
                  total_amount: row[1]
    )
  end
end

CSV.foreach('db/DB_demo/GrassDoc.csv', headers: true) do |row|
  unless GrassDoc.find_by(id: row[0])
    GrassDoc.create!(id: row[0],
                     grass_id: row[1],
                     language: row[2],
                     name: row[3],
                     grass_type: row[4]
    )
  end
end

CSV.foreach('db/DB_demo/Source.csv', headers: true) do |row|
  unless Source.find_by(id: row[0])
    Source.create!(id: row[0],
                   name: row[1],
                   url: row[2]
    )
  end
end

CSV.foreach('db/DB_demo/Category.csv', headers: true) do |row|
  unless Category.find_by(id: row[0])
    Category.create!(id: row[0],
                     view_type: row[1]
    )
  end
end

CSV.foreach('db/DB_demo/Category.csv', headers: true) do |row|
  unless Category.find_by(id: row[0])
    Category.create!(id: row[0],
                     view_type: row[1]
    )
  end
end

CSV.foreach('db/DB_demo/CategoryDoc.csv', headers: true) do |row|
  unless CategoryDoc.find_by(id: row[0])
    CategoryDoc.create!(id: row[0],
                        category_id: row[1],
                        language: row[2],
                        name: row[3]
    )
  end
end

CSV.foreach('db/DB_demo/Base.csv', headers: true) do |row|
  unless Base.find_by(id: row[0])
    Base.create!(id: row[0],
                 image_url: row[1]
    )
  end
end

CSV.foreach('db/DB_demo/BaseDoc.csv', headers: true) do |row|
  unless BaseDoc.find_by(id: row[0])
    BaseDoc.create!(id: row[0],
                    base_id: row[1],
                    language: row[2],
                    name: row[3],
                    description: row[4]
    )
  end
end

CSV.foreach('db/DB_demo/DrinkTechnique.csv', headers: true) do |row|
  unless DrinkTechnique.find_by(id: row[0])
    DrinkTechnique.create!(id: row[0])
  end
end

CSV.foreach('db/DB_demo/Drink.csv', headers: true) do |row|
  unless Drink.find_by(id: row[0])
    Drink.create!(id: row[0],
                  drink_taste_id: row[1],
                  min_degree: row[2],
                  max_degree: row[3],
                  image_url: row[4],
                  shop_url: row[5],
                  grass_id: row[6],
                  category_id: row[7],
                  source_id: row[8],
                  base_id: row[9],
                  drink_technique_id: row[10]
    )
  end
end

CSV.foreach('db/DB_demo/DrinkName.csv', headers: true) do |row|
  unless DrinkName.find_by(id: row[0])
    DrinkName.create!(id: row[0],
                      drink_id: row[1],
                      language: row[2],
                      name: row[3],
                      primary: row[4]
    )
  end
end

CSV.foreach('db/DB_demo/DrinkCompornent.csv', headers: true) do |row|
  unless DrinkCompornent.find_by(id: row[0])
    DrinkCompornent.create!(id: row[0],
                            drink_id: row[1],
                            compornent_id: row[2],
                            amount_number: row[3]
    )
  end
end


CSV.foreach('db/DB_demo/DrinkCompornentDoc.csv', headers: true) do |row|
  unless DrinkCompornentDoc.find_by(id: row[0])
    DrinkCompornentDoc.create!(id: row[0],
                               drink_compornent_id: row[1],
                               language: row[2],
                               amount_string: row[3]
    )
  end
end

CSV.foreach('db/DB_demo/DrinkDoc.csv', headers: true) do |row|
  unless DrinkDoc.find_by(id: row[0])
    DrinkDoc.create!(id: row[0],
                     drink_id: row[1],
                     language: row[2],
                     description: row[3],
                     recipe: row[4],
                     color: row[5],
                     location: row[6],
                     company: row[7]
    )
  end
end

CSV.foreach('db/DB_demo/DrinkTechniqueDoc.csv', headers: true) do |row|
  unless DrinkTechniqueDoc.find_by(id: row[0])
    DrinkTechniqueDoc.create!(id: row[0],
                              drink_technique_id: row[1],
                              language: row[2],
                              name: row[3],
                              description: row[4]
    )
  end
end

