from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/generate", response_class=HTMLResponse)
def generate_plan(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    goal: str = Form(...)
):
    name = name.strip()
    gender = gender.strip()

    if not name:
        plan = "Please enter your name."

    elif age < 5 or age > 100:
        plan = "Please enter a valid age."

    elif goal == "fitness":
        plan = """
Day 1: Brisk Walking - 20 minutes
Day 2: Cycling - 20 minutes
Day 3: Light Jogging - 15 minutes
Day 4: Rest and Stretching
Day 5: Walking + Light Exercise - 25 minutes
Day 6: Outdoor Sport - 30 minutes
Day 7: Rest and Gentle Stretching
"""

    elif goal == "strength":
        plan = """
Day 1: Squats + Wall Push-ups
Day 2: Light Strength Exercises
Day 3: Rest and Stretching
Day 4: Squats + Wall Push-ups
Day 5: Bodyweight Exercises
Day 6: Light Strength Activity
Day 7: Rest and Gentle Stretching
"""

    elif goal == "running":
        plan = """
Day 1: Walking - 15 minutes
Day 2: Walking + Easy Jogging - 15 minutes
Day 3: Rest and Stretching
Day 4: Walking + Easy Jogging - 20 minutes
Day 5: Easy Walking - 20 minutes
Day 6: Easy Jogging - 15 minutes
Day 7: Rest and Gentle Stretching
"""

    elif goal == "active":
        plan = """
Day 1: Walking - 20 minutes
Day 2: Cycling - 20 minutes
Day 3: Outdoor Games - 30 minutes
Day 4: Rest and Light Stretching
Day 5: Walking - 25 minutes
Day 6: Cycling or Sports - 30 minutes
Day 7: Rest and Gentle Stretching
"""

    else:
        plan = """
Day 1: Light Walking - 20 minutes
Day 2: Simple Exercise - 15 minutes
Day 3: Rest and Stretching
Day 4: Walking - 20 minutes
Day 5: Light Exercise - 20 minutes
Day 6: Outdoor Activity - 30 minutes
Day 7: Rest and Gentle Stretching
"""

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "request": request,
            "name": name,
            "age": age,
            "gender": gender,
            "goal": goal,
            "plan": plan
        }
    )