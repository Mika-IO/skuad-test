from fastapi import FastAPI

'''
    Implementar uma API com as funcionalidades das atividades propostas
'''

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
