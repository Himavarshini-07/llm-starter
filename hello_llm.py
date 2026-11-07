import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Find and load the .env file
env_path = Path(__file__).with_name(".env")
load_dotenv(dotenv_path=env_path)

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Check API key
if not env_path.exists():
    print(".env file not found!")

elif not api_key:
    print("API key not found. Check your .env file.")

else:
    try:
        # Connect to Gemini
        client = genai.Client(api_key=api_key)

        print("Connected to Gemini successfully!")

        # Send a message
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents="Hello Gemini! Introduce yourself."
        )

        # Display response
        print("\nGemini Response:")
        print(response.text)

    except Exception as e:
        print("\nError:", e)