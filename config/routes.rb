Rails.application.routes.draw do
  
  resources :join_members
  match "/partyrequest/reject" => "join_members#reject", via: [:post], :as => :reject
  match "/partyrequest/accept" => "join_members#accept", via: [:post], :as => :accept

  resources :paperclip_images

  resources :profiles

   #needed for facebook login, and normal login
  devise_for :users, :controllers => { omniauth_callbacks: 'omniauth_callbacks' }

  match '/users/:id/finish_signup' => 'users#finish_signup', via: [:get, :patch], :as => :finish_signup

  # end facebook and normal login

  root 'parties#landingPage'
  resources :parties
  
  get '/upcoming' => 'parties#upcoming'
  get '/about' => 'parties#about'
  get '/help' => 'parties#help'
  get '/index' => 'parties#index'
  get '/past' => 'parties#past'
  get '/new' => 'parties#new'
  get '/login' => 'parties#login'
  get '/signup' => 'parties#signup'
  get '/logout' => 'parties#logout'
  get '/myparties' => 'parties#myparties'
  get '/closeparties' => 'parties#close_parties'
  get '/partyrequest' => 'parties#partyrequest'
  get '/myinvites' => 'parties#partyinvites'

  #when the user scaffold is created, 
  #change parties# to user#, and change the location of the html file myaccount.html.erb
  
  #get '/profiles/' => 'profiles#show'

  match '/profiles/:id' => 'profiles#show', via: [:get], :as => :show

 
  

  #root 'parties#upcoming'
 
  #resources :parties

  #

  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  # root 'welcome#index'

  # Example of regular route:
  #   get 'products/:id' => 'catalog#view'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase

  # Example resource route (maps HTTP verbs to controller actions automatically):
  #   resources :products

  # Example resource route with options:
  #   resources :products do
  #     member do
  #       get 'short'
  #       post 'toggle'
  #     end
  #
  #     collection do
  #       get 'sold'
  #     end
  #   end

  # Example resource route with sub-resources:
  #   resources :products do
  #     resources :comments, :sales
  #     resource :seller
  #   end

  # Example resource route with more complex sub-resources:
  #   resources :products do
  #     resources :comments
  #     resources :sales do
  #       get 'recent', on: :collection
  #     end
  #   end

  # Example resource route with concerns:
  #   concern :toggleable do
  #     post 'toggle'
  #   end
  #   resources :posts, concerns: :toggleable
  #   resources :photos, concerns: :toggleable

  # Example resource route within a namespace:
  #   namespace :admin do
  #     # Directs /admin/products/* to Admin::ProductsController
  #     # (app/controllers/admin/products_controller.rb)
  #     resources :products
  #   end
end
