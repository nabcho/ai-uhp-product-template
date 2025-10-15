# ---------- Base ----------
FROM python:3.11-slim

# ---------- Metadata ----------
LABEL maintainer="Nabil" \
      version="0.1" \
      description="AI-UHP Product Template - NetSentry Base"

# ---------- System setup ----------
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Copy code ----------
COPY . .

# ---------- Expose port for API ----------
EXPOSE 8080

# ---------- Default command ----------
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
