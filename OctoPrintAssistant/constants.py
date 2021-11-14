import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "api-key")
OCTOPRINT_PORT = os.getenv("OCTOPRINT_PORT", 5000)
OCTOPRINT_ADDRESS = os.getenv("OCTOPRINT_ADDRESS")
OCTOPRINT_PROTOCOL = os.getenv("OCTOPRINT_PROTOCOL", "http")
OCTOPRINT_X_API_KEY = os.getenv("OCTOPRINT_X_API_KEY")
MASTER_NAME = os.getenv("MASTER_NAME", "Master")

if str(os.getenv("DEBUG")).lower() == "true":
    print(f"API_KEY: {API_KEY}")
    print(f"OCTOPRINT_PORT: {OCTOPRINT_PORT}")
    print(f"OCTOPRINT_ADDRESS: {OCTOPRINT_ADDRESS}")
    print(f"OCTOPRINT_PROTOCOL: {OCTOPRINT_PROTOCOL}")
    print(f"OCTOPRINT_X_API_KEY: {OCTOPRINT_X_API_KEY}")
    print(f"MASTER_NAME: {MASTER_NAME}")


GENERAL_OCTOPRINT_HEADER = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "x-api-key": OCTOPRINT_X_API_KEY
}