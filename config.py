import os
from dotenv import load_dotenv

# Carga .env
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY');

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI');

    SQLALCHEMY_TRACK_MODIFICATIONS = False