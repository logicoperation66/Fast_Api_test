from fastapi import FastAPI
from typing import Union, Dict
from random import randint
from pydantic import BaseModel



class Relay(BaseModel):
    id: int
    state: bool

relay0 = Relay(id=0, state=False)
relay1 = Relay(id=1, state=False)
relay2 = Relay(id=2, state=False)

devices: Dict[int, Relay] = {
    0: Relay(id=0, state=False),
    1: Relay(id=1, state=False),
    2: Relay(id=2, state=False),
}

app = FastAPI()


@app.get("/temp1")
async def temp1_read():
    temp1 = randint(0, 100)
    return {"temp1": f"{temp1}"}

@app.get("/temp2")
async def temp2_read():
    temp2 = randint(0,100)
    return {"temp2": f"{temp2}"}

@app.get("/relay1_state")
async def get_relay1_state():
    return {"Relay1": f"{relay1.state}"}


@app.get("/relay/{relay_id}/toggle")
def toggle_relay(relay_id: int):
    if relay_id in devices:
        devices[relay_id].state = not devices[relay_id].state
        return {"id": relay_id, "state": devices[relay_id].state}
    return {"error": "Relay not found"}

