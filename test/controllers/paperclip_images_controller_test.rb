require 'test_helper'

class PaperclipImagesControllerTest < ActionController::TestCase
  setup do
    @paperclip_image = paperclip_images(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:paperclip_images)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create paperclip_image" do
    assert_difference('PaperclipImage.count') do
      post :create, paperclip_image: {  }
    end

    assert_redirected_to paperclip_image_path(assigns(:paperclip_image))
  end

  test "should show paperclip_image" do
    get :show, id: @paperclip_image
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @paperclip_image
    assert_response :success
  end

  test "should update paperclip_image" do
    patch :update, id: @paperclip_image, paperclip_image: {  }
    assert_redirected_to paperclip_image_path(assigns(:paperclip_image))
  end

  test "should destroy paperclip_image" do
    assert_difference('PaperclipImage.count', -1) do
      delete :destroy, id: @paperclip_image
    end

    assert_redirected_to paperclip_images_path
  end
end
