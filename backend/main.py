from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="Agenda For Dummies API", version="0.1")

# 1. Montamos la carpeta 'frontend' para que FastAPI pueda leer el CSS o JS
# Asegurate de que la carpeta 'frontend' exista en la raíz

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def read_index():
    # 2. Buscamos el archivo index.html dentro de la carpeta frontend
    file_path = os.path.join("frontend", "index.html")
    return FileResponse(file_path)

@app.get("/status")
def get_status():
    return {"status": "Operativo", "pilar": "Inicial"}
    