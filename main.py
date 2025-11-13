from typing import Union

import markdown
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_docs():
    with open("APIDOC.md", "r", encoding="utf-8") as f:
        md = f.read()
    return HTMLResponse(markdown.markdown(md))


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
