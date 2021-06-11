from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    lang : str,
    text : str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/translate")
def translate(item : Item):
    if item.lang == 'en':
        return {"lang": "fr", "translation" : "Bonjour"}