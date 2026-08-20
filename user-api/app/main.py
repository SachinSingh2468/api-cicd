from fastapi import FastAPI

app = FastAPI(title="User API")


@app.get("/")
def root():
    return {
        "service": "user-api",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/users")
def users():
    return {
        "users": [
            {"id": 1, "name": "Sachin"},
            {"id": 2, "name": "Rahul"},
            {"id": 3, "name": "Amit"}
        ]
    }
