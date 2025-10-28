import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PRIVATE_API_KEY = os.getenv("PRIVATE_API_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")

class TestConfig:
    TESTING = True
    PRIVATE_API_KEY = os.getenv("PRIVATE_API_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CLOUDINARY_CLOUD_NAME = None
    CLOUDINARY_API_KEY = None
    CLOUDINARY_API_SECRET = None


