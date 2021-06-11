from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Translate:
    def __init__(self):
        pass

    def translate(self, lang, text):
        if lang == "en":
            return "Bonjour"

class Item(BaseModel):
    lang : str
    text : str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/translate")
def translate(item : Item):
    trans  = Translate()
    result = trans.translate(item.lang, item.text)
    return {"lang" : "fr", "translation" : result}