from fastapi import APIRouter, WebSocket

from api.datatypes import (
    get_random_pet,
    get_random_pet_output,
)

router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive()

        pet = get_random_pet("Sparky")
        pet_output = get_random_pet_output(pet)
        
        await websocket.send_json(
            {
                "message": f"Server received: {data}",
                "response": {"latest_pet": pet_output},
            }
        )
