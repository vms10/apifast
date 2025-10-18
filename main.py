# archivo principal
import os
from fastapi import FastAPI, File, UploadFile
from typing import Annotated
app = FastAPI()

@app.get("/hola")
async def prueba_root():
    return {"message": "Accediste al endpoint de prueba"}

@app.get("/files")
async def buscar_archivos():
    carpeta = "files"

    # Verifica que la carpeta exista
    if not os.path.exists(carpeta):
        return {"error": f"La carpeta '{carpeta}' no existe."}

    # Lista solo los archivos dentro de la carpeta
    archivos = [
        f for f in os.listdir(carpeta)
        if os.path.isfile(os.path.join(carpeta, f))
    ]
    return {"archivos": archivos}






# Endpoint que guarda el archivo en la carpeta "files"
@app.post("/files")
async def upload_file(
    file: Annotated[UploadFile, File(...)]
):
    # Asegurarte de que exista la carpeta "files"
    os.makedirs("files", exist_ok=True)

    # Ruta completa donde se va a guardar
    save_path = os.path.join("files", os.path.basename(file.filename))

    # Leer el contenido del archivo y escribirlo
    with open(save_path, "wb") as f:
        content = await file.read()
        f.write(content)

    return {"message": f"Archivo guardado como {save_path}", "size": len(content)}


@app.get("/files/{file_name}")
async def contenido_archivo(file_name):
    carpeta = "files"
    
    # Verifica que la carpeta exista
    if not os.path.exists(carpeta):
        return {"error": f"La carpeta '{carpeta}' no existe."}

    # Lista solo los archivos dentro de la carpeta
    archivos = [
        f for f in os.listdir(carpeta)
        if os.path.isfile(os.path.join(carpeta, file_name))
    ]
    return {"archivos": os.path.join(carpeta, file_name)}





