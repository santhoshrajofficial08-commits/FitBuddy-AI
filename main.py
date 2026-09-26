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

    # Basic validation
    if not name:
        error = "Please enter your name."
        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "request": request,
                "name": "",
                "goal": goal,
                "plan": error
            }
        )

    if age < 5 or age > 100:
        error = "Please enter a valid age."
        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "request": request,
                "name": name,
                "goal": goal,
                "plan": error
            }
        )

    # Goal-based plan
    if goal == "fitness":
        plan = (
            "Try enjoyable activities such as walking, cycling, "
            "or a sport. Start gently, take breaks, "
            "and build activity gradually."
        )

    elif goal == "strength":
        plan = (
            "Try simple bodyweight movements such as squats "
            "and wall push-ups. Focus on comfortable movement, "
            "good form, and enough rest."
        )

    elif goal == "running":
        plan = (
            "Start with comfortable walking and short periods "
            "of easy jogging if it feels good. Increase gradually "
            "and include rest days."
        )

    elif goal == "active":
        plan = (
            "Add more movement to your day through walking, "
            "outdoor activities, cycling, or games you enjoy. "
            "Take regular breaks and stay hydrated."
        )

    else:
        plan = (
            "Choose an activity you enjoy, start gently, "
            "and build up gradually while taking enough rest."
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
            "plan": plan
        }
    )