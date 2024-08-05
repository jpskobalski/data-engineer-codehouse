from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("API_KEY")

REDSHIFT_USER = os.getenv("REDSHIFT_USER")
REDSHIFT_PASSWORD = os.getenv("REDSHIFT_PASSWORD")
REDSHIFT_HOST = os.getenv("REDSHIFT_HOST")
REDSHIFT_PORT = os.getenv("REDSHIFT_PORT")
REDSHIFT_DATABASE = os.getenv("REDSHIFT_DATABASE")