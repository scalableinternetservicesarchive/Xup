class RegistrationsController < Devise::RegistrationsController

  def create
    super
    
    resource.skip_confirmation!

    resource.profile = Profile.new(
      first_name: resource.name.split[0],
      last_name: resource.name.split[1]
    )
  end
 
  private

  def sign_up_params
    params.require(:user).permit(:name, :email, :password, :password_confirmation)
  end
 
  def account_update_params
    params.require(:user).permit(:name, :email, :password, :password_confirmation, :current_password)
  end
end
