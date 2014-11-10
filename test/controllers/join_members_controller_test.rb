require 'test_helper'

class JoinMembersControllerTest < ActionController::TestCase
  setup do
    @join_member = join_members(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:join_members)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create join_member" do
    assert_difference('JoinMember.count') do
      post :create, join_member: { party_id: @join_member.party_id, user_id: @join_member.user_id }
    end

    assert_redirected_to join_member_path(assigns(:join_member))
  end

  test "should show join_member" do
    get :show, id: @join_member
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @join_member
    assert_response :success
  end

  test "should update join_member" do
    patch :update, id: @join_member, join_member: { party_id: @join_member.party_id, user_id: @join_member.user_id }
    assert_redirected_to join_member_path(assigns(:join_member))
  end

  test "should destroy join_member" do
    assert_difference('JoinMember.count', -1) do
      delete :destroy, id: @join_member
    end

    assert_redirected_to join_members_path
  end
end
