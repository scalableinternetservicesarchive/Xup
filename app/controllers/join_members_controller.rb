class JoinMembersController < ApplicationController
  # status indicate the request, 0 means pending, 1 means invited, 2 means accepted, 3 means rejected, 4 means owner.
  respond_to :html, :xml, :json
  before_action :set_join_member, only: [:show, :edit, :update, :destroy]

  def index
    @join_members = JoinMember.all
    
    respond_with(@join_members)
    
  end

  def show
    respond_with(@join_member)
  end

  def new
    @join_member = JoinMember.new
    respond_with(@join_member)
  end

  def edit

  end

  def accept
    @join_member = JoinMember.where(user_id: params[:user_id], party_id: params[:party_id]).first
    @join_member.status = 2
    @join_member.save
    flash[:notice] = "Successfully accepted."
    redirect_to :back
  end

  def reject
    @join_member = JoinMember.where(user_id: params[:user_id], party_id: params[:party_id]).first
    @join_member.status = 3
    @join_member.save
    flash[:notice] = "Successfully rejected."
    redirect_to :back
  end

  def join
    @join_member = JoinMember.where(user_id: params[:user_id], party_id: params[:party_id]).first
    @join_member.status = 2
    @join_member.save
    flash[:notice] = "Successfully joined."
    redirect_to :back
  end

  def createasinvite
    user = User.find(params[:user_id])
    party = Party.find(params[:party_id])

    @join_member = party.join_members.build(user: user)
    @join_member.status = 1
    @join_member.save
    redirect_to :back

  end

  def create
    p 'running create'
    # @join_member = JoinMember.new(join_member_params)
    
    user = User.find(params[:user_id])
    party = Party.find(params[:party_id])

    @join_member = party.join_members.build(user: user)
    
    # status indicate the request, 0 means pending, 1 means invited, 2 means accepted, 3 means rejected, 4 means owner.
    @join_member.status = 0
    @join_member.save
    #respond_with(@join_member)
    redirect_to parties_path
  end

  # def createaspartyowner
    
    # user = User.find(params[:user_id])
    # party = Party.find(params[:party_id])

    # @join_member = party.join_members.build(user: user)
    # @join_member.status = 4
    # @join_member.save
    
    # redirect_to parties_show_path
  # end

  def update
    @join_member.update(join_member_params)
    respond_with(@join_member)
  end

  def destroy
    @join_member.destroy
    redirect_to :back
  end

  private
    def set_join_member
      @join_member = JoinMember.find(params[:id])
    end

    def join_member_params
      params.require(:join_member).permit(:user_id, :party_id,:status)
    end
end
