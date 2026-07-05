import os
import google.generativeai as genai
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


class GeminiService:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        genai.configure(
            api_key=api_key
        )

        self.model = genai.GenerativeModel(
            "gemini-1.5-flash"
        )


    def generate_response(self, prompt):

        try:
            response = self.model.generate_content(prompt)

            return response.text

        except Exception as e:

            return (
                "Gemini AI error: "
                + str(e)
            )