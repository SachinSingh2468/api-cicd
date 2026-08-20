FROM python:3.14-alpine
WORKDIR /app
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt
COPY app ./app
EXPOSE 8000
CMD ["uvicorn", "app.broken:app", "--host", "0.0.0.0", "--port", "8000"]
