class PaperclipImagesController < ApplicationController
  before_action :set_paperclip_image, only: [:show, :edit, :update, :destroy]

  def index
    @paperclip_images = PaperclipImage.all
    respond_with(@paperclip_images)
  end

  def show
    respond_with(@paperclip_image)
  end

  def new
    @paperclip_image = PaperclipImage.new
    respond_with(@paperclip_image)
  end

  def edit
  end

  def create
    @paperclip_image = PaperclipImage.new(paperclip_image_params)
    @paperclip_image.save
    respond_with(@paperclip_image)
  end

  def update
    @paperclip_image.update(paperclip_image_params)
    respond_with(@paperclip_image)
  end

  def destroy
    @paperclip_image.destroy
    respond_with(@paperclip_image)
  end

  private
    def set_paperclip_image
      @paperclip_image = PaperclipImage.find(params[:id])
    end

    def paperclip_image_params
      params[:paperclip_image]
    end
end
