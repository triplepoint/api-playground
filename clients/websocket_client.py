from websockets.sync.client import connect

if __name__ == "__main__":
    with connect("ws://localhost:8008/websocket/ws") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv(decode=True)
        print(f"Received: {message}")
