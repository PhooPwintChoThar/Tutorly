from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from controllers.tutor_controller import TutorController
import uvicorn


app = FastAPI()

# Add session middleware
app.add_middleware(
    SessionMiddleware,
    secret_key="your_secret_key_here", 
    same_site="lax",  # Change from "none"
    https_only=False, 
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Create controller instance
tutor_controller = TutorController()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    tutor_controller.ensure_user_session(request.session)
    return templates.TemplateResponse("tutor.html", {"request": request})


@app.post("/api/create_session")
async def create_session(request: Request):
    tutor_controller.ensure_user_session(request.session) 
    return tutor_controller.create_session(request.session)


@app.post("/api/send_query")
async def send_query(request: Request):
    data = await request.json()
    return tutor_controller.send_query(request.session, data)

# Run the server
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=3000,
        reload=True
    )