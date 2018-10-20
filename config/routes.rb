Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  scope :api do
    get 'menu_images/new', to: 'menu_images#new'
    post 'menu_images/create', to: 'menu_images#create'
    get 'menu_drinks/show', to: 'menu_drinks#show'
  end
end
