import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API with the key
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

def call_gemini_api(expression):
    prompt = f"Evaluate the mathematical expression: {expression}. Provide only the numerical result. Return 0 if the expression is empty."
    try:
        response = model.generate_content(
            contents=[prompt]
        )
        result = response.text
        return result
    except Exception as e:
        return f"Error: {str(e)}"