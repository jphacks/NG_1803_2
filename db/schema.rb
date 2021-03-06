# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20181020085917) do

  create_table "base_docs", force: :cascade do |t|
    t.integer "base_id"
    t.integer "language"
    t.string "name"
    t.text "description"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["base_id"], name: "index_base_docs_on_base_id"
  end

  create_table "bases", force: :cascade do |t|
    t.string "image_url"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "categories", force: :cascade do |t|
    t.integer "view_type"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "category_docs", force: :cascade do |t|
    t.integer "category_id"
    t.integer "language"
    t.string "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["category_id"], name: "index_category_docs_on_category_id"
  end

  create_table "compornent_docs", force: :cascade do |t|
    t.integer "compornent_id"
    t.integer "language"
    t.string "name"
    t.text "description"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["compornent_id"], name: "index_compornent_docs_on_compornent_id"
  end

  create_table "compornents", force: :cascade do |t|
    t.integer "min_degree"
    t.integer "max_degree"
    t.string "shop_url"
    t.string "image_url"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "drink_compornent_docs", force: :cascade do |t|
    t.integer "drink_compornent_id"
    t.integer "language"
    t.string "amount_string"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["drink_compornent_id"], name: "index_drink_compornent_docs_on_drink_compornent_id"
  end

  create_table "drink_compornents", force: :cascade do |t|
    t.integer "drink_id"
    t.integer "compornent_id"
    t.decimal "amount_number"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["compornent_id"], name: "index_drink_compornents_on_compornent_id"
    t.index ["drink_id"], name: "index_drink_compornents_on_drink_id"
  end

  create_table "drink_docs", force: :cascade do |t|
    t.integer "drink_id"
    t.integer "language"
    t.text "description"
    t.text "recipe"
    t.string "color"
    t.string "location"
    t.string "company"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["drink_id"], name: "index_drink_docs_on_drink_id"
  end

  create_table "drink_names", force: :cascade do |t|
    t.integer "drink_id"
    t.integer "language"
    t.string "name"
    t.boolean "primary"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["drink_id"], name: "index_drink_names_on_drink_id"
  end

  create_table "drink_taste_docs", force: :cascade do |t|
    t.integer "drink_taste_id"
    t.integer "language"
    t.string "taste"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["drink_taste_id"], name: "index_drink_taste_docs_on_drink_taste_id"
  end

  create_table "drink_tastes", force: :cascade do |t|
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "drink_technique_docs", force: :cascade do |t|
    t.integer "drink_technique_id"
    t.integer "language"
    t.string "name"
    t.text "description"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["drink_technique_id"], name: "index_drink_technique_docs_on_drink_technique_id"
  end

  create_table "drink_techniques", force: :cascade do |t|
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "drinks", force: :cascade do |t|
    t.integer "min_degree"
    t.integer "max_degree"
    t.string "image_url"
    t.string "shop_url"
    t.integer "drink_taste_id"
    t.integer "grass_id"
    t.integer "category_id"
    t.integer "source_id"
    t.integer "base_id"
    t.integer "drink_technique_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["base_id"], name: "index_drinks_on_base_id"
    t.index ["category_id"], name: "index_drinks_on_category_id"
    t.index ["drink_taste_id"], name: "index_drinks_on_drink_taste_id"
    t.index ["drink_technique_id"], name: "index_drinks_on_drink_technique_id"
    t.index ["grass_id"], name: "index_drinks_on_grass_id"
    t.index ["source_id"], name: "index_drinks_on_source_id"
  end

  create_table "grass_docs", force: :cascade do |t|
    t.integer "grass_id"
    t.integer "language"
    t.string "name"
    t.string "grass_type"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["grass_id"], name: "index_grass_docs_on_grass_id"
  end

  create_table "grasses", force: :cascade do |t|
    t.integer "total_amount"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "menu_drinks", force: :cascade do |t|
    t.integer "drink_id"
    t.integer "menu_id"
    t.decimal "min_x"
    t.decimal "min_y"
    t.decimal "max_x"
    t.decimal "max_y"
    t.string "ocr_string"
    t.string "ocr_language"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["drink_id"], name: "index_menu_drinks_on_drink_id"
    t.index ["menu_id"], name: "index_menu_drinks_on_menu_id"
  end

  create_table "menu_image_menu_drinks", force: :cascade do |t|
    t.integer "menu_image_id"
    t.integer "menu_drink_id"
    t.decimal "min_x"
    t.decimal "max_x"
    t.decimal "min_y"
    t.string "min_x_bg"
    t.string "max_x_bg"
    t.string "min_y_bg"
    t.string "max_y_bg"
    t.boolean "scanable"
    t.string "ocr_string"
    t.integer "ocr_language"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["menu_drink_id"], name: "index_menu_image_menu_drinks_on_menu_drink_id"
    t.index ["menu_image_id"], name: "index_menu_image_menu_drinks_on_menu_image_id"
  end

  create_table "menu_images", force: :cascade do |t|
    t.integer "menu_id"
    t.integer "user_id"
    t.string "image_url"
    t.text "row"
    t.integer "lat"
    t.integer "lon"
    t.integer "alt"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["menu_id"], name: "index_menu_images_on_menu_id"
    t.index ["user_id"], name: "index_menu_images_on_user_id"
  end

  create_table "menus", force: :cascade do |t|
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "sources", force: :cascade do |t|
    t.string "name"
    t.string "url"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

end
