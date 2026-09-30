import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_nutrition_tip_with_flash(goal):

    prompt = f"""
    Give one short and practical nutrition or recovery tip
    for someone whose fitness goal is: {goal}.

    Keep it simple and general.
    """

    response = model.generate_content(prompt)

    return response.text
