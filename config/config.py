import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram Bot Configuration
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    
    # Database Configuration
    DATABASE_URL = os.getenv('DATABASE_URL')
    
    # Redis Configuration
    REDIS_URL = os.getenv('REDIS_URL')
    
    # API Keys
    NEWS_API_KEY = os.getenv('NEWS_API_KEY')
    SCIENCE_DB_API_KEY = os.getenv('SCIENCE_DB_API_KEY')
    
    # Model Paths
    NLP_MODEL_PATH = os.getenv('NLP_MODEL_PATH')
    IMAGE_MODEL_PATH = os.getenv('IMAGE_MODEL_PATH')
