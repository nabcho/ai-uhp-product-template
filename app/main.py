# app/main.py
from fastapi import FastAPI

# ➊ Create the FastAPI app instance
app = FastAPI(
    title="NetSentry API",
    version="0.1",
    description="Base API for the AI-UHP product family."
)

# ➋ Define a simple root route to test health
@app.get("/")
def root():
    """Root endpoint for quick health check."""
    return {"message": "✅ NetSentry API is alive and running!"}
