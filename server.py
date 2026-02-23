from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
clients = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_methods=[],
    allow_headers=[],
)

@app.websocket(ws)
async def websocket_endpoint(ws WebSocket)
    await ws.accept()
    clients.append(ws)
    try
        while True
            msg = await ws.receive_text()
            for client in clients
                if client != ws
                    await client.send_text(msg)
    except
        clients.remove(ws)