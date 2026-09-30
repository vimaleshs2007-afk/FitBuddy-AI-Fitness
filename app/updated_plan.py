import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")


def update_workout_plan(original_plan, feedback):

    prompt = f"""
    Here is the user's existing workout plan:

    {original_plan}

    User feedback:
    {feedback}

    Create an updated 7-day workout plan based on
    the feedback.

    Keep the plan structured and easy to follow.
    """

    response = model.generate_content(prompt)

    return response.text
