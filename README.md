from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

goal = input("Enter your fitness goal: ")
days = input("Enter workout days per week: ")

prompt = f"""
Create a simple fitness plan for:
Goal: {goal}
Workout days: {days}

Give exercises, duration and rest days.
Keep it simple and safe.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\n--- FitBuddy AI Fitness Plan ---")
print(response.text)
