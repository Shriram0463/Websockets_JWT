from fastapi import FastAPI, WebSocket
from jwt_service import decode_jwt

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            jwt_token = await websocket.receive_text()
            print("")
            print(f"Received JWT Token: {jwt_token}")
            print("")
            decoded_message = decode_jwt(jwt_token)
            print(f"Decoded message: {decoded_message}")
            print("")
            await websocket.send_text(f"Message received and decoded: {decoded_message}")
    except Exception as e:
        print(f"WebSocket connection closed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
