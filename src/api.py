from fastapi import FastAPI

'''
    Implementar uma API com as funcionalidades dos Script1 Script2
'''

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
