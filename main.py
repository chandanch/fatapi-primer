from typing import Optional
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


@app.get("/api/calculate")
def calculate(x: int, y: int, z: Optional[int] = None):
    """ The above parameters (x, y & z) of the function are
     query or route parameters passed in the request
     we can mark an parameter as optional i.e.
     either query or route parameter using the Optional keyword."""
    if z == 0:
        return fastapi.Response(content='value of z cannot be 0', status_code=400)
    value = x + y

    if z is not None:
        value /= z

    return {
        'value': value,
        'x': x,
        'y': y,
        'z': z
    }


uvicorn.run(app, port=8000, host='localhost')
