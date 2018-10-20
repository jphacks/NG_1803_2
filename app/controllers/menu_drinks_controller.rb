class MenuDrinksController < ApplicationController
  def show
    menu_drink_id = params[:menu_drink_id]
    language = params[:language]
    language = 0

    drink = Drink.find_by(id: 1)

    drink_doc = drink.drink_docs.find_by(language: language)
    drink_technique_doc = drink.drink_technique.drink_technique_docs.find_by(language: language)
    grass_doc = drink.grass.grass_docs.find_by(language: language)
    base_doc = drink.base.base_docs.find_by(language: language)
    source = drink.source

    render json: {
      menu_drink_id: menu_drink_id,
      language: language,
      drink: {
        min_degree: drink.min_degree,
        max_degree: drink.max_degree,
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
        technique: {
          name: drink_technique_doc.name,
          description: drink_technique_doc.description
        },
        grass: {
          total_amount: drink.grass.total_amount,
          name: grass_doc.name,
          grass_type: grass_doc.grass_type
        },
        base: {
          image_url: drink.base.image_url,
          name: base_doc.name,
          description: base_doc.description
        },
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

          amount_string = ""
          if drink_compornent.drink_compornent_docs.exists?
            amount_string = drink_compornent.drink_compornent_docs.find_by(language: language).amount_string
          end

          {
            compornent_id: compornent.id,
            min_degree: compornent.min_degree,
            max_degree: compornent.max_degree,
            shop_url: compornent.shop_url,
            image_url: compornent.image_url,
            name: compornent_doc.name,
            description: compornent_doc.description,
            amount_number: drink_compornent.amount_number,
            amount_string: amount_string
          }
        }
      }
    }
  end
end
