class MenuDrinksController < ApplicationController
  def show
    menu_drink_id = params[:menu_drink_id].to_i
    language = params[:language].to_i

    drink = Drink.find_by(id: menu_drink_id)

    drink_doc = drink.drink_docs.find_by(language: language)

    begin
      drink_technique_doc = drink.tequnique.drink_technique_docs.find_by(language: language)
      technique = {
        name: drink_technique_doc.name,
        description: drink_technique_doc.description
      }
    rescue
      technique = {
        name: nil,
        description: nil
      }
    end

    begin
      grass_doc = drink.grass.grass_docs.find_by(language: language)
      grass = {
          total_amount: drink.grass.total_amount,
          name: grass_doc.name,
          grass_type: grass_doc.grass_type
      }
    rescue
      grass = {
          total_amount: -1,
          name: nil,
          grass_type: nil
      }
    end
    begin
      base_doc = drink.base.base_docs.find_by(language: language)
      base = {
          image_url: drink.base.image_url,
          name: base_doc.name,
          description: base_doc.description
      }
    rescue
      base = {
          image_url: drink.base.image_url,
          name: nil,
          description: nil
      }
    end
    source = drink.source

    render json: {
      menu_drink_id: menu_drink_id,
      language: language,
      drink: {
        min_degree: (drink.min_degree ? drink.min_degree : -1),
        max_degree: (drink.min_degree ? drink.max_degree : -1),
        image_url: drink.image_url,
        shop_url: drink.shop_url,
        primary_name: drink.drink_names.find_by(language: language, primary: true).name,
        names: drink.drink_names.where(language: language, primary: false).map {|drink_name| drink_name.name},
        taste: drink.drink_taste.drink_taste_docs.find_by(language: language).taste,
        description: drink_doc.description,
        recipe: drink_doc.recipe,
        color: drink_doc.color,
        location: drink_doc.location,
        company: drink_doc.company,
        technique: technique,
        grass: grass,
        base: base,
        category: {
          view_type: drink.category.view_type,
          name: drink.category.category_docs.find_by(language: language).name
        },
        source: {
          name: source.name,
          url: source.url
        },
        compornents: drink.compornents.map { |compornent|
          compornent_doc = compornent.compornent_docs.find_by(language: language)
          drink_compornent = DrinkCompornent.find_by(drink: drink, compornent: compornent)

          amount_string = drink_compornent.drink_compornent_docs
          if drink_compornent.drink_compornent_docs.exists?
            amount_string = drink_compornent.drink_compornent_docs.find_by(language: language).amount_string
          end

          {
            compornent_id: compornent.id,
            min_degree: (compornent.min_degree ? compornent.min_degree : -1),
            max_degree: (compornent.max_degree ? compornent.max_degree : -1),
            shop_url: compornent.shop_url,
            image_url: compornent.image_url,
            name: compornent_doc.name,
            description: compornent_doc.description,
            amount_number: drink_compornent.amount_number.to_f,
            amount_string: amount_string
          }
        }
      }
    }
  end
end
