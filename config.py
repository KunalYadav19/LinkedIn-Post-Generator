import os
from dotenv import load_dotenv
import google.generativeai as genai

def load_api():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print('Gemini API key was not found in the .env file')
    else:
        print('Gemini API key was successfully loaded from the .env file')
    
    return api_key


def configure_api():
    api_key = load_api()
    genai.configure(api_key=api_key)


def get_model():
    configure_api()
    gemini_model = "gemini-2.5-flash"
    model = genai.GenerativeModel(gemini_model)

    return model
if __name__ == "__main__":
    get_model()
    resp = get_model().generate_content("What is capital of India?")
    print(resp.text)