import cloudinary
import cloudinary.uploader
from flask import current_app

def upload_media(file):
    cloudinary.config(
        cloud_name=current_app.config["CLOUDINARY_CLOUD_NAME"],
        api_key=current_app.config["CLOUDINARY_API_KEY"],
        api_secret=current_app.config["CLOUDINARY_API_SECRET"]
    )
    result = cloudinary.uploader.upload(file)
    return result.get("secure_url")
