import fastapi
import uvicorn

app = fastapi.FastAPI()

print("First Fast API")


@app.get("/healthcheck")
def health_check():
    """
    First API
    """
    return {"status": "OK", "message": "Up & Running!"}


@app.get('/api/calculate')
def calculate():
    value = 2 + 2
    return {
        'value': value
    }


uvicorn.run(app, port=8000, host='localhost')
