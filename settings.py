import os

DEBUG = os.getenv('DEBUG', False)
SECRET_KEY = os.getenv('SECRET_KEY')

ROOT_URL = os.getenv('ROOT_URL', 'http://localhost:5000')

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')