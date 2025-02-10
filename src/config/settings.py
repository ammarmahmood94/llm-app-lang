import os
from dotenv import load_dotenv

# loading environment variable from the .env file
load_dotenv()

# Retrieve Values
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

