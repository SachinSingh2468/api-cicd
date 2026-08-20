from fastapi import FastAPI

app = FastAPI(title="Payment API")


@app.get("/")
def root():
    return {
        "service": "payment-api",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/payments")
def payments():
    return {
        "payments": [
            {"id": 501, "amount": 1500, "status": "success"},
            {"id": 502, "amount": 2500, "status": "success"},
            {"id": 503, "amount": 800, "status": "pending"}
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
