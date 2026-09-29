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
        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "request": request,
                "name": "",
                "age": age,
                "gender": gender,
                "goal": goal,
                "plan": "Please enter your name.",
                "schedule": []
            }
        )

    if age < 5 or age > 100:
        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "request": request,
                "name": name,
                "age": age,
                "gender": gender,
                "goal": goal,
                "plan": "Please enter a valid age.",
                "schedule": []
            }
        )

    schedule = [
        {
            "day": "Day 1",
            "activity": "Walking",
            "duration": "20 minutes"
        },
        {
            "day": "Day 2",
            "activity": "Bodyweight Exercises",
            "duration": "20 minutes"
        },
        {
            "day": "Day 3",
            "activity": "Cycling",
            "duration": "25 minutes"
        },
        {
            "day": "Day 4",
            "activity": "Rest & Stretching",
            "duration": "15 minutes"
        },
        {
            "day": "Day 5",
            "activity": "Jogging",
            "duration": "20 minutes"
        },
        {
            "day": "Day 6",
            "activity": "Strength Exercises",
            "duration": "25 minutes"
        },
        {
            "day": "Day 7",
            "activity": "Light Walking & Recovery",
            "duration": "20 minutes"
        }
    ]

    plan = (
        "Follow this weekly activity plan. "
        "Start gently, take breaks, stay hydrated, "
        "and increase activity gradually."
    )

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "request": request,
            "name": name,
            "age": age,
            "gender": gender,
            "goal": goal,
            "plan": plan,
            "schedule": schedule
        }
    )