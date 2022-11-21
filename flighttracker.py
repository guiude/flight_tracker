# File that hosts the request handler for the flight tracker app
from fastapi import FastAPI
from flightdata import get_flight_data

app = FastAPI()


@app.get("/")
async def read_root():
    return {"msg": "Hello, World"}


@app.get("/flights/{flight_code}")
async def retrieve_flight(flight_code):
    data = get_flight_data(flight_code)
    return data