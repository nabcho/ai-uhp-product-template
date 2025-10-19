# app/main.py
# Synesis auto-deploy test v1.6 — added HEAD method support for uptime monitors
from fastapi import FastAPI, Response

# ➊ Create the FastAPI app instance
app = FastAPI(
    title="NetSentry API",
    version="0.1",
    description="Base API for the AI-UHP product family."
)

# ➋ Define a simple root route to test health (supports GET and HEAD)
@app.api_route("/", methods=["GET", "HEAD"])
def root():
    """Root endpoint for quick health check (GET and HEAD supported)."""
    return {"message": "✅ NetSentry API is alive and running!"}
