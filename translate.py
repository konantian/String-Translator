from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Translate:
    def __init__(self):
        pass

    def translate(self, lang, text, output):
        if lang == "fr":
            return "Bonjour"
        elif lang == "sp":
            return "Hola"

class Item(BaseModel):
    lang : str
    text : str
    output : str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/translate")
def translate(item : Item):
    trans  = Translate()
    result = trans.translate(item.lang, item.text, item.output)
    return {"translation" : result}