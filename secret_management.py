import os

api_key = os.getenv("MY_API_KEY")

if api_key is None:
    print("API key is missing")
else:
    print("API key loaded successfully")