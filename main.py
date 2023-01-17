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
def calculate(x: int, y: int, z: Optional[int]):
    # The above parameters (x, y & z) of the function are query or route parameters passed in the request
    # we can mark an parameter as optional i.e. either query or route parameter using the Optional keyword.
    value = (x + y) * z if z else x + y
    return {
        'value': value
    }


uvicorn.run(app, port=8000, host='localhost')
