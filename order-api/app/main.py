from fastapi import FastAPI

app = FastAPI(title="Order API")


@app.get("/")
def root():
    return {
        "service": "order-api",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/orders")
def orders():
    return {
        "orders": [
            {"id": 101, "product": "Laptop"},
            {"id": 102, "product": "Keyboard"},
            {"id": 103, "product": "Mouse"}
        ]
    }



@app.get("/")
def root():
    return {
        "service": "order-api",
        "version": "v1.1.0",
        "status": "running"
    }


@app.get("/version")
def version():
    return {
        "service": "order-api",
        "version": "v1.1.0"
    }

