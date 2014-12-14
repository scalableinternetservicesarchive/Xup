class PartiesController < ApplicationController
  before_action :set_party, only: [:show, :edit, :update, :destroy,:invitetoparty]
  before_action :authenticate_user!, only: [:create, :edit, :new, :update, :destroy]
  protect_from_forgery :except => :destroy 

   respond_to :html, :xml, :json

  # GET /parties
  # GET /parties.json
  def index
    @parties = Party.order(:time)
    @parties = @parties.paginate(:page => params[:page], :per_page => 20)
  end

  def close_parties
    # @parties = Party.all
    @parties = Party.order(:time)
    @myloc = request.location
    p 'this is close parties'


    @closepartylist=[]
    latrang=[0.013,0.026,0.1]
    longrang=[0.016,0.032,0.120]

    lat=34.42
    long= -119.86

    latlow= lat-latrang[0]
    lathigh= lat+latrang[0]

    for i in 0..2

      p 'running forloop'

      latlow= lat-latrang[i]
      lathigh= lat+latrang[i]
      
      longlow= long-longrang[i]
      longhigh= long+longrang[i]


      closep=Party.where(:latitude => latlow...lathigh)

      @closepartylist = closep.where(:longitude => longlow...longhigh)


      #if (@closepartylist.count >10) then
       
      if (@closepartylist.count>10) then
       
       p 'its bigger than ten '
        break

      end

      end

    p @closepartylist
    p @closepartylist.count
    gon.parties=@closepartylist
    gon.latlow=latlow
    gon.longlow=longlow
    gon.lathigh=lathigh
    gon.longhigh=longhigh




  end

  def myparties
      @parties = Party.order(:time)
      
  end

  def count

    @pp = Party.count
    respond_with @pp

  end



  # GET /parties/1
  # GET /parties/1.json
  def show
    @users= User.all
    
  end

  def invitetoparty
    @people = User.search(params[:search])
  
  end


  def upcoming
    current = DateTime.now
    @parties = Party.where("time >= ?", current)
    @parties = @parties.order(:time)
    @parties = @parties.paginate(:page => params[:page], :per_page => 20)
  end

  def past
    current = DateTime.now
    @parties = Party.where("time < ?", current)
    @parties = @parties.order(:time)
    @parties = @parties.paginate(:page => params[:page], :per_page => 20)
  end

  # GET /parties/new
  def new
    @party = Party.new
  end

# GET /parties/1/edit
  def edit
     # owners = JoinMember.where(status: 4) 
     # ownparties = owners.where(user_id:  current_user.id).pluck(:party_id)
     ownparties = JoinMember.where(user_id:  current_user.id, status: 4).pluck(:party_id)
     # ownparties is a party_id from "join_members"

    respond_to do |format|
      if(ownparties.include?(@party.id))
        p "fallthrough"
        format.html { render :edit }
        format.json { render json: @profile.errors, status: :unprocessable_entity }
      else
        p "jump"
        format.html { redirect_to party_path, notice: 'Redirectet to parties, you are not owner of this party.' }
        format.json { render :show, status: :ok, location: @parties }
      end
    end
  end

  def partyrequest
     # @parties = Party.order(:time)
     # @jm = JoinMember.all
     # @user = User.all
  end

  def partyinvites
     # @parties = Party.order(:time)
     # @jm = JoinMember.all
     # @user = User.all
  end

  # POST /parties
  # POST /parties.json
  def create
    @party = Party.new(party_params)
    @party.time = DateTime.new(@party.date.year, @party.date.month, @party.date.day, @party.time.hour, @party.time.min, @party.time.sec, @party.date.zone)
    owner = User.find(current_user.id)
    @join_member = @party.join_members.build(user: owner)
    @join_member.status = 4
    @join_member.save

    respond_to do |format|
      if @party.save
        format.html { redirect_to @party, notice: 'Party was successfully created.' }
        format.json { render :show, status: :created, location: @party }
      else
        format.html { render :new }
        format.json { render json: @party.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /parties/1
  # PATCH/PUT /parties/1.json
  def update
    respond_to do |format|
      if @party.update(party_params)
        format.html { redirect_to @party, notice: 'Party was successfully updated.' }
        format.json { render :show, status: :ok, location: @party }
      else
        format.html { render :edit }
        format.json { render json: @party.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /parties/1
  # DELETE /parties/1.json
  def destroy
    @party.destroy
    respond_to do |format|
      format.html { redirect_to parties_url, notice: 'Party was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_party
      @party = Party.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def party_params
      params.require(:party).permit(:latitude,:longitude,:name, :owner, :date, :time, :location, :description, :participants)
    end
end
