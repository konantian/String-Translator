import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Translate:
    def __init__(self):
        pass

    def translate(self, lang, text, output):
        if output == "fr":
            return "Bonjour"
        elif output == "sp":
            return "Hola"
        elif output == "zh":
            return "你好"
        elif output == "jp":
            return "こんにちは"
        elif output == "ar":
            return "مرحبا"
        elif output == "ko":
            return "안녕하세요"
        elif output == "hd":
            return "नमस्ते"

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)