import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")


def generate_workout_gemini(age, weight, goal, intensity):

    prompt = f"""
    Create a safe, beginner-friendly 7-day fitness plan.

    Age: {age}
    Weight: {weight} kg
    Fitness Goal: {goal}
    Workout Intensity: {intensity}

    Give the plan day by day.

    For each day include:
    - Warm-up
    - Main workout
    - Sets/repetitions or duration
    - Cool-down/recovery

    Keep the response simple and structured.
    Do not provide medical advice.
    """

    response = model.generate_content(prompt)

    return response.text
