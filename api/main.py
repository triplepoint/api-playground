from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from api import doc, restful, websocket

app = FastAPI(title="API Playground", description="A simple set of example endpoints")


@app.get("/")
def read_docs() -> HTMLResponse:
    return HTMLResponse(doc.html())


app.include_router(restful.router, prefix="/restful", tags=["RESTful"])
app.include_router(websocket.router, prefix="/websocket", tags=["Websocket"])
