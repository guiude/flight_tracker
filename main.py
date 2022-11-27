import uvicorn
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

#merged old main with flighttracker.py
if __name__ == '__main__':
    uvicorn.run('flighttracker:app', host='0.0.0.0', port=8000, reload=True)
