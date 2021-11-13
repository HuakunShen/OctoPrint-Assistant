import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "api-key")
OCTOPRINT_PORT = os.getenv("OCTOPRINT_PORT", 5000)
OCTOPRINT_ADDRESS = os.getenv("OCTOPRINT_ADDRESS")
OCTOPRINT_PROTOCOL = os.getenv("OCTOPRINT_PROTOCOL", "http")
OCTOPRINT_X_API_KEY = os.getenv("OCTOPRINT_X_API_KEY")

MASTER_NAME = os.getenv("MASTER_NAME", "Master")