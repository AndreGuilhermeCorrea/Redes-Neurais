# main.py é o arquivo principal da aplicação, onde é criado o objeto FastAPI e configurado o CORS.

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from api.v1.api import api_router
from fastapi.staticfiles import StaticFiles




app = FastAPI(title="ZooWildVision")

# Configuração do CORS
# Permite que a API seja acessada por qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monta o diretório public para servir arquivos estáticos
app.mount("/static", StaticFiles(directory="public"), name="static")

# Rota principal que redireciona para o index.html
@app.get("/")
async def root():
    return FileResponse("public/index.html")

app.include_router(api_router) 
app.mount("/uploads", StaticFiles(directory="localstorage/img_up"), name="uploads")

# Entrada de execução
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
