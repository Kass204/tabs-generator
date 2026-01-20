from fastapi import FastAPI
from app.modules.users.controller import router as users_router
from app.modules.login.controller import router as login_router

app = FastAPI(
    title="Minha API",
    version="1.0.0"
)

app.include_router(users_router)
app.include_router(login_router)


@app.get("/")
def health_check():
    return {"status": "ok"}
