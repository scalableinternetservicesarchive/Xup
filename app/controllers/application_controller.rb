class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :exception

  # ensure the user has provided all the necessary information 
  #before accessing a specific resource.
  #You can use it in a before_filter like so: 
  #before_filter :ensure_signup_complete, only: [:new, :create, :update, :destroy]
 
  def ensure_signup_complete
    # Ensure we don't go into an infinite loop
    
    return if action_name == 'finish_signup'
      
    # Redirect to the 'finish_signup' page if the user
    # email hasn't been verified yet
    if current_user && !current_user.email_verified?
      # change the redirect to:
      # # redirect to '/profiles/4/edit'  after signing up first time
      # if user allready exist redirect to '/upcoming'

      redirect_to finish_signup_path(current_user)
    end
  end

 
end
