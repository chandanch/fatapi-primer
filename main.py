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
def calculate(x: int, y: int, z: int):
    # The above parameters of the function are the query parameters passed of the request
    value = (x + y) * z
    return {
        'value': value
    }


uvicorn.run(app, port=8000, host='localhost')
