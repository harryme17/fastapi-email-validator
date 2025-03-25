from fastapi import FastAPI
from controller import router as email_router

app = FastAPI(title="Email & Domain Validator API")

# Include routes
app.include_router(email_router)

@app.get("/")
def home():
    return {"message": "Email Validator API is running!"}
