from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from core.config import settings
from api.v1.api import api_router

app = FastAPI(title="ZooWildVision")

app.include_router(api_router, prefix=settings.API_V1_STR)

# Monta o diretório public para servir arquivos estáticos
app.mount("/static", StaticFiles(directory="public"), name="static")

# Rota principal que redireciona para o index.html
@app.get("/")
async def root():
    return FileResponse("public/index.html")

# Entrada de execução
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
