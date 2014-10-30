require 'test_helper'

class PartiesControllerTest < ActionController::TestCase
  setup do
    @party = parties(:one)
    @update = {
        name: "party 2",
        owner: "Peter",
        date: "2014-10-31 20:22:00",
        time: "2014-10-31 20:22:00",
        location: "Goleta",
        description: "A good party",
        participants: "Peter, Alice, Bob"
    }
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:parties)
  end

  test "should get new" do
    sign_in users(:one)
    get :new
    assert_response :success
  end

  test "should create party" do
    sign_in users(:one)
    assert_difference('Party.count') do
       post :create, party: @update
    end

    assert_redirected_to party_path(assigns(:party))
  end

  test "should show party" do
    get :show, id: @party
    assert_response :success
  end

  test "should get edit" do
    sign_in users(:one)
    get :edit, id: @party
    assert_response :success
  end

  test "should update party" do
    sign_in users(:one)
    patch :update, id: @party, party: @update
    assert_redirected_to party_path(assigns(:party))
  end

  test "should destroy party" do
    sign_in users(:one)
    assert_difference('Party.count', -1) do
      delete :destroy, id: @party
    end

    assert_redirected_to parties_path
  end
end
