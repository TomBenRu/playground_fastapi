from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Konfigurieren Sie Jinja2Templates
templates = Jinja2Templates(directory="templates")

# Simulierte Datenbank für Benutzer und Passwörter
users_db = {
    "user1": "password1",
    "user2": "password2"
}

# Statische Dateien (z.B. CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/login/", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username in users_db and users_db[username] == password:
        return RedirectResponse("/index/", status_code=302)
    else:
        return templates.TemplateResponse("login_form.html", {"request": request,
                                                              "error": "Login fehlgeschlagen. Username oder Password unkorrekt."})


@app.get("/login/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login_form.html", {"request": request})


@app.get("/forgot-password/", response_class=HTMLResponse)
async def forgot_password(request: Request):
    return templates.TemplateResponse("forgot_password_form.html", {"request": request})


@app.post("/new-password/", response_class=HTMLResponse)
async def new_password(request: Request, email: str = Form(...)):
    # Hier könnte der Code stehen, um eine E-Mail mit einem neuen Passwort zu senden
    # Da dies nur ein Beispiel ist, geben wir eine Erfolgsmeldung zurück
    return templates.TemplateResponse("forgot_password_success.html", {"request": request})


@app.get("/index/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index_success.html", {"request": request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
