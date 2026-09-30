import os

from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from .gemini_generator import generate_workout_gemini
from .gemini_flash_generator import generate_nutrition_tip_with_flash
from .updated_plan import update_workout_plan
from .database import (
    save_user,
    save_plan,
    get_user,
    update_plan,
    get_all_users
)

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates")
)


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@router.post("/generate-workout")
def generate_workout(
    request: Request,
    user_id: str = Form(...),
    name: str = Form(...),
    age: int = Form(...),
    weight: str = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...)
):

    workout_plan = generate_workout_gemini(
        age,
        weight,
        goal,
        intensity
    )

    nutrition_tip = generate_nutrition_tip_with_flash(goal)

    save_user(
        user_id,
        name,
        age,
        weight,
        goal,
        intensity
    )

    save_plan(
        user_id,
        workout_plan,
        nutrition_tip
    )

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "user_id": user_id,
            "name": name,
            "age": age,
            "weight": weight,
            "goal": goal,
            "intensity": intensity,
            "workout_plan": workout_plan,
            "nutrition_tip": nutrition_tip
        }
    )


@router.post("/submit-feedback")
def submit_feedback(
    request: Request,
    user_id: str = Form(...),
    feedback: str = Form(...)
):

    user = get_user(user_id)

    if not user:
        return {"error": "User not found"}

    updated_plan = update_workout_plan(
        user.original_plan,
        feedback
    )

    update_plan(user_id, updated_plan)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "user_id": user.user_id,
            "name": user.name,
            "age": user.age,
            "weight": user.weight,
            "goal": user.goal,
            "intensity": user.intensity,
            "workout_plan": updated_plan,
            "nutrition_tip": user.nutrition_tip,
            "message": "Workout plan updated successfully!"
        }
    )


@router.get("/view-all-users")
def view_all_users(request: Request):

    users = get_all_users()

    return templates.TemplateResponse(
        "all_users.html",
        {
            "request": request,
            "users": users
        }
  )
